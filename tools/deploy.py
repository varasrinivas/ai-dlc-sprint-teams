#!/usr/bin/env python3
"""
Publish the course player to S3 and invalidate the CloudFront cache.

The player (course/index.html) is a single self-contained file, so a deploy is
one PUT plus one cache invalidation:

    course/index.html
      -> s3://<bucket>/<prefix>/index.html
      -> invalidate /<prefix>/* on the CloudFront distribution
      -> https://<domain>/<prefix>/

Before uploading it runs tools/validate.py and checks the working tree (clean,
on the release branch, in sync with the remote). Those git checks are warnings
by default -- use --strict to make them hard failures.

The upload is skipped when the deployed file already matches the local one, so
re-running is safe and cheap.

Usage:
    python tools/deploy.py                  # validate, upload, invalidate
    python tools/deploy.py --dry-run        # print every step, change nothing
    python tools/deploy.py --strict         # refuse to deploy a dirty tree
    python tools/deploy.py --force          # upload even if S3 is already current
    python tools/deploy.py --skip-validate  # skip tools/validate.py

Requires the AWS CLI on PATH with credentials that can write the bucket and
create invalidations.
"""
import argparse
import hashlib
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PLAYER = ROOT / "course" / "index.html"

# Deploy target. These match the live site; override with the flags below.
BUCKET = "learnings.varasrinivas.com"
PREFIX = "ai-dlc-sprint-teams"
DISTRIBUTION = "ESC8HMAS41DRF"
DOMAIN = "learnings.varasrinivas.com"

CONTENT_TYPE = "text/html; charset=utf-8"
CACHE_CONTROL = "public, max-age=300"
RELEASE_BRANCH = "main"

warnings = []


def warn(m):
    warnings.append(m)


def run(cmd, check=True):
    """Run a command and return (returncode, stdout). Never raises on non-zero."""
    # The child may print non-ASCII (validate.py uses em dashes); pin both ends
    # to UTF-8 so a cp1252 console on Windows cannot mangle or crash on it.
    env = {**os.environ, "PYTHONIOENCODING": "utf-8"}
    p = subprocess.run(cmd, capture_output=True, text=True,
                       encoding="utf-8", errors="replace", env=env)
    if check and p.returncode != 0:
        sys.stderr.write((p.stderr or p.stdout or "").strip() + "\n")
    return p.returncode, (p.stdout or "").strip()


def git(*args):
    code, out = run(["git", "-C", str(ROOT), *args], check=False)
    return out if code == 0 else None


def md5(path: Path) -> str:
    h = hashlib.md5()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def git_checks():
    """Warn about anything that would make this deploy hard to trace back."""
    if git("rev-parse", "--git-dir") is None:
        warn("not a git repository -- cannot record what was deployed.")
        return

    if git("status", "--porcelain"):
        warn("working tree has uncommitted changes -- deploying content that is "
             "not committed anywhere.")

    branch = git("rev-parse", "--abbrev-ref", "HEAD")
    if branch and branch != RELEASE_BRANCH:
        warn(f'on branch "{branch}", not "{RELEASE_BRANCH}" -- production would '
             f"run unmerged content.")

    counts = git("rev-list", "--left-right", "--count", f"HEAD...origin/{branch}")
    if counts:
        ahead, _, behind = counts.partition("\t")
        if ahead.strip() != "0":
            warn(f"{ahead.strip()} commit(s) not pushed to origin/{branch} -- the "
                 f"deployed content would not be on the remote.")
        if behind.strip() != "0":
            warn(f"{behind.strip()} commit(s) behind origin/{branch} -- you may be "
                 f"deploying stale content.")


def remote_etag(bucket: str, key: str):
    """Return the deployed object's ETag, or None if it is not there yet."""
    code, out = run(["aws", "s3api", "head-object",
                     "--bucket", bucket, "--key", key,
                     "--query", "ETag", "--output", "text"], check=False)
    if code != 0:
        return None
    return out.strip().strip('"')


def main() -> int:
    # A cp1252 console must not turn a successful deploy into a traceback.
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8", errors="replace")
        except (AttributeError, ValueError):
            pass

    ap = argparse.ArgumentParser(description="Deploy the course player to S3 + CloudFront.")
    ap.add_argument("--bucket", default=BUCKET, help=f"S3 bucket (default: {BUCKET})")
    ap.add_argument("--prefix", default=PREFIX, help=f"key prefix (default: {PREFIX})")
    ap.add_argument("--distribution", default=DISTRIBUTION,
                    help=f"CloudFront distribution id (default: {DISTRIBUTION})")
    ap.add_argument("--file", default=str(PLAYER), help="file to publish (default: the player)")
    ap.add_argument("--dry-run", action="store_true", help="print each step, change nothing")
    ap.add_argument("--strict", action="store_true", help="treat git warnings as failures")
    ap.add_argument("--force", action="store_true", help="upload even if S3 already matches")
    ap.add_argument("--skip-validate", action="store_true", help="skip tools/validate.py")
    ap.add_argument("--no-invalidate", action="store_true", help="skip the CloudFront invalidation")
    args = ap.parse_args()

    src = Path(args.file)
    key = f"{args.prefix.strip('/')}/index.html"
    url = f"https://{DOMAIN}/{args.prefix.strip('/')}/"

    if not src.exists():
        print(f"ERROR: nothing to deploy at {src}", file=sys.stderr)
        return 2
    if shutil.which("aws") is None:
        print("ERROR: the AWS CLI is not on PATH.", file=sys.stderr)
        return 2

    # --- preflight -------------------------------------------------------
    if not args.skip_validate:
        print("Validating the player ...")
        code, out = run([sys.executable, str(ROOT / "tools" / "validate.py")], check=False)
        print("\n".join("  " + ln for ln in out.splitlines()))
        if code != 0:
            print("\nERROR: validation failed -- not deploying.", file=sys.stderr)
            return 1

    git_checks()
    if warnings:
        print()
        for w in warnings:
            print("WARN:", w)
        if args.strict:
            print(f"\nERROR: --strict and {len(warnings)} warning(s) -- not deploying.",
                  file=sys.stderr)
            return 1

    # --- is the deploy even needed? --------------------------------------
    local = md5(src)
    deployed = remote_etag(args.bucket, key)
    print(f"\nSource    : {src.relative_to(ROOT) if src.is_relative_to(ROOT) else src} "
          f"({src.stat().st_size:,} bytes, md5 {local[:12]}...)")
    print(f"Target    : s3://{args.bucket}/{key}")

    if deployed is None:
        print("Deployed  : (not present -- first deploy)")
    elif "-" in deployed:
        # Multipart upload: the ETag is not a plain md5, so we cannot compare.
        print(f"Deployed  : multipart ETag {deployed} -- cannot compare, uploading.")
        deployed = None
    else:
        print(f"Deployed  : md5 {deployed[:12]}...")

    if deployed == local and not args.force:
        print("\nAlready current -- nothing to upload. (Use --force to re-upload.)")
        print(f"Live at   : {url}")
        return 0

    # --- upload ----------------------------------------------------------
    upload = ["aws", "s3", "cp", str(src), f"s3://{args.bucket}/{key}",
              "--content-type", CONTENT_TYPE, "--cache-control", CACHE_CONTROL]
    if args.dry_run:
        print("\n[dry-run] would run:")
        print("  " + " ".join(upload))
        if not args.no_invalidate:
            print(f"  aws cloudfront create-invalidation --distribution-id "
                  f"{args.distribution} --paths /{args.prefix.strip('/')}/*")
        return 0

    print("\nUploading ...")
    code, _ = run(upload)
    if code != 0:
        print("ERROR: upload failed.", file=sys.stderr)
        return 1

    # Read it back: the deployed ETag must equal the local md5.
    confirmed = remote_etag(args.bucket, key)
    if confirmed != local:
        print(f"ERROR: uploaded, but the deployed ETag ({confirmed}) does not match "
              f"the local md5 ({local}).", file=sys.stderr)
        return 1
    print(f"OK: uploaded and verified (ETag matches local md5).")

    # --- invalidate ------------------------------------------------------
    if args.no_invalidate:
        print(f"\nSkipped the invalidation -- CloudFront may serve the old file for "
              f"up to the cache lifetime.")
    else:
        print("Invalidating CloudFront ...")
        code, out = run(["aws", "cloudfront", "create-invalidation",
                         "--distribution-id", args.distribution,
                         "--paths", f"/{args.prefix.strip('/')}/*",
                         "--output", "json"])
        if code != 0:
            print("ERROR: upload succeeded but the invalidation failed. The new file "
                  "is in S3; re-run to retry the invalidation.", file=sys.stderr)
            return 1
        inv = json.loads(out)["Invalidation"]
        print(f"OK: invalidation {inv['Id']} ({inv['Status']}).")

    commit = git("rev-parse", "--short", "HEAD")
    print(f"\nDeployed{' ' + commit if commit else ''} -> {url}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

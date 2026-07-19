#!/usr/bin/env python3
"""
Inject (or replace) a single course module into the player HTML.

The course player (course/index.html) holds each module as one
    <article class="mod" data-mod="mNN"> ... </article>
inside the hidden <div id="mod-source">, just above the sentinel:
    <!--INJECT-MODULES-HERE-->

This script takes a fragment file that contains exactly one such <article>
and splices it in immediately before the sentinel. If an article with the
same data-mod already exists, it is replaced in place (so re-running is safe).

Usage:
    python tools/inject_module.py m02
    python tools/inject_module.py m02 --fragment build/m02.html
    python tools/inject_module.py m02 --dry-run

Defaults:
    fragment  ->  build/<id>.html
    course    ->  course/index.html
"""
import argparse
import re
import sys
from pathlib import Path

SENTINEL = "<!--INJECT-MODULES-HERE-->"
ROOT = Path(__file__).resolve().parent.parent


def article_pattern(mod_id: str) -> re.Pattern:
    # Match a whole <article ... data-mod="mod_id" ...> ... </article> block.
    return re.compile(
        r'<article\b[^>]*\bdata-mod="' + re.escape(mod_id) + r'"[^>]*>.*?</article>',
        re.DOTALL,
    )


def main() -> int:
    ap = argparse.ArgumentParser(description="Inject a module into the course player.")
    ap.add_argument("mod_id", help='module id, e.g. "m02"')
    ap.add_argument("--fragment", help="fragment HTML file (default: build/<id>.html)")
    ap.add_argument("--course", default=str(ROOT / "course" / "index.html"),
                    help="path to the player HTML")
    ap.add_argument("--dry-run", action="store_true", help="print what would change, write nothing")
    args = ap.parse_args()

    mod_id = args.mod_id.strip()
    frag_path = Path(args.fragment) if args.fragment else ROOT / "build" / f"{mod_id}.html"
    course_path = Path(args.course)

    if not frag_path.exists():
        print(f"ERROR: fragment not found: {frag_path}", file=sys.stderr)
        return 2
    if not course_path.exists():
        print(f"ERROR: player not found: {course_path}", file=sys.stderr)
        return 2

    fragment = frag_path.read_text(encoding="utf-8").strip()

    # The fragment must be exactly one <article> for this module id.
    articles = article_pattern(mod_id).findall(fragment)
    if len(articles) != 1:
        print(f"ERROR: fragment must contain exactly one "
              f'<article ... data-mod="{mod_id}"> ... </article> (found {len(articles)}).',
              file=sys.stderr)
        return 3
    fragment = articles[0]  # ignore any stray whitespace/markup around it

    html = course_path.read_text(encoding="utf-8")
    if html.count(SENTINEL) != 1:
        print(f"ERROR: expected exactly one sentinel {SENTINEL} in the player "
              f"(found {html.count(SENTINEL)}).", file=sys.stderr)
        return 4

    existing = article_pattern(mod_id).search(html)
    if existing:
        new_html = html[:existing.start()] + fragment + html[existing.end():]
        action = "replaced"
    else:
        new_html = html.replace(SENTINEL, fragment + "\n\n" + SENTINEL, 1)
        action = "inserted"

    if args.dry_run:
        print(f"[dry-run] would have {action} {mod_id} "
              f"({len(fragment)} chars) in {course_path}")
        return 0

    course_path.write_text(new_html, encoding="utf-8")
    total = len(article_pattern_any().findall(new_html))
    print(f"OK: {action} {mod_id} in {course_path.name}. "
          f"Player now holds {total} authored module(s).")
    return 0


def article_pattern_any() -> re.Pattern:
    return re.compile(r'<article\b[^>]*\bdata-mod="m\d+"[^>]*>.*?</article>', re.DOTALL)


if __name__ == "__main__":
    raise SystemExit(main())

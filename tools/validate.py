#!/usr/bin/env python3
"""
Validate the course player and (optionally) one module.

Global checks (always run):
  - exactly one insertion sentinel
  - exactly one <script> and one <style>
  - every authored <article data-mod> matches an id declared in the MODS array
  - <article> open/close tags balance inside #mod-source
  - reports which planned modules are built vs still on the roadmap

Per-module checks (when a module id is passed):
  - the module's <article> appears exactly once
  - Java generics inside <code> look HTML-escaped (heuristic warning)
  - any source paths it references (com/portal/priorauth/...) exist on disk

Usage:
    python tools/validate.py            # whole player
    python tools/validate.py m08        # player + module m08
"""
import re
import sys
from pathlib import Path

SENTINEL = "<!--INJECT-MODULES-HERE-->"
ROOT = Path(__file__).resolve().parent.parent
PLAYER = ROOT / "course" / "index.html"
SERVICE = ROOT / "labs" / "priorauth-service"

problems, warnings = [], []


def err(m): problems.append(m)
def warn(m): warnings.append(m)


def mods_ids(html: str):
    m = re.search(r"const MODS\s*=\s*\[(.*?)\];", html, re.DOTALL)
    if not m:
        err("Could not find the MODS array.")
        return []
    return re.findall(r"id:'(m\d+)'", m.group(1))


def built_ids(html: str):
    return re.findall(r'data-mod="(m\d+)"', html)


def global_checks(html: str):
    if html.count(SENTINEL) != 1:
        err(f"Expected exactly one sentinel {SENTINEL}; found {html.count(SENTINEL)}.")
    for tag, n in (("<script>", html.count("<script>")),
                   ("</script>", html.count("</script>")),
                   ("<style>", html.count("<style>")),
                   ("</style>", html.count("</style>"))):
        if n != 1:
            err(f"Expected exactly one {tag}; found {n}.")

    declared = mods_ids(html)
    built = built_ids(html)
    for b in built:
        if b not in declared:
            err(f'Authored module "{b}" is not declared in MODS.')

    src = re.search(r'<div id="mod-source".*?>(.*)</div>\s*<script>', html, re.DOTALL)
    region = src.group(1) if src else html
    opens = len(re.findall(r"<article\b", region))
    closes = region.count("</article>")
    if opens != closes:
        err(f"Unbalanced <article> tags in #mod-source: {opens} open, {closes} close.")

    built_set = set(built)
    done = [i for i in declared if i in built_set]
    todo = [i for i in declared if i not in built_set]
    print(f"MODS declared : {len(declared)}")
    print(f"Authored      : {len(done)}  ({', '.join(done) or '—'})")
    print(f"On roadmap    : {len(todo)}  ({', '.join(todo) or '—'})")


def module_checks(html: str, mod_id: str):
    blocks = re.findall(
        r'<article\b[^>]*\bdata-mod="' + re.escape(mod_id) + r'"[^>]*>.*?</article>',
        html, re.DOTALL)
    if len(blocks) != 1:
        err(f'Module "{mod_id}": expected exactly one <article>, found {len(blocks)}.')
        return
    block = blocks[0]

    # Heuristic: Java generics should be escaped inside code samples.
    for code in re.findall(r"<code>(.*?)</code>", block, re.DOTALL):
        if re.search(r"<[A-Z][A-Za-z0-9]*>", code):
            warn(f'Module "{mod_id}": a <code> block may contain an UNescaped Java '
                 f'generic (e.g. write List&lt;Foo&gt; not List<Foo>).')
            break

    # Any referenced source paths should exist.
    for rel in re.findall(r"(com/portal/priorauth/[A-Za-z0-9_/]+\.java)", block):
        p = SERVICE / "src" / "main" / "java" / rel
        if not p.exists():
            err(f'Module "{mod_id}" references missing source file: {rel}')

    # Balanced tabs, if it's a dual-path lab.
    if 'class="paths"' in block:
        tabs = block.count('data-tab=')
        panels = block.count('data-panel=')
        if tabs < 2 or panels < 2:
            warn(f'Module "{mod_id}": a dual-path lab usually has 2 tabs and 2 panels '
                 f'(found {tabs} tab / {panels} panel).')

    print(f'Module "{mod_id}": article found, {len(block)} chars.')


def main() -> int:
    if not PLAYER.exists():
        print(f"ERROR: player not found at {PLAYER}", file=sys.stderr)
        return 2
    html = PLAYER.read_text(encoding="utf-8")

    global_checks(html)
    if len(sys.argv) > 1:
        module_checks(html, sys.argv[1].strip())

    print()
    for w in warnings:
        print("WARN:", w)
    for p in problems:
        print("FAIL:", p)
    if problems:
        print(f"\n{len(problems)} problem(s), {len(warnings)} warning(s).")
        return 1
    print(f"PASS — 0 problems, {len(warnings)} warning(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

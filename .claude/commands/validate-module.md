---
description: Validate a built module (structure + content review)
argument-hint: [module number or id, e.g. 8 or m08]
allowed-tools: Read, Grep, Glob, Bash(python*)
---

Validate one module. The id is `m` + the two-digit module number ($ARGUMENTS → e.g. `m08`).

## 1. Automated check
Run the validator and report its output verbatim:

    python tools/validate.py <id>

It confirms: exactly one insertion sentinel, one `<script>`/`<style>`, the module's
`<article>` appears exactly once, referenced `com/portal/priorauth/...` files exist,
Java generics inside `<code>` look escaped, and dual-path labs have their tabs/panels.

## 2. Content review (read the module and judge it)
Read the `<article data-mod="<id>">` block in `course/index.html` and check:

- **Beginner-friendly** — no undefined jargon; short, concrete sentences.
- **Real** — every file, class, endpoint, and command matches `labs/priorauth-service`.
  Open the referenced files and confirm names and signatures are correct.
- **Component discipline** — only the documented classes are used; no inline `<style>`,
  no new CSS, no `localStorage`/`sessionStorage`.
- **Labs only** — scenario, numbered acceptance criteria, a working dual-path block with a
  real prompt in each panel, expected output, review checklist, and verify-it commands.
- **Accessibility** — headings are in order; any animation still reads with reduced motion.

## 3. Report
List any FAIL/WARN from the tool, plus your content findings, each with the fix. If everything
is clean, say so and confirm `PROGRESS.md` marks the module built. Remind me to `/clear`
before the next module.

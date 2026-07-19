---
description: Build one course module and inject it into the player
argument-hint: [module number or id, e.g. 5 or m05]
allowed-tools: Read, Grep, Glob, Write, Bash(python*)
---

Build **one** module of the course as an HTML fragment, then inject and validate it.
For lab modules, prefer `/build-lab` instead — it enforces the dual-path structure.

The id is `m` + the two-digit module number ($ARGUMENTS → e.g. `m05`).

## 1. Read before writing
- `build/<id>.plan.md` (run `/plan-module $ARGUMENTS` first if it's missing).
- `CLAUDE.md` — the **Authoring conventions** and **Component kit** sections.
- The reference module `m01` in `course/index.html` — copy its structure and class usage exactly.
- Any `labs/priorauth-service` source the module references, so paths and code are real.

## 2. Write `build/<id>.html`
Output exactly one block:

```html
<article class="mod" data-mod="<id>">
  <p class="lede"> ... </p>
  ...
</article>
```

Rules:
- Use only the component classes documented in `CLAUDE.md` (`.lede`, `.callout--note/key/warn/try`,
  `.snippet` + `pre.code`, `.figure`, the animation blocks, etc.). Don't add new CSS — the
  stylesheet is fixed.
- **Beginner-friendly:** short sentences, concrete examples, define jargon on first use.
- **Escape Java generics** inside `<code>`: write `List&lt;AuthResponse&gt;`, never `List<AuthResponse>`.
- Tie every technical claim to a real file/class/endpoint in the service.
- End with a short "before the next module" callout (`.callout--try`) when it helps.

## 3. Inject, validate, record
Run these and fix anything they flag:

    python tools/inject_module.py <id>
    python tools/validate.py <id>

Then update `PROGRESS.md`: mark this module **built** with today's date and a one-line note.

## 4. Finish
Tell me to open `course/index.html`, click to this module, and check it renders — then
`/clear` before starting the next module (one module per session).

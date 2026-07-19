---
description: Plan one course module before building it
argument-hint: [module number or id, e.g. 8 or m08]
allowed-tools: Read, Grep, Glob, Write
---

You are planning **one** module of the AI-Assisted Development course. Do not write the
module HTML in this step — only produce a plan.

## Inputs to read first
- `CLAUDE.md` at the repo root — the course concept, the AI-DLC methodology facts, the player
  architecture, the component classes, and the full module plan.
- The `MODS` array in `course/index.html` — find the entry whose number/id matches
  `$ARGUMENTS`. The id is `m` + the two-digit number (module 8 → `m08`).
- The reference module `m01` inside `course/index.html` — match its voice and structure.
- If the module touches code, read the relevant files under
  `labs/priorauth-service/src/` so every claim and path is real.

## Produce a plan and write it to `build/<id>.plan.md`

Cover, briefly:
1. **Objective** — what the learner can do after this module (one or two sentences).
2. **Audience check** — this is beginner-friendly; note anything that needs plain-language framing.
3. **Outline** — the section headings in order (aim for 3–6 sections).
4. **Code touchpoints** — exact files/classes/endpoints in `labs/priorauth-service` the module
   references. If none, say so.
5. **Kind** — `concept`, `hands-on`, or `lab`. If it's a **lab**, state the intent, sketch the Mob Elaboration beat (2–3 clarifying questions + answers), list the
   numbered acceptance criteria, and confirm it must be **dual-path** (Claude Code + GitHub Copilot).
6. **Animation** — does this module reuse one of the built animation blocks
   (`.lanes` hero, `.loop` context loop, `.pipe` request flow)? If yes, which, and what it shows.
   Most modules need none — don't invent one.
7. **The one thing to get right** — the single idea this module must land.

Keep the plan to about one page. End by telling me to run `/build-module $ARGUMENTS`
(or `/build-lab $ARGUMENTS` if it's a lab).

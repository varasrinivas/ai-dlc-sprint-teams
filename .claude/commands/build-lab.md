---
description: Build a dual-path (Claude Code + Copilot) lab module
argument-hint: [module number or id, e.g. 8 or m08]
allowed-tools: Read, Grep, Glob, Write, Bash(python*)
---

Build **one bolt lab**. In this course a lab is a bolt: the learner states an intent, the AI
elaborates and constructs, and the learner validates at checkpoints — done **twice**, once with
Claude Code and once with GitHub Copilot, on the running `labs/priorauth-service`.

The id is `m` + the two-digit module number ($ARGUMENTS → e.g. `m08`).

## 1. Read first
- `build/<id>.plan.md` (intent + acceptance criteria).
- `CLAUDE.md` (AI-DLC facts, Component kit, Lab structure).
- The reference modules `m01` (methodology voice) and `m20` (lab shape) in `course/index.html`.
- The exact service files this bolt changes, so prompts and expected output are real.

## 2. Required structure of `build/<id>.html`
Produce one `<article class="mod" data-mod="<id>">` containing, in order:

1. `<p class="lede">` — one-paragraph framing of the bolt.
2. **Intent** — a `.scenario` callout labeled `Intent`, written as the business ask
   ("As a provider, when my request is denied, I can file one appeal…").
3. **Elaboration (Mob Elaboration beat)** — show the AI turning the intent into a plan **and
   clarifying questions**, and the team's answers. At minimum: a real elaboration prompt, two or
   three plausible clarifying questions the AI would ask, and the decided answers. This is where
   AI-DLC differs from prompt-driven work — never skip it.
4. **Validated acceptance criteria** — an `<ol class="criteria">` the team signs off before
   construction starts.
5. **Dual-path construction** — a `.paths` component with two tabs and two panels:

   ```html
   <div class="paths">
     <div class="paths__tabs">
       <button class="tab is-active" data-tab="cc">Claude Code</button>
       <button class="tab t-cop" data-tab="cop">GitHub Copilot</button>
     </div>
     <div class="panel is-active" data-panel="cc"> ...Claude Code steps + a real prompt... </div>
     <div class="panel" data-panel="cop"> ...Copilot steps + where ghost text / chat helps... </div>
   </div>
   ```
   Each panel gives concrete steps and at least one **real, copy-pasteable prompt**.

6. **Expected output** — an `.expected` callout showing a representative result, framed as
   "your assistant will produce something like this; yours may differ." Escape Java generics.
7. **Validation checklist** — a `<ul class="checklist">` of what the team validates at the checkpoint
   (does it enforce the business rule? does it use `applyDecision(...)`? is there a test?).
8. **Verify it** — a `.verify` callout with the exact commands to prove it works
   (`mvn spring-boot:run`, a `curl`, the expected status code).

The teaching point of every bolt: **the team stated intent, the AI elaborated and constructed,
and humans validated at every checkpoint.** Make that loop explicit.

## 3. Inject, validate, record
    python tools/inject_module.py <id>
    python tools/validate.py <id>

Fix anything flagged (the validator warns if the dual-path tabs/panels are missing or if a
referenced source file doesn't exist). Update `PROGRESS.md`.

## 4. Finish
Tell me to open the player, run the lab both ways against the service, then `/clear`.

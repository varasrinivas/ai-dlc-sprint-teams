# CLAUDE.md — AI-Assisted Development course (Prior Auth Portal)

Read automatically by Claude Code in this repo. This is the authoring context for building
the course **one module per session**. The companions `labs/priorauth-service/CLAUDE.md` and
`labs/priorauth-web/CLAUDE.md` are the context for the applications the course teaches on.

## What this repo is

Three things:

1. **`course/`** — a self-contained HTML course *player* (`course/index.html`) that teaches a
   sprint team to migrate from traditional coding to **AI-assisted development** with
   **Claude Code** and **GitHub Copilot**.
2. **`labs/priorauth-service/`** — the runnable Spring Boot application the course uses as its
   shared codebase for every hands-on lab.
3. **`labs/priorauth-web/`** — the React provider portal (Vite + React) that calls the service's
   API; the shared codebase for the "provider portal (React)" track (m28–m31). Ships with the
   request list built and intentional gaps (submit form, appeal flow, thin tests) that its labs fill.

The course is authored *with* Claude Code, using the slash commands in `.claude/commands/`.

## The course, in one paragraph

Audience: working developers on a sprint team, **beginners to AI-DLC**. The course migrates the
team from traditional sprints to **AI-DLC — the AI-Driven Development Lifecycle** (AWS, 2025):
AI drives planning and building, humans supervise and validate at checkpoints. Running frame:
**AI proposes, humans approve**. The team practises real work as **bolts** (feature, tests, bug,
refactor) on one small service. Every lab is **dual-path**: the same bolt run once with Claude Code
and once with GitHub Copilot, because AI-DLC is tool-agnostic.

Domain anchor: the **Prior Auth Portal**, with `AUTO_APPROVE_THRESHOLD = 0.85`.

**Organizational driver (keep this lens in every module):** leadership's major factor is
**measurable productivity improvement from AI tools**. Content should connect practices to
measurable outcomes — baselines, the metric set (time-to-market, cost incl. validation attention,
escape rate, coverage), honest evidence over vendor claims. Module m21 and
`docs/leadership-brief.md` carry this directly; other modules shouldn't contradict it.

## AI-DLC facts (keep modules consistent with these)

- Origin: AWS, introduced mid-2025; workflow rules open-sourced as `awslabs/aidlc-workflows`.
  Tool-agnostic — AWS names Amazon Q Developer, Kiro, and Claude Code as engines.
- Three phases: **Inception → Construction → Operations**; the same loop runs inside each:
  AI proposes → humans validate → AI executes → humans review.
- Vocabulary: **bolt** replaces the sprint (a cycle of hours–days); **Unit of Work** replaces the
  epic; **Mob Elaboration** (Inception: AI turns intent into requirements + clarifying questions,
  the whole team answers together); **Mob Construction** (Construction: AI proposes
  architecture/design/code, the team resolves decisions in real time); **persistent context**
  (decisions and conventions live in the repository — CLAUDE.md, skills, agents are this course's
  concrete form of it).
- Honest framing to preserve: vendor-reported gains (10–15x on AWS-run engagements vs ~10–15%
  from unstructured assistant adoption) are benchmarks, not guarantees; bolts are calendar-fast but
  hungry for senior validation attention; every artifact passes a human checkpoint.

## Player architecture (fixed — don't redesign it)

- **One file:** `course/index.html`. Self-contained: fonts via Google Fonts, all CSS in one
  `<style>`, all JS in one `<script>`.
- **`MODS` array** (in the `<script>`) is the single source of truth for structure and order.
  Each entry: `{id, track, num, kind, mins, title}`; roadmap entries also carry `roadmap:true`
  and a `summary`. `kind` is `concept` | `lab` | `hands`.
- **Content registry:** each module is one `<article class="mod" data-mod="mNN"> … </article>`
  inside `<div id="mod-source" hidden>`, just above the sentinel `<!--INJECT-MODULES-HERE-->`.
  A module with no article renders a "roadmap / not built yet" placeholder automatically.
- **Never hand-edit the registry.** Author a fragment in `build/<id>.html` and run
  `python tools/inject_module.py <id>` (idempotent: re-running replaces that module in place).
- **No `localStorage` gymnastics, no new CSS per module, no inline `<style>`.** The stylesheet
  is complete; modules use existing classes only.

### Palette & type (already in the stylesheet)
Warm-paper family, in **both light and dark**: every colour is a CSS variable on `:root`, with
dark overrides on `:root[data-theme="dark"]` (warm charcoal; `--teal`/`--amber` lanes preserved).
The topbar ◐ button toggles the theme (persisted in its own localStorage key, OS preference as
the default) — never hardcode a colour in a module; use the kit classes so both themes work.
Two-lane colour story encodes the course's theme:
`--teal` = the **AI-assisted** lane / approved; `--amber` = the **traditional** lane / caution.
Display font Space Grotesk, body Newsreader, mono JetBrains Mono. Reduced motion is respected.

## Component kit (use these classes — nothing else)

- `<p class="lede">` — opening paragraph. `<b>` inside it renders teal.
- Callouts: `<div class="callout callout--note|key|warn|try"><div class="callout__label">…</div><p>…</p></div>`
  (key = teal, warn = rose, try = amber, note = neutral).
- Inline emphasis pills: `<span class="pill-ai">Claude Code</span>`, `<span class="pill-trad">Copilot</span>`.
- Code: `<div class="snippet"><div class="snippet__cap">CAPTION</div><pre class="code"><code>…</code></pre></div>`.
  Terminal variant: `<pre class="code code--term">` — wrap prompt markers in `<span class="p">$</span>`
  and comments in `<span class="c">…</span>`. **Escape Java generics**: `List&lt;Foo&gt;`.
- Figures / diagrams: `<figure class="figure"> … <figcaption class="figure__cap">…</figcaption></figure>`.
- Keys: `<span class="kbd">Tab</span>`.

### Lab-only components
- `<div class="scenario"><div class="callout__label">Intent</div><p>…</p></div>` — the bolt's
  intent statement (every built lab uses the bare `scenario` class and the label "Intent").
- `<ol class="criteria"> … </ol>` — numbered acceptance criteria. (Established exception:
  concept modules also use it for numbered step sequences, e.g. m22's retrofit steps.)
- Dual-path block (tab switching is wired in the player JS):
  ```html
  <div class="paths">
    <div class="paths__tabs">
      <button class="tab is-active" data-tab="cc">Claude Code</button>
      <button class="tab t-cop" data-tab="cop">GitHub Copilot</button>
    </div>
    <div class="panel is-active" data-panel="cc"> … </div>
    <div class="panel" data-panel="cop"> … </div>
  </div>
  ```
- `<div class="expected"><div class="callout__label">Expected output</div> … </div>`
- `<ul class="checklist"> … </ul>` — reviewer checklist.
- `<div class="verify"><div class="callout__label">Verify it</div> … </div>`
  (`scenario` / `expected` / `verify` are styled standalone — do not add the `callout` class.)

### Animation blocks (CSS already present; reuse the markup)
- **Two-lane hero** (`.lanes` … `.mover--slow` / `.mover--fast`) — see module `m01`. Traditional vs
  AI-assisted flow.
- **Context loop** (`.loop`, `.loop__orbit`, `.loop__node`) — intended for `m02` (intent →
  context → predict → review cycle).
- **Request flow** (`.pipe`, `.pipe__stage`, `.gate`, `.branch`) — intended for `m05` (Controller →
  Service → rules-engine gate → Repository, branching to APPROVED / PENDING_REVIEW at 0.85).

Most modules need **no** animation. Don't add one just to decorate.

## Authoring workflow (one module per session)

1. `/plan-module <n>` → writes `build/<id>.plan.md`.
2. `/build-module <n>` (or `/build-lab <n>` for labs) → writes `build/<id>.html`, injects it,
   validates it, updates `PROGRESS.md`.
3. `/validate-module <n>` → automated + content review.
4. Open `course/index.html`, click to the module, confirm it renders.
5. `/clear` before the next module.

Keep sessions to one module so context stays small and focused.

## Module plan (32 modules, 9 tracks)

**The AI-DLC shift**
- m01 · concept · From sprints to bolts: the AI-DLC shift   *(built — reference module)*
- m02 · concept · How your AI collaborator thinks
- m03 · concept · One methodology, many tools: Claude Code vs GitHub Copilot
- m04 · hands-on · Setup day: install both, run your first prompt

**The Prior Auth Portal**
- m05 · concept · Tour of the Prior Auth Portal
- m06 · lab · Bolt 0 — Read the codebase with AI
- m07 · concept · Persistent context: CLAUDE.md & Copilot instructions

**Everyday developer craft**
- m08 · hands-on · In the flow: autocomplete, inline chat & the CLI   *(built)*
- m09 · lab · Finding and raising defects with AI   *(built — raises the ticket m12 fixes)*

**Construction bolts**
- m10 · lab · Bolt — The Appeals endpoint, from intent to code
- m11 · lab · Bolt — Lock the rules engine with tests
- m12 · lab · Bolt — Fix a bug (the units boundary)
- m13 · lab · Bolt — Refactor the rules engine into composable rules
- m14 · concept · Validation checkpoints: reviewing AI output

**Running AI-DLC as a team**
- m15 · concept · Mob Elaboration: intent into units of work
- m16 · concept · Guardrails: security, PHI, and when NOT to use AI
- m17 · concept · Planning in bolts: estimation & Definition of Done
- m18 · concept · Rolling out AI-DLC: a team adoption playbook


**Leading the transformation**  *(the leadership track — built for the leadership-productivity driver)*
- m19 · concept · The scoreboard: DORA, SPACE & the AI Capabilities Model   *(built)*
- m20 · concept · Engineering the metrics: how bolts move DORA & SPACE   *(built)*
- m21 · concept · Proving it: productivity evidence for leadership   *(built — DORA 2025 + METR RCT grounded)*

**AI engineering & automation**  *(this track is the concrete form of AI-DLC's "persistent context")*
- m22 · concept · Turn a non-AI repo into an AI-ready repo   *(built)*
- m23 · concept · Package repeatable work as Claude Skills   *(built)*
- m24 · concept · Specialized subagents for your codebase   *(built)*
- m25 · lab · Build a code-review agent   *(built)*
- m26 · lab · Automated PR review & CI with Claude Code   *(built)*
- m27 · concept · MCP, hooks & the rest of the toolbox   *(built)*

**The provider portal (React)**  *(realizes the React roadmap item; app at `labs/priorauth-web/`)*
- m28 · concept · Tour of the provider portal: React meets the Prior Auth API   *(built)*
- m29 · lab · Bolt — The submit form, from intent to UI   *(built)*
- m30 · lab · Bolt — File an appeal from the portal   *(built — needs the m10 appeals endpoint)*
- m31 · lab · Bolt — Lock the portal with component tests   *(built)*

**What's next**
- m32 · concept · Extend the Portal: a second service & beyond   *(built)*

The "AI engineering & automation" track (m22–m27) teaches the real, already-shipped setup in
`labs/priorauth-service` — its `.claude/agents/` (code-reviewer, security-reviewer),
`.claude/skills/prior-auth-rules/`, and `.github/workflows/` (claude-code-review.yml,
claude.yml). Bolt labs (m06, m09, m10–m13, m29–m31) must follow the AI-DLC loop explicitly: intent →
AI elaboration with clarifying questions (Mob Elaboration beat) → validated acceptance
criteria → supervised construction → validation checkpoint. Keep every lab dual-path
(Claude Code vs the GitHub Copilot equivalent). Verify Claude Code facts against the docs,
since these features move fast: subagents live in `.claude/agents/*.md` (frontmatter: name,
description, tools, model; loaded at session start); Skills live in
`.claude/skills/<name>/SKILL.md` (folder name = skill name; model-invoked via the description);
PR review is either the managed path (`claude /install-github-app`, then `@claude review`) or the
`anthropics/claude-code-action@v1` GitHub Action. Note the current convergence: a slash command
and a Skill both create a `/name` command — commands are "skills-lite."

## Metrics facts (leadership track — keep consistent)

- DORA four keys: deployment frequency, lead time for changes, change failure rate, failed
  deployment recovery time — always reported as speed+stability pairs.
- SPACE (Forsgren/Storey et al.): Satisfaction, Performance, Activity, Communication, Efficiency/flow;
  measure ≥3 dimensions mixing system + survey data; Activity is never a target (Goodhart).
- DORA AI Capabilities Model (2025 companion): seven capabilities — clear/communicated AI stance,
  healthy data ecosystems, AI-accessible internal data, strong version control practices, working in
  small batches, user-centric focus, quality internal platforms; VSM as force multiplier; "AI is an
  amplifier" thesis. Course mapping: stance→guardrails, internal data→persistent context,
  small batches→bolts.
- Rollout expectation: J-curve announced in advance; thresholds pre-agreed; target levers not metrics.

## Content conventions

- Beginner-friendly: short sentences, concrete examples, define jargon on first use.
- Every technical claim maps to a real file/class/endpoint/command in `labs/priorauth-service`.
- Labs teach the AI-DLC loop: **state intent; AI elaborates (clarifying questions) and proposes;
  humans validate; AI constructs; humans review at the checkpoint.** Always include a
  "trust nothing you didn't validate" moment.
- Claude Code facts stay accurate: installed via `npm install -g @anthropic-ai/claude-code`,
  launched with `claude` in the repo; custom commands live in `.claude/commands/`; `CLAUDE.md`
  gives project context; `/clear` resets context. Copilot: VS Code extension + Copilot Chat,
  repo-wide `.github/copilot-instructions.md`, ghost-text you accept with Tab.

## Roadmap — building on this course later

Keep the architecture ready for these; they slot in as new tracks/modules without redesign:

- **A second microservice** — split the rules engine or an eligibility service out of the monolith
  to teach AI-assisted work across service boundaries. Module m32 tees this up as the next unit
  of work.

(CI & PR automation is no longer roadmap — it's the "AI engineering & automation" track, m22–m27.
The React provider portal is no longer roadmap either — it's the "provider portal (React)" track,
m28–m31, built on the real app at `labs/priorauth-web/`.)

When adding a track: extend the `MODS` array (new ids continue the number sequence), reuse the
existing component kit, and add any new app under `labs/`. The player and tooling need no changes.

# PROGRESS — AI-DLC for Sprint Teams

Build **one module per session**. After each build: `/validate-module <n>`, confirm it renders,
update the row below, then `/clear`.

Status: ✅ built · 🔨 in progress · ⬜ not started

| #   | Track                        | Kind     | Module                                              | Status | Notes                            |
|-----|------------------------------|----------|-----------------------------------------------------|--------|----------------------------------|
| m01 | The AI-DLC shift             | concept  | From sprints to bolts: the AI-DLC shift             | ✅     | Reference module + bolt anim.    |
| m02 | The AI-DLC shift             | concept  | How your AI collaborator thinks                     | ✅     | Reuse `.loop` animation.         |
| m03 | The AI-DLC shift             | concept  | One methodology, many tools: CC vs Copilot          | ✅     | AI-DLC is tool-agnostic.         |
| m04 | The AI-DLC shift             | hands-on | Setup day: install both, run your first prompt      | ✅     | Verify install steps vs docs.    |
| m05 | The Prior Auth Portal        | concept  | Tour of the Prior Auth Portal                       | ✅     | Reuse `.pipe` flow animation.    |
| m06 | The Prior Auth Portal        | lab      | Bolt 0 — Read the codebase with AI                  | ✅     | Dual-path micro-bolt.            |
| m07 | The Prior Auth Portal        | concept  | Persistent context: CLAUDE.md & Copilot instr.      | ✅     | AI-DLC persistent context.       |
| m08 | Everyday developer craft     | hands-on | In the flow: autocomplete, inline chat & the CLI    | ✅     | Verified current tool features.  |
| m09 | Everyday developer craft     | lab      | Finding and raising defects with AI                 | ✅     | Raises the ticket m12 fixes.     |
| m10 | Construction bolts           | lab      | Bolt — The Appeals endpoint, from intent to code    | ✅     | Full loop incl. Mob Elaboration. |
| m11 | Construction bolts           | lab      | Bolt — Lock the rules engine with tests             | ✅     | 0.85 boundary case.              |
| m12 | Construction bolts           | lab      | Bolt — Fix a bug (the units boundary)               | ✅     | Red-first.                       |
| m13 | Construction bolts           | lab      | Bolt — Refactor the rules engine into rules objects | ✅     | Mob Construction style.          |
| m14 | Construction bolts           | concept  | Validation checkpoints: reviewing AI output         | ✅     |                                  |
| m15 | Running AI-DLC as a team     | concept  | Mob Elaboration: intent into units of work          | ✅     |                                  |
| m16 | Running AI-DLC as a team     | concept  | Guardrails: security, PHI, and when NOT to use AI   | ✅     |                                  |
| m17 | Running AI-DLC as a team     | concept  | Planning in bolts: estimation & Definition of Done  | ✅     |                                  |
| m18 | Running AI-DLC as a team     | concept  | Rolling out AI-DLC: a team adoption playbook        | ✅     |                                  |
| m19 | Leading the transformation   | concept  | The scoreboard: DORA, SPACE & AI Capabilities Model | ✅     | The three frameworks + mapping.  |
| m20 | Leading the transformation   | concept  | Engineering the metrics: bolts → DORA & SPACE       | ✅     | Playbook + Prior Auth instrumenting. |
| m21 | Leading the transformation   | concept  | Proving it: productivity evidence for leadership    | ✅     | Leadership brief template in docs/. |
| m22 | AI engineering & automation  | concept  | Turn a non-AI repo into an AI-ready repo            | ✅     | Persistent-context track ref.    |
| m23 | AI engineering & automation  | concept  | Package repeatable work as Claude Skills            | ✅     | Uses the shipped example Skill.  |
| m24 | AI engineering & automation  | concept  | Specialized subagents for your codebase             | ✅     | Uses `.claude/agents/`.          |
| m25 | AI engineering & automation  | lab      | Build a code-review agent                           | ✅     | Dual-path vs Copilot review.     |
| m26 | AI engineering & automation  | lab      | Automated PR review & CI with Claude Code           | ✅     | Uses the shipped workflows.      |
| m27 | AI engineering & automation  | concept  | MCP, hooks & the rest of the toolbox                | ✅     |                                  |
| m28 | The provider portal (React)  | concept  | Tour of the provider portal: React meets the API    | ✅     | labs/priorauth-web tour.         |
| m29 | The provider portal (React)  | lab      | Bolt — The submit form, from intent to UI           | ✅     | POST + inline result card.       |
| m30 | The provider portal (React)  | lab      | Bolt — File an appeal from the portal               | ✅     | Cross-stack; needs m10 endpoint. |
| m31 | The provider portal (React)  | lab      | Bolt — Lock the portal with component tests         | ✅     | Vitest/RTL; mock the API client. |
| m32 | What's next                  | concept  | Extend the Portal: a second service & beyond        | ✅     | React moved from roadmap to m28–m31. |

## Working AI artifacts already in the repo (persistent context + automation)

- `labs/priorauth-service/.claude/agents/code-reviewer.md` — code-review subagent
- `labs/priorauth-service/.claude/agents/security-reviewer.md` — security/PHI subagent
- `labs/priorauth-service/.claude/skills/prior-auth-rules/SKILL.md` — example Skill
- `labs/priorauth-service/.github/workflows/claude-code-review.yml` — auto PR review
- `labs/priorauth-service/.github/workflows/claude.yml` — on-demand `@claude`
- `labs/priorauth-web/CLAUDE.md` + `labs/priorauth-web/.github/copilot-instructions.md` — the web repo born AI-ready (m28)

## Session log

- 2026-07-18 · added a dark/light theme toggle to the player (topbar ◐ button; palette fully
  variable-driven with `:root[data-theme="dark"]` overrides; OS-pref default, persisted choice,
  WCAG-checked dark palette)
- 2026-07-18 · built the React provider portal track: new app `labs/priorauth-web/` (Vite + React,
  request list shipped; submit form / appeal flow / test suite left as intentional lab gaps) +
  modules m28–m31; "What's next" renumbered m28 → m32 and rewritten (React off the roadmap,
  second service is the road ahead); course is now 32 modules / 9 tracks
- 2026-07-17 · authored the full AI engineering & automation track (m23–m27) into the player
- 2026-07-17 · converted the course from prompt-driven framing to **AI-DLC** (AWS AI-Driven
  Development Lifecycle): rebranded player, rewrote m01 (sprints → bolts), renamed tracks,
  updated authoring commands so labs follow the intent → elaboration → validation loop
- 2026-07-18 · authored all remaining modules (m02–m18, m28) — the course is now complete: 23/23 built
- 2026-07-18 · added m21 (productivity evidence for leadership) + docs/leadership-brief.md; renumbered m22–m28; leadership productivity lens added to CLAUDE.md
- 2026-07-18 · added Everyday developer craft track (m08 daily toolkit, m09 defect raising); renumbered m10–m28; added independent-research section (DORA 2025, METR RCT) to m21
- 2026-07-18 · created the Leading the transformation track (m19 scoreboard, m20 engineering the metrics, m21 evidence moved in); renumbered m22–m28
- 2026-07-20 · resynced `build/` fragments from the player: restored the four missing fragments
  (m24–m27) and refreshed 13 stale ones (m05, m10–m18, m21–m23) that still held pre-renumbering
  content — `course/index.html` is the source of truth; `build/` is gitignored working files
- 2026-07-20 · full validation pass (automated 32/32 PASS + six-track content review): applied all
  WARN fixes — m04 Java/Maven prereq, m06 elaboration note + runnable verify curl, m09 Copilot
  triage prompts + runnable verify + policy UM-401 planted in the service README, m16 PHI expanded,
  m19 "a decade of DORA", m22 file count, m24 tools bullet + stray `</span>`, m25 read-only wording
  + Copilot review prompt, m29 list-refresh mechanism named; CLAUDE.md kit section updated to match
  built lab markup (bare `scenario`/`expected`/`verify`, "Intent" label)
- 2026-07-20 · applied the validation pass's nit fixes across 16 modules (jargon glosses, m01
  10–15x figure, m11/m12 criteria alignment, m13 framework wording, m14 checkpoint-two list,
  m21 METR follow-up corrected against METR's Feb-2026 update, m25/m26 elaboration + trust
  beats, m28 tree ellipsis, m30 409 comment, m31 exact error string; verified
  claude-sonnet-4-6 in m26's workflow is a live model id)
- 2026-07-20 · second full validation pass (automated 32/32 PASS + 7-track parallel content
  review): fixed both WARNs — m07 "Next" pointer corrected (m08/m09 come before the first
  construction bolt), m26 Copilot panel given a concrete settings-path snippet + the
  copilot-instructions.md repo-awareness note — plus nits across m09 (elaboration-collapse
  sentence), m16 (NPI gloss, authn/authz expanded, phrasing), m20 (CFR + bus-factor glosses),
  m26 ("Fix with Copilot" softened), m27 (shaped `claude mcp add`), m28 (RequestList "fetch"
  wording), m29 (impossible 0.72 → 0.70, terminal comments), m30 (npm test cwd comment);
  left as intentional: m01 `.stops` inline positioning, prose-guided Copilot panels in m06/m10–m13
- 2026-07-23 · student-perspective validation pass (browser walkthrough + labs actually attempted
  on a Maven-less machine + 5-track content review): shipped the **Maven Wrapper** in
  `labs/priorauth-service` (`mvnw`/`mvnw.cmd` + `.mvn/wrapper/`, verified `./mvnw test` green
  with no Maven installed) and switched every `mvn` command to `./mvnw` across 12 modules +
  service README/CLAUDE.md + web CLAUDE.md; m04 gained clone-the-repo + no-Maven-needed +
  Git-Bash-on-Windows "Before you start"; m26 gained a "Before you start" warn callout (push the
  service as its own GitHub repo — Actions won't run subfolder workflows — admin rights, Claude
  credential, criteria 2–3 Claude-only); player gained a `hashchange` listener (deep links now
  work in an already-open tab); plus fixes: m06 PowerShell/curl note + `approvalScore` field
  named, m09 failed-repro-is-a-clue note + same-branch note, m10 `decidedAt` elaboration ruling,
  m12 docs-catch-up checklist item, m13 AC5 marked the sanctioned tripwire exception, m14 "four
  construction bolts", m16/m17/m18 forward pointers to Modules 22–27, m20 PR-pickup-time defined,
  m24 verbatim frontmatter quote + honest Bash-can-edit wording, m25 annotated mixed terminal
  block, m28 Vite/RTL glosses, m30 restart-the-service verify note, m31 prerequisite callout
  (m29+m30), m05 full `src/main/java/` paths
- 2026-07-25 · student-perspective validation pass (ran the course rather than reading it): `./mvnw
  test` green, service booted and all lab verify curls behaved as documented (m05 seed 0.90/0.70/0.75,
  m06 MRI → PENDING_REVIEW at 0.70, m09 10-unit → APPROVED at 0.90, m10 deny id 2 → DENIED and
  `/appeal` → 404), `npm test` green in priorauth-web, and a browser walkthrough of all 32 modules
  (tabs switch, progress counts, no roadmap placeholders, no tab/panel mismatches). One fix applied:
  bumped the pinned review model from `claude-sonnet-4-6` to `claude-sonnet-5` in both workflows and
  m26's "Model & cost" bullet — the old id is still live, but it is a generation behind and students
  copy that line straight into their own CI
- 2026-07-25 · m10 · ran the appeals bolt for real to prove the lab is completable (all 5 acceptance
  criteria verified: DENIED → PENDING_REVIEW with `appealedAt` set and `decidedAt` kept, 409 on both
  conflict paths, 400 on a blank reason, layering intact, suite green at 5 tests) — then reverted the
  implementation so the intentional gap survives. Construction surfaced a state-machine subtlety the
  elaboration had missed: appealing twice *in a row* trips the status guard (the request is already
  PENDING_REVIEW), so the `appealedAt` rule is only reachable after the reviewer denies the first
  appeal — the obvious "appeal twice" test passes for the wrong reason and leaves the one-appeal rule
  unexercised. Added it as a fifth elaboration ruling, split criterion 2 into the two distinct 409
  paths, added a checklist line, and fixed a pre-existing "three answers"/"three tests" count drift
- 2026-07-25 · m11 · ran the test-lock bolt for real (all 5 criteria met: 5-row `@CsvSource` table,
  routing asserted alongside score, boundary pinned against the constant, `explain(...)` covered,
  8 tests green; mutation check red-then-green as the checklist demands) — then reverted so the
  one-starter-test gap survives. Construction surfaced a floating-point trap: the stacked row the
  module specifies as **0.55** is `0.5499999999999999` in doubles, so `isEqualTo(0.55)` fails on
  exactly the row m11 tells students to write, while the four single-factor rows come out exact and
  pass. Added a third elaboration ruling (compare with `isCloseTo(..., within(1e-9))`), annotated
  criterion 1, and extended the recompute-by-hand checklist line. Also confirmed m11's other claim:
  no penalty subset reaches 0.85, so the `>=` boundary really is unreachable through a real request
- 2026-07-25 · m12 · ran the defect bolt for real on top of a reconstructed m11 suite. The red-first
  sequence works exactly as written: the 10-unit test fails at `0.9` against an expected `0.75` (the
  message criterion 1 promises), the `>` → `>=` fix turns it green at 10 tests, 9 units still scores
  0.90, and the seeded rows stay 0.90/0.70/0.75 — so m05's tour and m06's verify survive the fix.
  Live verify confirmed 10 units → PENDING_REVIEW at 0.75. One correction: the Expected output
  claimed "one updated table row", but **no m11 row changes** — those rows use 1 and 24 units, and
  only exactly-10 is affected. What goes stale is prose (the table comment, the constant's Javadoc,
  the README list). Rewrote that line and added a note warning that editing a row's expected value
  to reach green means the fix has overreached. Criterion 3 already hedged correctly ("rows or
  comments"), so it needed no change
- 2026-07-26 · m13 · ran the refactor bolt for real. Criterion 3 holds: Module 11's table passes
  **unmodified** against a penalty-supplier refactor (ScoringRule interface + 3 rule classes + a
  fold in the service), 8 tests green, and the prescribed live spot check (seeded MRI at 0.70 /
  PENDING_REVIEW) passes. But "zero behavior change" is not literally true: summing penalties and
  subtracting once is a different floating-point operation from subtracting them one at a time, so
  a stacked request goes from `0.5499999999999999` to exactly `0.55` (proved with a probe test and
  through the API). Routing and the `%.2f` explain text are unmoved; only the raw score field
  shifts, by ~1e-16 — absorbed by m11's tolerance. Two notes added: criterion 3 now defines what
  "zero behavior change" covers and warns that an exact-equality table will appear to be *fixed*
  by this bolt, and the verify block notes the seed has no stacked request, so the prescribed spot
  check is structurally blind to this class of drift
- 2026-07-26 · m04/m06/m24/m25 · first pass with a **real Claude Code session** (`claude -p`, using the
  repo's own login) rather than reading the prompts. m04's first-contact claim holds exactly — the
  answer named the 0.90 base, all three penalties and the `>= 0.85` comparison, and unprompted it
  flagged both defects found earlier by building (0.85 unreachable; the `> 10` off-by-one). m24/m25
  verified end to end: `stream-json` shows the very first tool call is `Agent` with
  `subagent_type: code-reviewer`, i.e. the shipped agent file is genuinely delegated to; it caught
  the planted scoring-without-tests violation, grouped findings by severity with file:line, reported
  rather than edited, and additionally spotted that the change left `SKILL.md` and the README stale —
  noting a stale auto-loaded Skill "actively feeds the wrong penalty to the next AI-assisted change".
  **m06 produced a live confident error**: a trace correct at every step that also asserted
  "in IEEE-754 doubles `0.90 - 0.20` is actually `0.7000000000000001`". It is exactly `0.70` (verified
  in Java). Captured it in m06 as a worked specimen, because the shape — a right answer with an
  invented supporting detail — is harder to catch than the wrong-score case the module already
  describes; added a checklist line about auditing asides. Also noted in m25 that a headless
  `claude -p` review runs without shell access, so the subagent can't run the build
- _(add a line per session: date · module · what changed)_

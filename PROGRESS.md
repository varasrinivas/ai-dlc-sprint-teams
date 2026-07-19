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
- _(add a line per session: date · module · what changed)_

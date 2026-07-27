# AI-DLC for Sprint Teams — Prior Auth Portal

A beginner-friendly, hands-on course that migrates a sprint team to **AI-DLC — the AI-Driven
Development Lifecycle** (AWS, 2025): AI drives planning and building, humans validate at
checkpoints; work moves in **bolts** (hours–days) instead of sprints. Built to be authored *with*
Claude Code, one module per session.

AI-DLC is tool-agnostic, so the course teaches it dual-path — every bolt lab is run once with
**Claude Code** and once with **GitHub Copilot** — on a real, runnable **Spring Boot** service
(the "Prior Auth Portal").

## What's in here

```
ai-dlc-sprint-teams/
├── course/
│   └── index.html            # the course player — open in a browser
├── labs/
│   ├── priorauth-service/    # the runnable Spring Boot app used by every lab
│   └── priorauth-web/        # the React provider portal (the front-end track's app)
├── tools/
│   ├── inject_module.py      # splice a built module into the player
│   ├── validate.py           # check the player / a module
│   └── deploy.py             # publish the player to S3 + CloudFront
├── .claude/commands/         # authoring slash commands
│   ├── plan-module.md
│   ├── build-module.md
│   ├── build-lab.md
│   └── validate-module.md
├── build/                    # module drafts + plans land here (git-ignored)
├── CLAUDE.md                 # authoring context for Claude Code
└── PROGRESS.md               # module build tracker
```

## Read the course

Open `course/index.html` in any modern browser. **All 32 modules are authored** across nine
tracks — including the provider-portal (React) track built on `labs/priorauth-web/` — including a dedicated leadership track (DORA/SPACE/AI-Capabilities scoreboard, engineering the metrics, and evidence for leadership) — including an everyday-developer-craft track (autocomplete/inline-chat/CLI skills and defect raising) — from the sprints-to-bolts shift through construction bolts, team practice, productivity
evidence for leadership (with a ready brief template in `docs/leadership-brief.md`), and the
AI-engineering track. Progress is saved per-device, and the layout works on mobile.

## Run the app the labs use

```bash
cd labs/priorauth-service
mvn spring-boot:run          # http://localhost:8080
```

See `labs/priorauth-service/README.md` for the API, the rules engine, and example requests.
The app has an intentional gap — no appeals endpoint — which a lab adds.

For the front-end track, run the React portal too:

```bash
cd labs/priorauth-web
npm install
npm run dev                  # http://localhost:5173, proxies /api to :8080
```

It ships with its own intentional gaps (no submit form, no appeal flow, one starter test) —
those are the m29–m31 labs.

## Extend or revise the course (with Claude Code)

From the repo root:

```bash
claude
```

Revise a module or add new ones on the standard loop, one per session:

```
/plan-module 2        # writes build/m02.plan.md
/build-module 2       # writes build/m02.html, injects + validates it, updates PROGRESS.md
/validate-module 2    # automated + content review
```

Open the player, confirm module 2 renders, then `/clear` and move to the next. For lab modules
use `/build-lab <n>` instead of `/build-module`. Everything the commands need — the component
kit, the module plan, the conventions — is in `CLAUDE.md`.

## Publish it

The player is one self-contained file, so a deploy is a single upload plus a cache
invalidation. From the repo root:

```bash
python tools/deploy.py              # validate, upload, invalidate
python tools/deploy.py --dry-run    # show every step, change nothing
```

It validates the player first, warns if the working tree is dirty or the branch isn't
`main`, skips the upload when the live file already matches, and verifies the deployed
ETag against the local checksum. Live at
<https://learnings.varasrinivas.com/ai-dlc-sprint-teams/>.

Add `--strict` to turn those git warnings into a refusal — worth using in CI. The bucket,
key prefix, and CloudFront distribution default to the live site and can be overridden
with `--bucket` / `--prefix` / `--distribution`. Needs the AWS CLI on PATH with
credentials that can write the bucket and create invalidations.

## Extending it later

The player and tooling are built to grow. The roadmap (see `CLAUDE.md`) includes a **React
provider portal** that calls this API and a **second microservice** — added as new tracks in the
`MODS` array plus new apps under `labs/`, with no changes to the player or the tools. Module 17 is
the on-ramp to the React track.

## Requirements

- **Read the course:** just a browser.
- **Run the labs:** Java 17+ and Maven 3.9+.
- **Do the labs:** Claude Code (`npm install -g @anthropic-ai/claude-code`) and/or GitHub Copilot
  in VS Code. Module 4 walks through setup.
- **Author the course:** Claude Code, plus Python 3 for the tools.
- **Publish the course:** the AWS CLI, authenticated against the account that owns the bucket.

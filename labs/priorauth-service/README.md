# Prior Auth Portal — starter service

This is the running application used throughout the **AI-Assisted Development** course.
It's a small, layered Spring Boot service so you can practice real sprint tasks — adding
features, writing tests, fixing bugs, refactoring — with Claude Code and GitHub Copilot.

## Prerequisites

- Java 17 or newer
- Maven 3.9+
- (For the labs) Claude Code and/or GitHub Copilot — set up in Module 4

## Run it

```bash
mvn spring-boot:run
```

The service starts on `http://localhost:8080`. Three example requests are seeded on startup.

## Try the API

```bash
# List seeded requests (one APPROVED, two PENDING_REVIEW)
curl http://localhost:8080/api/v1/prior-auth

# Submit a routine request -> auto-approved (score 0.90)
curl -X POST http://localhost:8080/api/v1/prior-auth \
  -H "Content-Type: application/json" \
  -d '{"memberId":"MBR-2001","providerNpi":"1234567890","serviceCode":"99213","diagnosisCode":"M54.5","requestedUnits":1}'

# Submit an MRI (review-required service) -> routed for review
curl -X POST http://localhost:8080/api/v1/prior-auth \
  -H "Content-Type: application/json" \
  -d '{"memberId":"MBR-2002","providerNpi":"1234567890","serviceCode":"70551","diagnosisCode":"R51.9","requestedUnits":1}'

# A reviewer approves a pending request (use an id that is PENDING_REVIEW)
curl -X POST http://localhost:8080/api/v1/prior-auth/2/decision \
  -H "Content-Type: application/json" \
  -d '{"decision":"APPROVED","reason":"Clinical notes support the request"}'
```

Browse the database at `http://localhost:8080/h2-console`
(JDBC URL `jdbc:h2:mem:priorauth`, user `sa`, no password).

## Endpoints

| Method | Path                              | Purpose                                   |
|--------|-----------------------------------|-------------------------------------------|
| POST   | `/api/v1/prior-auth`              | Submit a request (auto-scored)            |
| GET    | `/api/v1/prior-auth/{id}`         | Fetch one request                         |
| GET    | `/api/v1/prior-auth?status=...`   | List requests, optionally filter by status |
| POST   | `/api/v1/prior-auth/{id}/decision`| Reviewer approves or denies a pending one |

> There is intentionally **no** `POST /{id}/appeal` endpoint yet — you build it in a lab.

## The rules engine

`AutoApprovalService` scores each request from 0.0 to 1.0:

- Starts at **0.90**
- **−0.20** if the service code is review-required (e.g. `70551` MRI)
- **−0.15** if requested units > 10
- **−0.10** if the diagnosis code is blank
- Clamped to `[0.0, 1.0]`

A request is auto-approved when the score is **>= 0.85** (`AUTO_APPROVE_THRESHOLD`); otherwise
it becomes `PENDING_REVIEW`.

> **Utilization policy (UM-401):** requests of **10 or more units** require human review before
> approval. The engine's high-units penalty is the implementation of this policy.

## Project layout

```
src/main/java/com/portal/priorauth/
├── PriorAuthApplication.java       # entry point
├── domain/
│   ├── PriorAuthRequest.java       # JPA entity
│   └── AuthStatus.java             # lifecycle enum
├── repository/
│   └── PriorAuthRepository.java    # Spring Data JPA
├── service/
│   ├── AutoApprovalService.java    # the rules engine (0.85 threshold)
│   └── PriorAuthService.java       # use-case orchestration
├── web/
│   ├── PriorAuthController.java    # REST endpoints
│   ├── GlobalExceptionHandler.java # error -> HTTP mapping
│   └── dto/                        # request/response records
└── config/
    └── DataSeeder.java             # seeds example data on startup
```

See `CLAUDE.md` (for Claude Code) and `.github/copilot-instructions.md` (for Copilot) —
these give your AI tools the project context that makes their output fit this codebase.

## This is an AI-ready repo

Beyond the context files above, the repo ships a working AI setup you can use and learn from
(the subject of the course's "AI engineering & automation" track):

- `.claude/agents/code-reviewer.md` and `.claude/agents/security-reviewer.md` — review subagents.
  Try: *"have the code-reviewer subagent review my changes"* in a Claude Code session.
- `.claude/skills/prior-auth-rules/SKILL.md` — a Skill that loads automatically when you work on
  the auto-approval scoring.
- `.github/workflows/claude-code-review.yml` and `claude.yml` — automated PR review and on-demand
  `@claude`. Set them up with `claude /install-github-app`.

# CLAUDE.md — Prior Auth Portal service

This file is read automatically by Claude Code when you launch it in this folder.
It is the codebase's "onboarding doc" for your AI teammate. Keep it accurate and
commit it to git so the whole sprint team shares the same context.

## What this app is

A small Spring Boot service for the **Prior Auth Portal**. A healthcare provider submits a
prior authorization request for a member; the service scores it and either **auto-approves**
routine requests or routes the rest to a **human reviewer**.

## Stack

- Java 17, Spring Boot 3.3.x (web, data-jpa, validation)
- H2 in-memory database (data resets on restart)
- Maven build; JUnit 5 + AssertJ + Mockito for tests

## Architecture (layered — respect the boundaries)

```
web (Controller + DTOs)  ->  service (use cases)  ->  repository (JPA)  ->  H2
                                     |
                                     +-> AutoApprovalService (the rules engine)
```

- Controllers are thin. They validate input and delegate to a service. They never touch the repository.
- Services hold use-case logic and transactions.
- The rules engine (`AutoApprovalService`) is pure and deterministic — no I/O.

## Conventions (please follow)

- **Never expose JPA entities over the wire.** Map to a DTO record (`AuthResponse`) in the web layer.
- Mutate `PriorAuthRequest` only through `applyDecision(...)`, not with setters.
- Request DTOs use Bean Validation annotations; validation errors return 400 via `GlobalExceptionHandler`.
- New endpoints live under `/api/v1/prior-auth`.
- Prefer constructor injection.
- Keep the rules engine free of framework/database calls so it stays unit-testable.

## The domain rule (important)

`AutoApprovalService.AUTO_APPROVE_THRESHOLD = 0.85`.
A request is auto-approved when its score is **>= 0.85**; otherwise it becomes `PENDING_REVIEW`.
Scoring starts at 0.90 and subtracts penalties (review-required service, high units, blank diagnosis),
clamped to [0.0, 1.0]. If you change the scoring, update the tests in the same change.

## Status lifecycle

`SUBMITTED` → (`APPROVED` | `PENDING_REVIEW`) → a reviewer decides `PENDING_REVIEW` into (`APPROVED` | `DENIED`).

## Build & run

```bash
./mvnw spring-boot:run        # starts on http://localhost:8080
./mvnw test                   # runs the test suite
```

Seed data loads three example requests on startup (one auto-approve, two review paths).

## Known gaps (intentional — these are course labs)

- There is **no appeals endpoint** yet. (Lab: add `POST /{id}/appeal`.)
- The rules engine has only one starter test. (Lab: build a full suite.)

## Gotchas

- H2 is in-memory: every restart wipes the data. That's expected for labs.
- `providerNpi` must be exactly 10 digits or submission returns 400.

## AI setup in this repo (this is an "AI-ready" repo)

This repo is deliberately equipped for AI-assisted development. Reuse these instead of
re-explaining conventions:

- **`CLAUDE.md`** (this file) and **`.github/copilot-instructions.md`** — shared project context.
- **`.claude/agents/code-reviewer.md`** — a code-review subagent. Invoke it with
  "have the code-reviewer subagent review my changes", or let Claude delegate to it after edits.
- **`.claude/agents/security-reviewer.md`** — a security/data-handling subagent for the healthcare context.
- **`.claude/skills/prior-auth-rules/SKILL.md`** — a Skill that loads automatically when working on
  the auto-approval scoring, so rules stay explainable, deterministic, and tested.
- **`.github/workflows/claude-code-review.yml`** and **`.github/workflows/claude.yml`** — automated PR
  review and on-demand `@claude` in pull requests. Set them up with `claude /install-github-app`.

Subagent and skill files are loaded at session start — restart Claude Code after editing them.

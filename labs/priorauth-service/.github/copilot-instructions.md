# GitHub Copilot instructions — Prior Auth Portal service

GitHub Copilot reads this file automatically and applies it as repo-wide context for
Copilot Chat and code suggestions. It is the Copilot counterpart to `CLAUDE.md`.
Keep the two roughly in sync.

## Project

Spring Boot service for the **Prior Auth Portal**. Providers submit prior authorization
requests; routine ones are auto-approved, the rest go to a human reviewer.

## Stack

Java 17, Spring Boot 3.3.x (web, data-jpa, validation), H2 in-memory DB, Maven, JUnit 5 + AssertJ.

## Rules for generated code

- Keep the layering: **Controller → Service → Repository**. Controllers must not call repositories.
- Do **not** return JPA entities from controllers. Map to the `AuthResponse` record.
- Change `PriorAuthRequest` state only through `applyDecision(...)`.
- Use constructor injection, not field injection.
- Put new endpoints under `/api/v1/prior-auth`.
- Add Bean Validation annotations to request DTOs; rely on `GlobalExceptionHandler` for error shapes.
- Keep `AutoApprovalService` pure and deterministic (no I/O), so it stays unit-testable.

## Domain rule

`AUTO_APPROVE_THRESHOLD = 0.85`. Auto-approve when score **>= 0.85**, else `PENDING_REVIEW`.
When you touch the scoring logic, update the corresponding tests in the same change.

## Tests

Prefer JUnit 5 with AssertJ assertions. For the rules engine, favor `@ParameterizedTest`
with `@CsvSource`. Always include the exact `0.85` boundary case.

## Style

Small, focused methods. Clear names over comments. Match the existing package structure
under `com.portal.priorauth`.

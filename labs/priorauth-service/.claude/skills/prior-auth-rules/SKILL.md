---
name: prior-auth-rules
description: Conventions for the Prior Auth auto-approval rules engine. Use whenever adding, changing, or reviewing approval scoring logic, the auto-approval threshold, or AutoApprovalService — so scoring stays explainable, deterministic, and covered by tests.
---

# Prior Auth rules engine

Apply this whenever the task touches auto-approval scoring (`AutoApprovalService`), the approval
threshold, or how requests are routed to review. The goal is a rules engine that a reviewer or
auditor can read and trust.

## The model

- Every request gets a score in `[0.0, 1.0]`. Higher = more confidently routine.
- Scoring starts at a **base of 0.90** and **subtracts penalties**. The result is clamped to `[0,1]`.
- A request is **auto-approved when score >= `AUTO_APPROVE_THRESHOLD` (0.85)**; otherwise it becomes
  `PENDING_REVIEW`.
- Current penalties: review-required service code (−0.20), requested units > 10 (−0.15),
  blank diagnosis code (−0.10).

## Rules for changing the engine

1. **Keep it pure and deterministic.** No database, network, clock, or randomness inside scoring —
   the same request must always produce the same score. This keeps it unit-testable.
2. **Make each factor explainable.** A penalty must correspond to a real clinical/administrative
   reason, and `explain(...)` should be able to describe the outcome to a provider in plain language.
3. **Never change the threshold silently.** `0.85` is a business decision. If a task asks to move it,
   flag it and confirm before changing, and update every test that depends on it.
4. **Add a factor as a small, named step**, not a tangle of nested conditions. If the engine grows,
   prefer extracting each factor into its own method or a `Rule` object (see the refactor lab).
5. **Update tests in the same change.** No scoring change ships without matching tests.

## Test conventions

- Use JUnit 5 with AssertJ.
- Prefer `@ParameterizedTest` with `@CsvSource` for the scoring table.
- **Always include the exact boundary:** a request scoring precisely `0.85` must auto-approve
  (the comparison is `>=`).
- Cover each penalty in isolation and at least one request where penalties stack.

## Example: adding a new penalty (the correct shape)

When asked to add, say, a penalty for out-of-network providers:

1. Add a single, named check in `score(...)` that subtracts a small, justified amount.
2. Make sure `explain(...)` still returns a sensible reason.
3. Add parameterized test rows: the new factor alone, and combined with an existing one.
4. Run `mvn test` and confirm the boundary case still passes.

Do **not**: hard-code approvals/denials for specific members, add hidden side effects, or introduce
non-determinism (e.g. "approve 10% at random").

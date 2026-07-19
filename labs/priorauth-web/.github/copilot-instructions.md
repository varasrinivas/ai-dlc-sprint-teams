# Copilot instructions — Prior Auth Portal, provider web app

React 19 + Vite SPA (plain JSX, no TypeScript, no router). Providers submit prior auth
requests, watch status, and appeal denials. All business rules live in the Spring service at
`/api/v1/prior-auth`; the dev server proxies `/api` to `localhost:8080`.

Rules for generated code:

- All HTTP goes through `src/api/priorAuth.js` — components never call `fetch` directly.
  Non-2xx responses throw `ApiError` carrying the RFC 7807 ProblemDetail `detail` message.
- Statuses mirror the service enum exactly: `SUBMITTED`, `APPROVED`, `PENDING_REVIEW`,
  `DENIED`. Render human-readable labels; keep raw values in `data-status` attributes.
- Never re-implement scoring or the 0.85 threshold in the UI — display `approvalScore` and
  `decisionReason` from the API only.
- Form validation may pre-check (`providerNpi` = exactly 10 digits, `requestedUnits` >= 1),
  but always surface the server's 400 `detail` as the source of truth.
- Presentational components stay pure (props in, markup out); fetching stays in page-level
  components. One component per file in `src/components/`, tests beside it as `Foo.test.jsx`
  (Vitest + React Testing Library).
- Healthcare-adjacent app: never log member data to the console.

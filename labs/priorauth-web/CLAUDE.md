# CLAUDE.md — Prior Auth Portal, provider web app

Read automatically by Claude Code when launched in this folder. This is the web repo's
persistent context — the front-end sibling of `../priorauth-service/CLAUDE.md`. Keep it
accurate; every elaboration decision the team makes in a bolt gets recorded here.

## What this app is

A small React single-page app for **providers**: submit a prior authorization request for a
member, watch its status, and (once denied) file an appeal. It talks only to the Prior Auth
service API at `/api/v1/prior-auth` — it holds no business rules of its own.

## Stack

- React 19 + Vite (plain JavaScript/JSX — no TypeScript, no router yet)
- Vitest + React Testing Library + jsdom for component tests
- No state library: `useState`/`useEffect` are enough at this size

## Run it

```bash
# 1. start the API first (separate terminal):
cd ../priorauth-service && mvn spring-boot:run     # :8080

# 2. then the web app:
npm install
npm run dev                                        # :5173, proxies /api -> :8080
npm test                                           # vitest run
```

The Vite dev server proxies `/api` to `localhost:8080` (see `vite.config.js`), so there is no
CORS setup anywhere. If the UI shows "is the Prior Auth service running?", start the service.

## Architecture (respect the boundaries)

```
App.jsx (shell)  ->  components/*  ->  api/priorAuth.js  ->  fetch  ->  Spring service
```

- **All HTTP goes through `src/api/priorAuth.js`.** Components never call `fetch` directly.
- The API client throws `ApiError` with the ProblemDetail `detail` message (RFC 7807) and the
  HTTP status; components surface `error.message` to the user, never a raw response.
- Presentational components (`StatusBadge`) are pure: props in, markup out. Data fetching
  stays in page-level components (`RequestList`).

## Conventions (please follow)

- The status enum mirrors the service exactly: `SUBMITTED`, `APPROVED`, `PENDING_REVIEW`,
  `DENIED`. Render human labels ("Pending review"), keep raw values in `data-status`.
- **The web app never re-implements scoring.** The 0.85 auto-approve threshold belongs to the
  rules engine; the UI only displays `approvalScore` and `decisionReason` the API returns.
- Validation mirrors, never replaces, the server: the form may pre-check (NPI = exactly
  10 digits, units >= 1), but the server's 400 `detail` is the truth and must be shown.
- This is healthcare-adjacent: **never log member data to the console** and keep fake-but-
  realistic seed values (`MBR-1001`, CPT-style codes) out of error messages sent anywhere.
- New components in `src/components/`, one component per file, tests next to the component
  (`Foo.test.jsx`).

## Known gaps (intentional — these are course labs)

- **No submit form.** (Lab: build "New request" against `POST /api/v1/prior-auth`.)
- **No appeal flow.** (Lab: appeal a DENIED request via `POST /{id}/appeal` — that endpoint
  is itself built in a service-side lab; do that bolt first.)
- **Tests are thin.** One starter test (`StatusBadge.test.jsx`). (Lab: grow a real suite.)

## Gotchas

- The service's H2 database is in-memory: restarting it resets the data to the three seed rows.
- `providerNpi` must be exactly 10 digits or the API returns 400.
- `approvalScore` is `null` until a request has been scored — guard before `.toFixed(2)`.

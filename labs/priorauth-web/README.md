# Prior Auth Portal — provider web app

The React front-end for the [Prior Auth service](../priorauth-service/): providers submit
prior authorization requests, watch their status, and file appeals. It is the shared codebase
for the course track **"The provider portal (React)"**.

## Run it

```bash
# terminal 1 — the API:
cd ../priorauth-service && mvn spring-boot:run    # http://localhost:8080

# terminal 2 — the web app:
npm install
npm run dev                                       # http://localhost:5173
npm test                                          # component tests (Vitest)
```

The Vite dev server proxies `/api` to the service, so no CORS setup is needed.

## What's here — and what's deliberately missing

Shipped: the request list with status filter, score, and decision reason (`RequestList`,
`StatusBadge`), an API client (`src/api/priorAuth.js`), and one starter test.

Intentionally missing — these are course labs:

- the **"New request" submit form**,
- the **appeal flow** for denied requests (its API endpoint is also a lab, on the service side),
- a real **component test suite**.

This repo is AI-ready: `CLAUDE.md` (Claude Code) and `.github/copilot-instructions.md`
(GitHub Copilot) carry the project context your AI assistant needs.

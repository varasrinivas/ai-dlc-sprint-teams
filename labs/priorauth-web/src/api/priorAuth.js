// The only file that talks HTTP. Components never call fetch directly — they import
// from here, so the API contract lives in one place.
//
// In dev, Vite proxies /api to the Spring Boot service on :8080 (see vite.config.js).

const BASE = '/api/v1/prior-auth';

/** Error thrown for any non-2xx response. `message` is the ProblemDetail `detail`. */
export class ApiError extends Error {
  constructor(message, status) {
    super(message);
    this.name = 'ApiError';
    this.status = status;
  }
}

async function handle(res) {
  if (res.ok) return res.json();
  // The service returns RFC 7807 ProblemDetail: { type, title, status, detail }.
  let detail = `Request failed (${res.status})`;
  try {
    const problem = await res.json();
    if (problem.detail) detail = problem.detail;
  } catch {
    // Non-JSON body (e.g. the service is down and the proxy answered) — keep the default.
  }
  throw new ApiError(detail, res.status);
}

/** List requests, optionally filtered: listRequests('PENDING_REVIEW'). */
export async function listRequests(status) {
  const url = status ? `${BASE}?status=${encodeURIComponent(status)}` : BASE;
  return handle(await fetch(url));
}

/** Fetch a single request by id. */
export async function getRequest(id) {
  return handle(await fetch(`${BASE}/${id}`));
}

// NOTE: There is intentionally no submitRequest(...) and no appealRequest(...) here yet.
// Adding them is a course lab (see CLAUDE.md, "Known gaps").

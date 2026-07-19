import { useEffect, useState } from 'react';
import { listRequests } from '../api/priorAuth.js';
import StatusBadge from './StatusBadge.jsx';

const STATUSES = ['', 'SUBMITTED', 'APPROVED', 'PENDING_REVIEW', 'DENIED'];

/**
 * The provider's view of every prior auth request: fetches from the API,
 * lets the user filter by status, and shows score + decision reason.
 */
export default function RequestList() {
  const [requests, setRequests] = useState([]);
  const [statusFilter, setStatusFilter] = useState('');
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    let cancelled = false;
    setLoading(true);
    setError(null);
    listRequests(statusFilter || undefined)
      .then((data) => { if (!cancelled) setRequests(data); })
      .catch((err) => { if (!cancelled) setError(err.message); })
      .finally(() => { if (!cancelled) setLoading(false); });
    return () => { cancelled = true; };
  }, [statusFilter]);

  return (
    <section>
      <div className="toolbar">
        <label>
          Status{' '}
          <select value={statusFilter} onChange={(e) => setStatusFilter(e.target.value)}>
            {STATUSES.map((s) => (
              <option key={s} value={s}>{s === '' ? 'All' : s}</option>
            ))}
          </select>
        </label>
      </div>

      {loading && <p className="muted">Loading…</p>}
      {error && (
        <p className="error" role="alert">
          {error} — is the Prior Auth service running on port 8080?
        </p>
      )}

      {!loading && !error && (
        <table className="requests">
          <thead>
            <tr>
              <th>ID</th>
              <th>Member</th>
              <th>Service</th>
              <th>Units</th>
              <th>Score</th>
              <th>Status</th>
              <th>Reason</th>
            </tr>
          </thead>
          <tbody>
            {requests.map((r) => (
              <tr key={r.id}>
                <td>{r.id}</td>
                <td>{r.memberId}</td>
                <td>{r.serviceCode}</td>
                <td>{r.requestedUnits}</td>
                <td>{r.approvalScore == null ? '—' : r.approvalScore.toFixed(2)}</td>
                <td><StatusBadge status={r.status} /></td>
                <td className="muted">{r.decisionReason ?? ''}</td>
              </tr>
            ))}
            {requests.length === 0 && (
              <tr><td colSpan="7" className="muted">No requests match this filter.</td></tr>
            )}
          </tbody>
        </table>
      )}
    </section>
  );
}

// Pure presentational component: status string in, colored badge out.
// The full lifecycle is SUBMITTED -> (APPROVED | PENDING_REVIEW) -> (APPROVED | DENIED).

const LABELS = {
  SUBMITTED: 'Submitted',
  APPROVED: 'Approved',
  PENDING_REVIEW: 'Pending review',
  DENIED: 'Denied',
};

export default function StatusBadge({ status }) {
  const label = LABELS[status] ?? status;
  return (
    <span className={`badge badge--${status.toLowerCase()}`} data-status={status}>
      {label}
    </span>
  );
}

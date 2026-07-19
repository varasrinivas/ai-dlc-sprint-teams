import { render, screen } from '@testing-library/react';
import StatusBadge from './StatusBadge.jsx';

// Starter test — the same "one starter test" pattern as the service repo.
// A course lab grows this into a real suite (form validation, appeal visibility, API errors).

describe('StatusBadge', () => {
  it('renders PENDING_REVIEW as a human-readable label with the right styling hook', () => {
    render(<StatusBadge status="PENDING_REVIEW" />);
    const badge = screen.getByText('Pending review');
    expect(badge).toBeInTheDocument();
    expect(badge).toHaveClass('badge--pending_review');
  });
});

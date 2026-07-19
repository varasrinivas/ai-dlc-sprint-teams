import RequestList from './components/RequestList.jsx';

/**
 * App shell: header + the one page that exists so far.
 *
 * Known gaps (intentional — these are course labs, see CLAUDE.md):
 *   - no "New request" form (lab: submit a request from the browser)
 *   - no appeal action on denied requests (lab: file an appeal from the portal)
 */
export default function App() {
  return (
    <div className="app">
      <header className="app__header">
        <h1>Prior Auth Portal</h1>
        <p className="app__sub">provider view · auto-approval threshold 0.85</p>
      </header>
      <main>
        <RequestList />
      </main>
    </div>
  );
}

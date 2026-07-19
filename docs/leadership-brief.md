# AI-DLC productivity brief — <team> — <period>

> One page, same format every cycle, so trends read at a glance. Numbers over adjectives.
> Sources: cycle times from <tracker>, effort from <timesheet/estimate records>, defects from <issue tracker>.

## What ran this period
| Unit of work | Bolts | Shipped |
|---|---|---|
| <e.g. Appeals flow (API)> | 3 | <date> |

## The delta (baseline vs. AI-DLC)
| Measure | Baseline (pre-pilot avg) | This period | Delta |
|---|---|---|---|
| Time-to-market (commit → ship, days) | <n> | <n> | <±%> |
| Cost per unit (person-days incl. validation) | <n> | <n> | <±%> |
| Escaped defects (30 days post-ship) | <n> | <n> | <±> |
| Coverage (eligible work run as bolts) | — | <n%> | — |

Baseline: <3–5 named comparable units completed <dates>, measured identically. Recorded <date>, before the pilot.>

## The spend (so the gain reads net)
- Tooling: <licenses/API cost this period>
- Validation attention: <senior hours across checkpoints; note trend>

## Risk posture
Guardrails in force: synthetic data in prompts; secrets in stores; human validation on every merged
change (named validator per bolt); security-sensitive and invariant changes human-led; automated
first-pass review on all PRs. Exceptions this period: <none | list>.

## The ask
<What expanding coverage needs next: e.g., extend to <team/area>, one mob-facilitation training,
continue current tooling spend. One sentence, one decision.>

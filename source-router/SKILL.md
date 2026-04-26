---
name: source-router
description: Route source-intelligence requests to the first lane and effort tier; return a source plan, not a brief.
---

# Source Router

Use this as the thin front door. Choose the first source lane and effort tier; do not do deep research here.

Read first:
- `../source-common/references/research-contract.md`
- `../source-common/references/routing-matrix.md`
- `../source-common/references/router-cheat-sheet.md`
- `../source-common/references/safety-boundaries.md`

Workflow:
1. State the user's question, entity, time window, and output need.
2. Pick effort tier: quick, standard, deep, or watchlist.
3. Choose one first lane unless the request truly spans domains.
4. Name any secondary lane only when it adds verification or a distinct signal class.
5. Send gathered notes to `source-briefing` unless the user asked for raw links only.

Rules:
- social signal is never proof
- visual/artifact are optional end steps, not default routes
- use watchlists only for recurring/custom source universes

Output:
- selected lane(s)
- effort tier
- source plan
- missing input if blocked
- citation expectations
- missing evidence if blocked

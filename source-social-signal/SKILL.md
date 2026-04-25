---
name: source-social-signal
description: Gather weak social/X/Twitter signal for trends, leads, sentiment, creator/builder reactions, and early discovery only. Never treat social as sole factual evidence. Route to source-briefing for verification.
---

# Source Social Signal

Use only when social/X signal is specifically useful: early trend detection, sentiment, creator/builder reactions, or leads to verify elsewhere.

## Source pattern

Use read-only Twitter/X reader patterns for public URLs, explicit accounts, or search terms.

Do not use account cookies, posting, scraping at scale, or tools that send directly to messaging platforms without explicit approval.


## Reference links

Use social sources as weak signal only. Prefer read-only public URLs and avoid cookies/posting/scraping at scale:

- FxTwitter API pattern: https://api.fxtwitter.com/
- X developer docs: https://docs.x.com/
- HN Algolia Search API: https://hn.algolia.com/api
- GitHub discussions/search: https://docs.github.com/en/search-github

## Workflow

1. Collect public social items relevant to the request. If a curated social list exists, read `/home/ubuntu/.openclaw/workspaces/orin/source-watchlists/social-signal.md` through `source-watchlist` first.
2. Preserve URL/status ID, author/account, timestamp, and quoted claim.
3. Label as signal, not proof.
4. Verify factual claims through another `source-*` skill or primary source before final briefing.
5. Send source notes to `source-briefing`.

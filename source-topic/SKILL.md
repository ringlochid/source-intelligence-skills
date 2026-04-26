---
name: source-topic
description: Gather topic sources from RSS, blogs, newsletters, feeds, monitored pages, and watchlists.
---

# Source Topic

Use for topic monitoring, feeds, newsletters, blogs, source lists, and recurring digests.

Read first:
- `../source-common/references/safety-boundaries.md`
- `../source-common/references/source-quality-ladder.md`
- `../source-common/references/research-contract.md`
- `../source-common/references/stop-rules.md`
- `../source-common/references/citation-and-timestamp-rules.md`
- `../source-common/references/watchlist-state-rules.md`

Source hints: use RSS/blog/newsletter pages first; RSSHub/RSS-Bridge/changedetection-style expansion requires configured/approved tooling.

Workflow:
1. Identify topic, entities, source list, and time window.
2. If curated/recurring, read relevant watchlist through `source-watchlist`.
3. Fetch recent feed/source items.
4. Preserve title, URL, source, published/retrieved time, excerpt, and tags.
5. Drop obvious duplicates/stale items before briefing.
6. Send notes to `source-briefing` unless the user asked for raw links only.

Output:
- topic scope
- sources checked
- normalized source notes
- stale/missing sources
- next briefing lane
- missing evidence
- citation/source link

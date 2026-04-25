---
name: source-topic
description: Gather topic sources from RSS, blogs, newsletters, feeds, and monitored pages. Use for ongoing topic tracking, digest inputs, niche source lists, and general source collection. Route to source-briefing.
---

# Source Topic

Use for topic monitoring and feed-style source gathering.

## Source pattern

Prefer RSSHub/RSS-Bridge style feed expansion and Miniflux/FreshRSS/Folo-style feed state if configured. If not configured, use direct RSS/web fetch and keep the run stateless.


## Reference links

Use these as feed/source infrastructure references, not mandatory dependencies:

- RSSHub: https://github.com/DIYgod/RSSHub
- RSS-Bridge: https://github.com/RSS-Bridge/rss-bridge
- Miniflux: https://miniflux.app/docs/
- FreshRSS: https://freshrss.github.io/FreshRSS/
- changedetection.io: https://github.com/dgtlmoon/changedetection.io

## Workflow

1. Identify topic, entities, and watchlist/source list if provided. If the request is recurring or curated, read live workspace watchlists through `source-watchlist` first.
2. Fetch recent feed items or source pages.
3. Keep title, URL, source, published time, retrieved time, excerpt, and topic tags.
4. Drop obvious duplicates and stale items before briefing.
5. Send source notes to `source-briefing`.

For high-stakes claims, verify against primary/reputable sources before finalizing.

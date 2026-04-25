---
name: source-watchlist
description: Maintain lightweight Markdown watchlists for source-intelligence retrieval. Use when the user wants recurring topic monitoring, curated blogs/RSS/source lists, social-signal accounts, research queries, product/competitor sources, market sources, or saved source lists for source-router/source-topic/source-social-signal.
---

# Source Watchlist

Use this to keep source lists simple and human-readable. Watchlists are optional; ordinary one-off source requests can run without them.

## Purpose

A watchlist is a curated list of sources or queries that a `source-*` collector can use on demand.

It is **not** continuous monitoring by itself. It does not deploy services, schedule jobs, log into accounts, scrape cookies, or post externally.

## Locations

Live workspace watchlists live here:

```text
/home/ubuntu/.openclaw/workspaces/orin/source-watchlists/
├── ai-tech.md
├── research.md
├── product.md
├── market.md
├── social-signal.md
└── general-topics.md
```

Template watchlists live inside this skill:

```text
source-watchlist/references/watchlists/
```

Prefer live workspace watchlists. Use templates only to initialize missing files or inspect expected format.

Create or update only the relevant live file. Keep entries short.

## Entry format

```markdown
## <Source or query name>

- **Type:** rss | blog | official | repo | arxiv-query | openreview | product | market | social | page-watch
- **URL/query:** <url or query>
- **Priority:** high | medium | low
- **Use for:** <topics/intents>
- **Notes:** <constraints, caveats, language, verification rules>
```

## Language policy

Watchlists may include Chinese or multilingual sources. Final outputs remain English-first unless the user asks otherwise. Translate source titles/claims/summaries during briefing.

## Routing

- Blogs/RSS/source pages → `source-topic`
- X/social accounts/URLs → `source-social-signal`
- Research queries/sources → `source-research`
- GitHub repos/topics → `source-github`
- Product/competitor pages → `source-product`
- Market/tickers/companies → `source-market`

## Safety

- Do not add private/authenticated sources unless Leo explicitly asks.
- Do not store credentials, cookies, tokens, or private URLs.
- Social entries are weak signal only.
- For page monitoring, use the URL as an on-demand source unless a separate approved service is deployed.

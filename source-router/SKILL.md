---
name: source-router
description: Route source-intelligence requests by intent, effort tier, and source plan. Use for breaking news, topic monitoring, AI/tech/builder updates, research papers, GitHub/repo trends, product/marketing scans, finance/BTC/market checks, X/social signal, competitor research, business opportunity scans, and optional real visual asset workflows; choose 1-N source-* collectors then finish with source-briefing.
---

# Source Router

Use this as the front door for source intelligence. First infer intent and effort tier, then build a source plan with 1-N collectors, then finish with `source-briefing`.

English is the default language for skill design and final output. Chinese and other non-English sources are allowed; translate their titles/claims/summaries into English unless the user asks otherwise.

## Route table

- **Watchlists/source lists:** `source-watchlist` when the request uses recurring/custom sources
- **Breaking/current events:** `source-breaking`
- **Topic/RSS/feed monitoring:** `source-topic`
- **AI/tech/builder ecosystem:** `source-tech`
- **Research/papers/trending research:** `source-research`
- **GitHub/repo/release trends:** `source-github`
- **Product/marketing/launch scans:** `source-product`
- **Finance/BTC/markets:** `source-market`
- **X/social trend signal:** `source-social-signal`
- **Final synthesis:** `source-briefing`
- **Image-first visual read:** `source-visual` for selected pages/PDFs/charts/tables/screenshots/news images when the user asks for visual read or image evidence matters
- **File-backed artifacts:** `source-artifact` only when report/save/handoff/archive files are requested

## Full workflow

```text
intent
→ source plan
→ collect raw items
→ normalize
→ dedupe
→ review / validate claims
→ brief
→ optional real visual asset / image prompt
→ optional handoff / archive / watchlist update
```

`source-router` owns intent, effort tier, and source plan. Check live workspace watchlists via `source-watchlist` when curated/recurring sources are relevant. `source-briefing` owns normalize/dedupe/review/validate/final output. Use `source-visual` only on selected important/unclear sources after initial dedupe, and only when an image-first visual read is useful or requested. `source-artifact` only persists Markdown-first files when the user asks for report/save/handoff/archive.

## Effort tiers

- **Quick:** about 10-20 raw sources; fast current answer; usually 1 collector.
- **Standard:** about 20-50 raw sources; normal source scan; usually 1-3 collectors.
- **Deep:** about 50-100+ raw sources; serious research/product/business decision; actively seek contradictions; usually multiple collectors.
- **Watchlist update:** collect only new/changed sources since last known state.

Quality beats count: high-stakes, finance, and breaking-news claims still require primary/current verification even in quick mode.

## Source planning examples

- Latest arXiv papers → `source-research` only.
- Trending research in AI agents → `source-research` + optional `source-github`/`source-tech` for code/adoption signals.
- AI agent trend brief → `source-tech` + `source-github` + `source-research`.
- Product opportunity in AI coding tools → `source-product` + `source-tech` + `source-github` + optional `source-social-signal`.
- Competitor/marketing scan → `source-product` + `source-topic` + optional `source-social-signal`.
- Breaking Iran/US update → `source-breaking` + optional `source-social-signal`, with social signal never used as proof.

Output shapes such as quick brief, deep research, product scan, marketing plan inputs, business opportunity scan, competitor scan, and optional real visual asset are examples selected after the source plan, not separate routes.

## Time awareness

For current, trending, market, product, or news requests, newer sources and updates outrank older material by default. Use older sources as background only unless the user asks for historical analysis. Always preserve concrete publish/update/retrieval times when available.

## Hard rules

- Prefer primary/current sources over social or aggregators.
- Output in English by default, even when sources are Chinese/multilingual; preserve original names/terms when useful.
- Treat X/Twitter as signal only, never factual proof.
- Finance/BTC claims need separate price/data verification.
- Breaking news needs concrete timestamps and at least two credible sources for major claims.
- Do not deploy services, post externally, or use account cookies without explicit approval.
- For recurring/custom topics, inspect `/home/ubuntu/.openclaw/workspaces/orin/source-watchlists/` before choosing collectors.
- Visual/image/infographic requests still run through `source-briefing` first; generate real visual assets or editorial prompts only after facts are stable and only when explicitly requested.
- Use `source-visual` only when visual read/image evidence matters; it must produce image(s) first with a one-sentence caption by default, not a text-only section.
- Chat-only reports should use the `source-briefing` Telegram-readable pattern; keep formatting details canonical there.
- Do not call chat-only output a visual asset/brief. Real image/infographic/prompt/file output is optional and explicit-request only. Use `source-artifact` only for saved visual assets, prompts, or reports.

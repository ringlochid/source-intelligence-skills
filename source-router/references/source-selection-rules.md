# Source Selection Rules

This is a reference for `source-router`. Skill docs and outputs should be English-first, even when sources are Chinese or multilingual. Translate non-English titles/claims into English for the final brief, while preserving original names/terms when useful.

## Core workflow

```text
intent
→ effort tier
→ source plan
→ 1-N source-* collectors
→ source-briefing
→ optional source-visual
→ optional source-artifact
```

## Effort tiers

| Tier | Raw source target | Typical use |
|---|---:|---|
| Quick | 10-20 | Fast current answer or light scan |
| Standard | 20-50 | Normal source intelligence brief |
| Deep | 50-100+ | Research, product, business, or high-stakes decisions |
| Watchlist | changed/new only | Recurring topic/source tracking |

Quality beats count. If strong primary sources answer the question, do not pad with weak sources.

## Collector selection

### `source-breaking`

Use for fresh current events, breaking news, policy/regulatory updates, crisis events, and fast-moving market/company developments.

Prioritize:
- official statements and primary documents
- reputable/wire reporting
- concrete publication/update timestamps
- at least two credible sources for major claims

Pair with:
- `source-social-signal` only for early leads/sentiment
- `source-market` for market-moving claims
- `source-visual` for charts, maps, official PDFs, or visual evidence

### `source-topic`

Use for topic monitoring, RSS/blog/news feed scans, newsletters, niche source lists, and broad recurring digests.

Prioritize:
- RSS/feed sources
- official blogs and source pages
- stable source lists/watchlists
- changedetection/RSSHub/RSS-Bridge style source expansion when configured

Pair with:
- `source-tech`, `source-product`, or `source-market` when the topic belongs to a domain

### `source-tech`

Use for AI/tech/startup/builder ecosystem news, model/tool releases, developer platform changes, and technical product shifts.

Prioritize:
- official blogs/docs/changelogs
- GitHub repos/releases
- HN as discovery and discussion signal
- papers only when they materially affect the technical story

Pair with:
- `source-github` for repo/release momentum
- `source-research` for paper-driven trends
- `source-product` for launch/business implications

### `source-research`

Use for papers, literature scans, trending research, and research-to-product signals.

Prioritize:
- arXiv IDs/pages/PDFs
- Semantic Scholar/OpenAlex-style metadata
- OpenReview/conference pages
- Papers with Code and GitHub for implementation/benchmark signal

Pair with:
- `source-github` for code adoption
- `source-tech` for practitioner impact
- `source-visual` for figures/tables/PDFs when text extraction is insufficient

### `source-github`

Use for repositories, releases, developer tools, libraries, GitHub trends, and product/platform changes on GitHub.

Prioritize:
- repo pages, READMEs, releases, issues, commits
- GitHub Changelog and GitHub Blog as primary sources for GitHub product/platform changes
- activity signals: release date, stars, forks, issues, license, maintainers

Pair with:
- `source-tech` for ecosystem context
- `source-product` for product opportunities

### `source-product`

Use for product launches, competitor scans, marketing inspiration, positioning, pricing/package changes, and business opportunity scans.

Prioritize:
- official product pages
- changelog/docs/pricing pages
- Product Hunt as discovery, not proof of validation
- founder/company posts only when source identity is clear

Pair with:
- `source-tech` for builder/product categories
- `source-social-signal` for weak sentiment
- `source-visual` when page layout or screenshots matter

### `source-market`

Use for finance, BTC/crypto, company/ticker, funding, earnings, regulatory, and market-moving source gathering.

Prioritize:
- verified price/market data
- company IR/filings/regulator/exchange statements
- reputable finance wires
- clear timestamps and market-session context

Pair with:
- `source-breaking` for market-moving news
- `source-social-signal` only as weak sentiment

### `source-social-signal`

Use only for weak signals: early trend detection, creator/builder reactions, sentiment, and leads to verify elsewhere.

Never use social as sole evidence for factual claims. Avoid cookies, posting, or scraping at scale unless explicitly approved.

### `source-visual`

Use after initial collection/dedupe for selected important or unclear sources.

Use when:
- charts/tables/figures matter
- screenshots or visual evidence need inspection
- product/GitHub/research pages need layout context
- PDF text extraction is weak
- real visual asset accuracy depends on page/figure details
- visual read must output image(s) first with a one-sentence caption, not a text-only section

Usually inspect only the top 3-8 sources.

### `source-artifact`

Use only when the user asks to save/create/write a report, research pack, source pack, real visual asset prompt/spec file, handoff, archive, or watchlist update.

Sample artifact structures should be shown as a tree only unless the user explicitly asks to create/write files.

## Counter-evidence rule

Use counter-evidence when:
- the user asks for evaluation, comparison, risk, or investment/product judgment
- the claim is high-stakes or controversial
- a dominant narrative may have confirmation bias
- sources conflict or are mostly social/aggregator signals

Counter-evidence can come from primary sources, critical reviews, failed replications, regulator warnings, caveats in papers, negative user reports, or credible contradictory reporting.

## Stop rules

| Scenario | Stop when |
|---|---|
| Breaking news | 2+ credible sources agree on major claims, or uncertainty is clearly stated |
| Quick brief | enough high-quality sources support 5-8 findings |
| Standard brief | 20-50 raw sources or diminishing returns after dedupe |
| Deep research | major source classes covered and contradictions checked |
| Trending research | paper/topic clusters stabilize across arXiv + metadata/code/discussion signals |
| Product/business scan | official pages + discovery signals + at least one caveat/competitor angle |

## Language policy

- Final output should be English by default.
- Chinese/non-English sources are allowed and useful.
- Translate source titles, claims, and summaries into English.
- Keep original names, product terms, paper titles, and quoted phrases when translation may lose meaning.
- If a translation is uncertain, mark it briefly instead of pretending certainty.

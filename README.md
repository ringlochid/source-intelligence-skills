# Source Intelligence Skills

Karpathy-style source gathering, validation, briefing, visual, watchlist, and artifact skills.

Canonical flow:

```text
source-router → source plan → 1-N source-* collectors → source-briefing
```

Optional steps:

```text
source-watchlist  # curated recurring/custom source lists
source-visual     # image-first visual read when visual evidence matters
source-artifact   # Markdown-first files when save/report/handoff is requested
```

## Public skills

- `source-router` — route intent, effort tier, and source plan.
- `source-topic` — topic/RSS/feed-style monitoring.
- `source-breaking` — breaking/current events.
- `source-tech` — AI/tech/builder ecosystem.
- `source-research` — papers and trending research scans.
- `source-github` — GitHub/repo/release trends.
- `source-product` — product/marketing/business/competitor scans.
- `source-market` — finance/BTC/market sources.
- `source-social-signal` — weak social/community signal only.
- `source-watchlist` — lightweight Markdown watchlists for recurring/custom sources.
- `source-briefing` — dedupe, validation, citations, confidence, and final output.
- `source-visual` — image-first visual reads.
- `source-artifact` — Markdown-first source packs for report/save/handoff/archive requests.

`source-common/` is shared support only and intentionally has no `SKILL.md`.

## Workflow lock

Every source skill follows:

```text
question → scope → source plan → gather → quality-rank → cross-check → cite → stop
```

Rules:

- Use one collector for simple asks; use multiple only when the request spans domains or needs stronger evidence.
- Always finish with `source-briefing` unless the user asked for raw links only.
- Use `source-artifact` only when files are requested.
- Use `source-visual` only when visual evidence/output matters.
- Social/community sources are weak signal until verified elsewhere.
- Output is English-first unless the user asks otherwise.

Validate:

```bash
python3 source-common/scripts/validate_source_bundle.py
```

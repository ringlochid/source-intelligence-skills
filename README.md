# Source Intelligence Skills

A compact OpenClaw skill bundle for source gathering, news/research/product intelligence, validation, readable brief generation, optional real visual assets, and Markdown-first artifacts.

Canonical flow:

```text
source-router → source plan → 1-N source-* collectors → source-briefing
```

Optional steps:

```text
source-watchlist       # curated recurring/custom source lists
source-visual     # image-first visual read when explicitly requested or image evidence matters
source-artifact        # Markdown-first files only when save/report/handoff is requested
```

## Public skills

- `source-router` — route intent, effort tier, and source plan.
- `source-watchlist` — lightweight Markdown watchlists for recurring/custom sources.
- `source-breaking` — breaking/current events.
- `source-topic` — topic/RSS/feed-style monitoring.
- `source-tech` — AI/tech/builder ecosystem.
- `source-research` — papers and trending research scans.
- `source-github` — GitHub/repo/release trends.
- `source-product` — product/marketing/business/competitor scans.
- `source-market` — finance/BTC/market sources.
- `source-social-signal` — X/social signal only.
- `source-briefing` — dedupe, validation, citations, confidence, and final output.
- `source-visual` — image-first visual reads: send image(s) with a one-sentence caption by default, not text-only analysis.
- `source-artifact` — Markdown-first source packs for report/save/handoff/archive requests.

## Rules

- Use one collector for simple asks; use multiple collectors when the request spans domains or needs stronger evidence.
- Always finish with `source-briefing` unless the user asked for raw links only.
- Use `source-artifact` only when files are requested.
- Use `source-visual` only for selected important sources where a visual read/image evidence matters; output image(s) first, one-sentence caption second.
- Output is English-first; Chinese/non-English sources are allowed and should be translated in the final brief unless requested otherwise.

## Effort tiers

- Quick: ~10-20 raw sources.
- Standard: ~20-50 raw sources.
- Deep: ~50-100+ raw sources and active contradiction checks.
- Watchlist: new/material changes only.

Output labels such as quick brief, deep research, product scan, marketing plan input, business opportunity scan, competitor scan, and optional real visual asset are examples chosen after source planning, not separate router branches.

## Telegram-readable brief pattern

Default chat briefs are readable text, not visual assets. Use the `source-briefing` pattern:

- top synthesis callout
- one quoted callout per important item
- vibe-matched icons when useful
- bullets for multi-point entries
- blank quoted line before labelled clickable source links
- no RED/AMBER severity labels unless the user asks for risk/incident triage
- real image/infographic/visual-asset output only when explicitly requested

## Artifact layout

```text
source-runs/YYYY-MM-DD-topic-slug/
├── brief.md
├── report-list.md
├── report.md              # optional
├── visual.md               # optional real visual asset prompt/spec
├── notes.md
└── references/
    ├── sources.md
    ├── citation-map.md
    └── rejected.md         # optional
```

Do not create JSON/JSONL unless automation/export is explicitly requested.

## Watchlists

Skill templates live in:

```text
source-watchlist/references/watchlists/
```

For Orin’s live workspace, use:

```text
/home/ubuntu/.openclaw/workspaces/orin/source-watchlists/
# includes ai-tech, research, product, market, social-signal, general-topics, sydney-life
```

# Source Intelligence Skills

Source Intelligence Skills is an OpenClaw skill bundle for turning messy research requests into scoped, cited, confidence-aware briefs.

It is built for questions where freshness and source quality matter: current events, product and market scans, technical releases, research papers, GitHub activity, social signal, watchlists, and handoff-ready source packs.

## What it can do

- Route a broad research request into the right source lane and effort level.
- Gather evidence from web, official docs, papers, GitHub, market data, product pages, and monitored sources.
- Separate verified facts from weak signal, speculation, and missing evidence.
- Produce concise briefs with citations, timestamps, caveats, and confidence.
- Save Markdown source packs when a report, archive, or handoff is requested.

## Core workflow

```text
question
  → scope and source plan
  → one or more source collectors
  → quality ranking and cross-checks
  → source-briefing
  → cited answer or artifact
```

The default is intentionally conservative: gather enough evidence to answer well, then stop. Social/community sources are useful for leads and sentiment, but they are not treated as proof until verified elsewhere.

## Skills map

| Need | Skill |
|---|---|
| Decide the right source path | `source-router` |
| Topic, RSS, blogs, newsletters, watch pages | `source-topic` |
| Breaking/current events | `source-breaking` |
| AI, tech, startup, builder ecosystem | `source-tech` |
| Papers and literature scans | `source-research` |
| GitHub repos, releases, issues, libraries | `source-github` |
| Product, launch, pricing, competitor scans | `source-product` |
| Finance, BTC, crypto, market/company sources | `source-market` |
| Weak social/community signal | `source-social-signal` |
| Recurring monitored source lists | `source-watchlist` |
| Final synthesis with citations and confidence | `source-briefing` |
| Image-first visual evidence reads | `source-visual` |
| Saved Markdown source packs | `source-artifact` |

`source-common/` contains shared references and validation logic. It is not an installable skill.

## Design philosophy

- **Source quality before volume.** A smaller set of better sources beats a pile of links.
- **Primary sources first.** Official docs, filings, papers, repos, and direct announcements are preferred when available.
- **Freshness is explicit.** Current or unstable claims should carry dates and caveats.
- **Signals are labeled.** Social traction, rumors, and community chatter stay clearly separated from verified facts.
- **Artifacts are deliberate.** Files are created only when the user asks for a saved report, source pack, archive, or handoff.

## Example requests

- “Find the strongest sources on the latest OpenAI API changes and summarize what changed.”
- “Track these five AI repos and brief me on meaningful releases every week.”
- “Research competitors for a lightweight student planning app; cite pricing, positioning, and launch notes.”
- “Turn this research into a Markdown source pack I can hand to another agent.”

## Validation

Run from the bundle root:

```bash
python3 source-common/scripts/validate_source_bundle.py
```

Expected shape: 13 public skills plus `source-common/` shared support.

## Installation notes

Copy the public skill directories plus `source-common/` into the active OpenClaw skills path. Do not copy scratch research outputs, archives, or unrelated community references into the installable bundle.

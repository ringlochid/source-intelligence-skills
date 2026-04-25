---
name: source-research
description: Gather research papers and literature sources. Use arXiv as the primary pattern, preserving exact IDs, authors, dates, links, abstracts, and paper claims. Route to source-briefing for research briefs or literature scans.
---

# Source Research

Use for papers, research updates, arXiv scans, and literature/source maps.

## Source pattern

Use arXiv metadata and paper pages/PDFs first. For broader trending research discovery, combine arXiv + Semantic Scholar/OpenAlex-style metadata + OpenReview/conference pages + Papers with Code where relevant.


## Reference links

Use these for trending research discovery and verification:

- arXiv API: https://info.arxiv.org/help/api/index.html
- arXiv search: https://arxiv.org/search/
- Semantic Scholar API: https://api.semanticscholar.org/api-docs/
- OpenAlex API: https://docs.openalex.org/
- OpenReview API/docs: https://docs.openreview.net/
- Papers with Code: https://paperswithcode.com/

## Workflow

1. Search arXiv by query/category/author/date window.
2. Preserve title, authors, arXiv ID, submitted/updated date, URL, abstract, and categories.
3. Separate paper claims from your interpretation.
4. If important or ambiguous, inspect the PDF/method/results before strong conclusions.
5. Send source notes to `source-briefing`.

## Trending research pattern

Treat trending research like trending news: gather multiple signals, dedupe into paper/topic clusters, then brief the important shifts.

For "what research is trending?", combine the sources by job:

- **Freshness:** arXiv recent/search by category/query.
- **Scholarly graph:** Semantic Scholar or OpenAlex-style metadata for citations, references, related papers, authors, venues, and recency.
- **Venue signal:** OpenReview/conference pages for ICLR/NeurIPS/ICML-style accepted papers, reviews, and workshop activity.
- **Implementation/benchmark signal:** Papers with Code and GitHub for code, tasks, benchmarks, and replication/adoption.
- **Practitioner discussion:** HN/blogs/social only as adoption/discussion signal.

Trending research should output **research findings**, not a raw paper list. Cluster by problem, method, benchmark, dataset, lab, and toolchain.

Trend strength should consider recency, venue/source quality, citation/related-work graph, code availability, benchmark movement, replication, independent discussion, and contradictions. Do not rank by social virality alone.

### Suggested source roles

- **arXiv:** fastest canonical source for preprints and exact paper IDs.
- **Semantic Scholar:** best for paper relevance, citation graph, related papers, author context, and quick literature expansion.
- **OpenAlex:** best open bibliographic index for broad metadata, institutions, venues, topics, citation counts, and large-scale queries.
- **OpenReview:** best for ML conference/workshop context, reviews, decisions, and venue-specific paper discovery.
- **Papers with Code:** best for implementation/benchmark/task momentum.

## arXiv fallback / rate limits

If the arXiv API returns 429 or is slow, do not hammer it. Fall back to:

- arXiv web search pages
- direct `https://arxiv.org/abs/<id>` pages if IDs are known
- paper PDFs only for the small subset that needs deeper inspection
- reputable paper indexes only as discovery signals, with arXiv/conference page as the citation anchor when possible

A paper is a primary source for what it claims, not proof the claim is true.

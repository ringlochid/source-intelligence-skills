---
name: source-tech
description: Gather AI, tech, startup, and builder ecosystem sources. Use HN-style discovery plus official blogs, release notes, docs, repos, and papers for verification. Route to source-briefing.
---

# Source Tech

Use for AI/tech/builder news, research-to-product signals, tools, launches, and ecosystem movement.

## Source pattern

Use Hacker News/API-style discovery as a signal, then verify through official blogs, docs, changelogs, release notes, repos, papers, or company posts.


## Reference links

Use discovery sources as signal, then verify with official sources:

- Hacker News Firebase API: https://github.com/HackerNews/API
- HN Algolia Search API: https://hn.algolia.com/api
- GitHub Changelog: https://github.blog/changelog/
- GitHub Blog: https://github.blog/
- Google AI blog: https://blog.google/technology/ai/

## Workflow

1. Gather relevant HN/top/discussion items for the topic or time window.
2. Follow through to original sources, not just comments.
3. For model/tool/company claims, prefer official release notes/docs/repos.
4. Keep HN comments as sentiment/adoption signal only.
5. Send source notes to `source-briefing`.

## HN fallback pattern

If no richer HN helper is available, use the public Firebase API pattern:

- Top stories: `https://hacker-news.firebaseio.com/v0/topstories.json`
- New stories: `https://hacker-news.firebaseio.com/v0/newstories.json`
- Item: `https://hacker-news.firebaseio.com/v0/item/<id>.json`

For topic-specific runs, use HN as discovery only: search the web for `site:news.ycombinator.com <topic>` or inspect candidate item URLs, then verify through the original source.

HN popularity means attention, not correctness.

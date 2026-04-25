---
name: source-github
description: Gather GitHub/repo trends, releases, libraries, and builder signals. Use GitHub search/API/trending-style discovery; verify with repo metadata, releases, commits, issues, and docs. Route to source-briefing.
---

# Source GitHub

Use for repo trends, new libraries, releases, and builder signals.

## Source pattern

Use GitHub API/search and repository pages. For GitHub product/platform changes, GitHub Changelog and official GitHub Blog pages count as primary sources.


## Reference links

Use GitHub official pages as primary sources for GitHub/repo facts:

- GitHub REST API: https://docs.github.com/en/rest
- GitHub Search API: https://docs.github.com/en/rest/search/search
- GitHub Releases API: https://docs.github.com/en/rest/releases/releases
- GitHub Changelog: https://github.blog/changelog/
- GitHub Blog: https://github.blog/

## Workflow

1. Search repos/releases/issues by topic, language, date, or entity.
2. Preserve repo full name, URL, stars/forks if available, latest release/date, license, and activity signals.
3. Prefer release notes, README, docs, source, GitHub Changelog, and official GitHub Blog over third-party summaries.
4. Treat stars/trending as attention, not quality.
5. Send source notes to `source-briefing`.

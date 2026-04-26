#!/usr/bin/env python3
from pathlib import Path
import re, sys

root = Path(__file__).resolve().parents[2]
refs_dir = root / 'source-common' / 'references'
errors = []

EXPECTED_SKILLS = {
    'source-artifact', 'source-breaking', 'source-briefing', 'source-github',
    'source-market', 'source-product', 'source-research', 'source-router',
    'source-social-signal', 'source-tech', 'source-topic', 'source-visual',
    'source-watchlist',
}
COLLECTORS = {'source-breaking','source-topic','source-tech','source-research','source-github','source-product','source-market','source-social-signal'}
EXPECTED_REFS = {
    'source-router': {'research-contract.md','safety-boundaries.md','routing-matrix.md','router-cheat-sheet.md'},
    'source-briefing': {'research-contract.md','safety-boundaries.md','source-quality-ladder.md','citation-and-timestamp-rules.md','claim-verification-loop.md','output-shapes.md','chat-brief-style.md'},
    'source-watchlist': {'research-contract.md','safety-boundaries.md','watchlist-state-rules.md'},
    'source-visual': {'research-contract.md','safety-boundaries.md','visual-evidence-rules.md'},
    'source-artifact': {'research-contract.md','safety-boundaries.md','output-shapes.md','citation-and-timestamp-rules.md'},
}
for skill in COLLECTORS:
    EXPECTED_REFS[skill] = {'research-contract.md','safety-boundaries.md','source-quality-ladder.md','citation-and-timestamp-rules.md','stop-rules.md'}
if 'source-research' in EXPECTED_REFS:
    EXPECTED_REFS['source-research'].add('claim-verification-loop.md')
if 'source-topic' in EXPECTED_REFS:
    EXPECTED_REFS['source-topic'].add('watchlist-state-rules.md')

REQUIRED_REFS = set().union(*EXPECTED_REFS.values())
MAX_SKILLS = 13
MAX_REFS = 12
MAX_SKILL_LINES = 48
MAX_REFS_PER_SKILL = 7
MAX_REF_WORDS = 280
MAX_TOTAL_MD_WORDS = 5200
OUTPUT_REQUIRED = {'citation', 'missing evidence'}


def is_archived(path: Path) -> bool:
    return any(part.startswith('_archive') for part in path.parts)


def parse_frontmatter(text, skill_name):
    if not text.startswith('---\n'):
        errors.append(f'{skill_name}/SKILL.md missing frontmatter')
        return {}
    parts = text.split('---\n', 2)
    if len(parts) < 3:
        errors.append(f'{skill_name}/SKILL.md malformed frontmatter')
        return {}
    data = {}
    for line in parts[1].splitlines():
        if ':' not in line:
            errors.append(f'{skill_name}/SKILL.md invalid frontmatter line: {line}')
            continue
        key, value = line.split(':', 1)
        data[key.strip()] = value.strip().strip('"')
    return data


def output_block(text: str) -> str:
    m = re.search(r'(?im)^Output:\s*$', text)
    if not m:
        return ''
    rest = text[m.end():]
    next_heading = re.search(r'(?m)^#{1,6}\s+', rest)
    return rest[:next_heading.start()] if next_heading else rest


def read_first_block(text: str) -> str:
    m = re.search(r'(?im)^Read first:\s*$', text)
    if not m:
        return ''
    block_lines = []
    started = False
    for line in text[m.end():].splitlines():
        if not started and not line.strip():
            continue
        if not line.strip():
            break
        started = True
        block_lines.append(line)
    return '\n'.join(block_lines)


def md_refs(text: str) -> set[str]:
    refs = set(re.findall(r'`([^`]+\.md)`', text))
    refs.update(re.findall(r'\[[^\]]+\]\(([^)\s]+\.md)\)', text))
    refs.update(re.findall(r'(?<![\w`(])(\.\./[^\s`)]+\.md)', text))
    return refs


def common_ref_basename(link: str) -> str | None:
    prefix = '../source-common/references/'
    if not link.startswith(prefix):
        return None
    ref = link[len(prefix):]
    if '/' in ref or '\\' in ref or '..' in ref or ref != Path(ref).name:
        return None
    return ref

skill_dirs = [p for p in sorted(root.iterdir()) if p.is_dir() and (p/'SKILL.md').exists()]
skill_names = {p.name for p in skill_dirs}
if skill_names != EXPECTED_SKILLS:
    errors.append(f'skill set mismatch: missing={sorted(EXPECTED_SKILLS-skill_names)} extra={sorted(skill_names-EXPECTED_SKILLS)}')
if len(skill_dirs) > MAX_SKILLS:
    errors.append(f'too many skills: {len(skill_dirs)} > {MAX_SKILLS}')
if (root/'source-common'/'SKILL.md').exists():
    errors.append('source-common must not contain SKILL.md')

all_refs = sorted(refs_dir.glob('*.md'))
ref_names = {p.name for p in all_refs}
if not REQUIRED_REFS.issubset(ref_names):
    errors.append(f'missing required refs: {sorted(REQUIRED_REFS-ref_names)}')
if len(all_refs) > MAX_REFS:
    errors.append(f'too many references: {len(all_refs)} > {MAX_REFS}')

for skill in skill_dirs:
    path = skill / 'SKILL.md'
    text = path.read_text()
    lower = text.lower()
    lines = text.splitlines()
    fm = parse_frontmatter(text, skill.name)
    if fm.get('name') != skill.name:
        errors.append(f'{skill.name}/SKILL.md name mismatch')
    if not fm.get('description'):
        errors.append(f'{skill.name}/SKILL.md missing non-empty description')
    elif len(fm['description'].split()) > 28:
        errors.append(f'{skill.name}/SKILL.md description too long: {len(fm["description"].split())} words')
    if len(lines) > MAX_SKILL_LINES:
        errors.append(f'{skill.name}/SKILL.md too long: {len(lines)} lines')
    for section in ('read first:', 'workflow:', 'output:'):
        if section not in lower:
            errors.append(f'{skill.name}/SKILL.md missing {section}')

    all_md_links = md_refs(text)
    for link in all_md_links:
        if common_ref_basename(link) is None:
            errors.append(f'{skill.name}/SKILL.md invalid markdown ref outside source-common: {link}')

    read_first = read_first_block(text)
    read_first_links = md_refs(read_first)
    outside_read_first = text.replace(read_first, '', 1)
    for link in md_refs(outside_read_first):
        if common_ref_basename(link) is not None:
            errors.append(f'{skill.name}/SKILL.md common ref outside Read first: {link}')

    refs = set()
    for link in read_first_links:
        ref = common_ref_basename(link)
        if ref is None:
            errors.append(f'{skill.name}/SKILL.md invalid ref path {link}')
            continue
        refs.add(ref)
    expected = EXPECTED_REFS.get(skill.name)
    if expected is None:
        errors.append(f'{skill.name}/SKILL.md has no expected ref contract')
        continue
    if refs != expected:
        errors.append(f'{skill.name}/SKILL.md Read first refs mismatch: missing={sorted(expected-refs)} extra={sorted(refs-expected)}')
    if len(refs) > MAX_REFS_PER_SKILL:
        errors.append(f'{skill.name}/SKILL.md references too many refs: {len(refs)} > {MAX_REFS_PER_SKILL}')
    for ref in refs:
        if not (refs_dir / ref).exists():
            errors.append(f'{skill.name} references missing {ref}')

    out = output_block(text).lower()
    for term in OUTPUT_REQUIRED:
        if term not in out:
            errors.append(f'{skill.name}/SKILL.md Output block missing {term}')

# Semantic sentinel checks in common refs / critical leaves.
sentinels = {
    refs_dir/'safety-boundaries.md': ['logged-in', 'private', 'pii', 'external writes', 'scraping', 'investment advice'],
    refs_dir/'source-quality-ladder.md': ['social', 'signal', 'not quality proof'],
    refs_dir/'visual-evidence-rules.md': ['generated/editorial images are presentation, not evidence'],
    refs_dir/'citation-and-timestamp-rules.md': ['publish/update time', 'multilingual'],
    refs_dir/'claim-verification-loop.md': ['counter-evidence'],
    root/'source-social-signal'/'SKILL.md': ['signal, not proof', 'verify factual claims'],
    root/'source-market'/'SKILL.md': ['verify price/market data separately'],
}
for path, terms in sentinels.items():
    hay = path.read_text(errors='ignore').lower()
    for term in terms:
        if term.lower() not in hay:
            errors.append(f'{path.relative_to(root)} missing sentinel phrase: {term}')

for ref in all_refs:
    text = ref.read_text()
    if not text.strip():
        errors.append(f'empty reference: {ref.name}')
    if not text.lstrip().startswith('#'):
        errors.append(f'{ref.name} missing top-level heading')
    words=len(text.split())
    if words > MAX_REF_WORDS:
        errors.append(f'{ref.name} too long: {words} words > {MAX_REF_WORDS}')

# No orphan non-archived router references.
for p in (root/'source-router'/'references').glob('*.md'):
    if not is_archived(p.relative_to(root)):
        errors.append(f'orphan router reference should be archived or linked: {p}')

word_count = sum(len(p.read_text(errors='ignore').split()) for p in root.rglob('*.md') if '.git' not in p.parts and not is_archived(p.relative_to(root)) and not p.name.endswith('summary-2026-04-26.md'))
if word_count > MAX_TOTAL_MD_WORDS:
    errors.append(f'total markdown word count too high: {word_count} > {MAX_TOTAL_MD_WORDS}')

if errors:
    print('FAIL')
    for e in errors:
        print('-', e)
    sys.exit(1)
print(f'OK: {len(skill_dirs)} skills, {len(all_refs)} references, {word_count} markdown words')

#!/usr/bin/env python3
"""Build/check the readable 250-topic map from canonical JSON, without network."""
from __future__ import annotations
import argparse
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]


def render_map(root: Path = ROOT) -> str:
    data=json.loads((root/'docs/topic-map.json').read_text(encoding='utf-8'))
    entries=data['topics']
    if [r['id'] for r in entries] != list(range(1,251)):
        raise ValueError('Original topic IDs must be exactly 1..250 in order')
    lines=['# The original 250 topics — applicability map', '', data['purpose'], '',
           '**Not an official OWASP control mapping and not 250 required technologies.**', '',
           'The authoring environment could not verify live institutional/vendor sources. '
           'Use [the source catalog](../shared/sources.md) with verified editions during a real review.', '',
           '## Categories', '']
    for key, meaning in data['categories'].items():
        count=sum(e['category']==key for e in entries)
        lines.append(f'- **{key} ({count})**: {meaning}')
    lines += ['', '## Complete routing table', '',
              '| # | Original topic | Applicability | Primary skill | Review criterion |',
              '| --- | --- | --- | --- | --- |']
    for r in entries:
        if r['category'] not in data['categories'] or not (root/'skills'/r['skill']/'SKILL.md').is_file():
            raise ValueError('Unknown topic category or primary skill')
        vals=[str(r['id']),r['topic'],r['category'],r['skill'],r['criterion']]
        if any('\n' in v or '|' in v for v in vals):
            raise ValueError('Topic fields cannot contain newlines or pipe delimiters')
        link=f"[{r['skill']}](../skills/{r['skill']}/SKILL.md)"
        lines.append(f"| {r['id']} | {r['topic']} | {r['category']} | {link} | {r['criterion']} |")
    lines += ['', 'Item 250 is interpreted as full coverage of large/truncated diffs, not permission to '
              'skip files after a maximum line count. Record missing ranges and recover source when possible.', '',
              'See [supplemental controls](additional-controls.md) for browser/API requirements and other '
              'web surfaces added beyond the original list. Security impact requires actual evidence; '
              'classification here is only a routing decision.', '']
    return '\n'.join(lines)


def main() -> int:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--apply',action='store_true',help='Write the derived Markdown; default checks it')
    args=parser.parse_args()
    text=render_map()
    path=ROOT/'docs/topic-map.md'
    if path.is_symlink():
        raise ValueError('Refusing symlink topic-map destination')
    if args.apply:
        path.write_text(text,encoding='utf-8')
    if not path.is_file() or path.read_text(encoding='utf-8') != text:
        print('Topic map is stale; run this script with --apply')
        return 1
    print('All 250 topic IDs and generated routing rows are consistent')
    return 0


if __name__=='__main__':
    try:
        raise SystemExit(main())
    except (OSError, ValueError, KeyError, TypeError) as exc:
        raise SystemExit(f'Topic-map check failed: {exc}')

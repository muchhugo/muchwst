#!/usr/bin/env python3
"""Check local skill packaging, references, shared copies and topic-map consistency."""
from __future__ import annotations
import ast
import json
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit
import sys
from build_topic_map import render_map
from sync_shared import drift

ROOT=Path(__file__).resolve().parents[1]
EXPECTED={'muchwst','muchwst-fix','muchwst-data',
          'muchwst-supply-chain','muchwst-vps','muchwst-cloudflare',
          'muchwst-runtime','muchwst-ai'}


def metadata(path: Path) -> dict[str,str]:
    text=path.read_text(encoding='utf-8')
    match=re.match(r'\A---\n(.*?)\n---\n',text,re.S)
    if not match:
        raise ValueError('Missing frontmatter')
    fields={}
    for line in match.group(1).splitlines():
        key,sep,value=line.partition(':')
        if not sep or key in fields:
            raise ValueError('Invalid or duplicate metadata key')
        value=value.strip()
        if value.startswith('"'):
            value=json.loads(value)
        if not isinstance(value,str):
            raise ValueError('Metadata values must be strings')
        fields[key]=value
    if set(fields)!={'name','description'}:
        raise ValueError('Expected name and description frontmatter only')
    if fields['name']!=path.parent.name or not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*',fields['name']):
        raise ValueError('Skill name must match its directory')
    if not 1<=len(fields['description'])<=1024:
        raise ValueError('Description length outside package policy')
    return fields


def prose_only(text: str) -> str:
    lines=[]
    fence=None
    for line in text.splitlines():
        match=re.match(r'^\s*(`{3,}|~{3,})',line)
        if match:
            token=match.group(1)
            if fence is None:
                fence=token
            elif token[0]==fence[0] and len(token)>=len(fence):
                fence=None
            continue
        if fence is None:
            lines.append(line)
    return '\n'.join(lines)


def validate(root: Path=ROOT) -> dict[str,int]:
    skills=sorted((root/'skills').glob('*/SKILL.md'))
    if {p.parent.name for p in skills}!=EXPECTED:
        raise ValueError('Expected exactly the eight documented skill folders')
    for path in skills:
        metadata(path)
        text=path.read_text(encoding='utf-8')
        for required in ('references/safety.md','references/evidence-and-reporting.md','templates/report.md','templates/finding.md'):
            if required not in text:
                raise ValueError(f'{path.relative_to(root)}: missing required safety/report route')
    if drift(root):
        raise ValueError('Shared distribution files differ from canonical sources')
    if (root/'docs/topic-map.md').read_text(encoding='utf-8')!=render_map(root):
        raise ValueError('Generated topic-map Markdown is stale')
    paths=[p for p in root.rglob('*') if '.git' not in p.parts and '__pycache__' not in p.parts]
    if any(p.is_symlink() for p in paths):
        raise ValueError('Distribution must not contain symlinks')
    md_files=[p for p in paths if p.is_file() and p.suffix=='.md']
    link_count=0
    for path in md_files:
        text=prose_only(path.read_text(encoding='utf-8'))
        for target in re.findall(r'\[[^\]]*\]\(([^\s)]+)\)',text):
            parsed=urlsplit(target)
            if parsed.scheme or target.startswith('#'):
                continue
            candidate=(path.parent/unquote(parsed.path)).resolve()
            if not candidate.is_relative_to(root.resolve()) or not candidate.exists():
                raise ValueError(f'{path.relative_to(root)}: broken/outside relative target {target}')
            if path.is_relative_to(root/'skills'):
                unit=root/'skills'/path.relative_to(root/'skills').parts[0]
                if not candidate.is_relative_to(unit.resolve()):
                    raise ValueError(f'{path.relative_to(root)}: link leaves its portable skill')
            link_count+=1
    for path in paths:
        if path.is_file() and path.suffix=='.py':
            ast.parse(path.read_text(encoding='utf-8'),filename=str(path))
        if path.is_file() and path.suffix=='.json':
            json.loads(path.read_text(encoding='utf-8'))
    return {'skills':len(skills),'topics':250,'markdown_files':len(md_files),'relative_links':link_count,
            'files':sum(p.is_file() for p in paths)}


def main() -> int:
    result=validate()
    for label,count in result.items():
        print(f'{label}: {count}')
    print('PASS: metadata, internal file references, self-contained skills, shared copies, JSON/Python syntax and topic map')
    print('Not checked: live external links/advisories, host-agent discovery or security effectiveness against an application')
    return 0


if __name__=='__main__':
    try:
        raise SystemExit(main())
    except (OSError,ValueError,KeyError,TypeError,SyntaxError) as exc:
        print(f'Pack validation failed: {exc}',file=sys.stderr)
        raise SystemExit(1)

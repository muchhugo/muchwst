#!/usr/bin/env python3
"""Check or refresh generated shared files in each portable skill (no network)."""
from __future__ import annotations
import argparse
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]


def expected_copies(root: Path = ROOT):
    for folder in sorted((root / 'skills').iterdir()):
        if not folder.is_dir() or not (folder / 'SKILL.md').is_file():
            continue
        for name in ('safety.md', 'evidence-and-reporting.md', 'sources.md', 'report.schema.json'):
            yield root / 'shared' / name, folder / 'references' / name
        for template in sorted((root / 'shared' / 'templates').glob('*.md')):
            yield template, folder / 'templates' / template.name


def drift(root: Path = ROOT) -> list[Path]:
    return [dst for src, dst in expected_copies(root)
            if not dst.is_file() or dst.is_symlink() or dst.read_bytes() != src.read_bytes()]


def synchronize(root: Path = ROOT) -> int:
    changed = 0
    for src, dst in expected_copies(root):
        for item in (src, dst, dst.parent, dst.parent.parent):
            if item.is_symlink():
                raise ValueError('Refusing symlink in a shared distribution path')
        if not dst.exists() or dst.read_bytes() != src.read_bytes():
            dst.parent.mkdir(parents=True, exist_ok=True)
            dst.write_bytes(src.read_bytes())
            changed += 1
    return changed


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--apply', action='store_true', help='Write generated copies; default only checks')
    args = parser.parse_args()
    if args.apply:
        print(f'Updated {synchronize()} generated shared files')
    missing = drift()
    if missing:
        for path in missing:
            print('Out of sync:', path.relative_to(ROOT))
        return 1
    print('Shared distribution copies match canonical files')
    return 0


if __name__ == '__main__':
    try:
        raise SystemExit(main())
    except (OSError, ValueError) as exc:
        raise SystemExit(f'Shared-copy check failed: {exc}')

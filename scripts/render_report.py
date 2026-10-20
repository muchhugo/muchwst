#!/usr/bin/env python3
"""Validate a toolkit JSON report and render private offline Markdown/HTML copies.

This validates this repository's deliberately limited schema vocabulary and selected
lifecycle consistency. It is not a generic JSON Schema engine, a CVSS calculator,
a secret scanner, or an assessment of the truth of supplied evidence.
"""
from __future__ import annotations
import argparse
from collections import Counter
from datetime import date
import html
import json
import math
import os
from pathlib import Path
import re
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
MAX_INPUT_BYTES = 5 * 1024 * 1024


class ReportError(ValueError):
    """Invalid report or unsafe output request; messages do not quote evidence."""


def _validate(value: Any, rule: dict[str, Any], path: str = '$', depth: int = 0) -> None:
    if depth > 60:
        raise ReportError('Report nesting exceeds the allowed depth')
    supported = {'$schema', 'title', 'type', 'properties', 'required', 'additionalProperties',
                 'items', 'enum', 'minLength', 'minimum', 'maximum', 'minItems'}
    if set(rule) - supported:
        raise ReportError('Toolkit schema uses an unsupported validator keyword')
    kind = rule.get('type')
    matches = {
        'object': isinstance(value, dict), 'array': isinstance(value, list),
        'string': isinstance(value, str), 'boolean': type(value) is bool,
        'number': type(value) in (int, float), 'integer': type(value) is int,
    }
    if kind not in matches or not matches[kind]:
        raise ReportError(f'{path}: wrong value type')
    if 'enum' in rule and value not in rule['enum']:
        raise ReportError(f'{path}: value is not in the allowed enumeration')
    if kind == 'object':
        props = rule['properties']
        if any(key not in value for key in rule.get('required', [])):
            raise ReportError(f'{path}: missing required field')
        if rule.get('additionalProperties') is False and set(value) - set(props):
            raise ReportError(f'{path}: unexpected field')
        for key, subrule in props.items():
            if key in value:
                _validate(value[key], subrule, path + '.' + key, depth + 1)
    elif kind == 'array':
        if len(value) < rule.get('minItems', 0):
            raise ReportError(f'{path}: too few items')
        for index, item in enumerate(value):
            _validate(item, rule['items'], f'{path}[{index}]', depth + 1)
    elif kind == 'string':
        if len(value) < rule.get('minLength', 0):
            raise ReportError(f'{path}: string is too short')
    elif kind in ('number', 'integer'):
        if isinstance(value, float) and not math.isfinite(value):
            raise ReportError(f'{path}: non-finite number')
        if 'minimum' in rule and value < rule['minimum']:
            raise ReportError(f'{path}: number below allowed range')
        if 'maximum' in rule and value > rule['maximum']:
            raise ReportError(f'{path}: number above allowed range')


def validate_report(report: Any) -> None:
    schema = json.loads((ROOT / 'shared/report.schema.json').read_text(encoding='utf-8'))
    _validate(report, schema)
    if report['example_only'] != (report['classification'] == 'synthetic-example'):
        raise ReportError('Example flag and report classification disagree')
    seen: set[str] = set()
    for index, finding in enumerate(report['findings']):
        locator = f'findings[{index}]'
        identifier = finding['id']
        if not re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9._-]{0,63}', identifier) or identifier in seen:
            raise ReportError(f'{locator}: invalid or duplicate finding ID')
        seen.add(identifier)
        if finding['kind'] == 'vulnerability' and finding['evidence_level'] == 'observation':
            raise ReportError(f'{locator}: a vulnerability needs a specified evidence level')
        if finding['evidence_level'].startswith('confirmed') and not finding['evidence']:
            raise ReportError(f'{locator}: confirmed evidence cannot be empty')
        if finding['evidence_level'] == 'confirmed-reproduction':
            if finding['reproduction']['status'] != 'executed' or not finding['reproduction']['steps']:
                raise ReportError(f'{locator}: confirmed reproduction needs executed steps')
        if finding['status'] == 'retest-passed':
            if not finding['retests'] or finding['retests'][-1]['result'] != 'passed':
                raise ReportError(f'{locator}: retest-passed needs a final passing retest record')
            last = finding['retests'][-1]
            if (last['revision'] != report['target']['head_revision'] or
                    last['configuration_revision'] != report['target']['configuration_revision']):
                raise ReportError(f'{locator}: final retest must identify the report target revision/config')
        if finding['status'] == 'accepted-risk':
            if 'risk_acceptance' not in finding:
                raise ReportError(f'{locator}: risk acceptance needs an owner and review record')
            try:
                date.fromisoformat(finding['risk_acceptance']['revisit_date'])
            except ValueError as exc:
                raise ReportError(f'{locator}: revisit date must be an ISO calendar date') from exc
        if finding['status'] in ('false-positive', 'not-applicable') and not finding.get('closure_reason'):
            raise ReportError(f'{locator}: closure needs a specific reason/counterevidence')
        if any(not mapping['verified'] for mapping in finding['mappings']):
            raise ReportError(f'{locator}: omit unverified control mappings; use source pointers instead')
        if 'cvss' in finding:
            cvss = finding['cvss']
            if not cvss['validated'] or not cvss['vector'].startswith('CVSS:' + cvss['version'] + '/'):
                raise ReportError(f'{locator}: CVSS needs a consistent version/vector and validation attestation')
            # The caller must independently verify the score/vector. Do not pretend to calculate it here.


def load_report(path: Path) -> dict[str, Any]:
    if not path.is_file() or path.stat().st_size > MAX_INPUT_BYTES:
        raise ReportError('Input must be a JSON file of at most 5 MiB')
    raw = path.read_bytes()
    if len(raw) > MAX_INPUT_BYTES:
        raise ReportError('Input exceeded 5 MiB while reading')
    try:
        report = json.loads(raw.decode('utf-8'))
    except (ValueError, UnicodeError, RecursionError) as exc:
        raise ReportError('Input is not valid bounded UTF-8 JSON') from exc
    validate_report(report)
    return report


def _bullets(items: list[str]) -> str:
    return '\n'.join('- ' + item for item in items) if items else 'None recorded.'


def _object_lines(item: dict[str, Any]) -> str:
    return '\n'.join(f'{key.replace("_", " ").capitalize()}: {value}' for key, value in item.items())


def _summary_counts(report: dict[str, Any]) -> str:
    confirmed = [f for f in report['findings'] if f['kind'] == 'vulnerability'
                 and f['evidence_level'].startswith('confirmed')
                 and f['status'] not in ('false-positive', 'not-applicable')]
    severity = Counter(f['severity'] for f in confirmed)
    suspected = sum(f['kind'] == 'vulnerability' and f['evidence_level'] == 'suspected'
                    and f['status'] not in ('false-positive', 'not-applicable')
                    for f in report['findings'])
    counts = ', '.join(f'{key}: {severity[key]}' for key in
                       ('critical', 'high', 'medium', 'low', 'informational'))
    statuses = ', '.join(f'{key}: {value}' for key, value in sorted(
        Counter(f['status'] for f in confirmed).items())) or 'None'
    return (f'Confirmed vulnerability records (including remediated history): {len(confirmed)}\n'
            f'{counts}\nConfirmed remediation states: {statuses}\n'
            f'Suspected vulnerability records: {suspected}\n'
            f'Other observations/closed false positives: {len(report["findings"])-len(confirmed)-suspected}\n'
            'Counts describe supplied records, not independently verified target truth.')


def sections(report: dict[str, Any]) -> list[tuple[int, str, str]]:
    result = [
        (2, 'Assessment', _object_lines({key: report[key] for key in
            ('assessment_id', 'classification', 'created_at', 'mode')})),
        (2, 'Target and revisions', _object_lines(report['target'])),
        (2, 'Summary', report['summary'] + '\n\n' + _summary_counts(report)),
        (2, 'Authorization and scope', '\n\n'.join(
            f'{key.replace("_", " ").capitalize()}\n' + (_bullets(value) if isinstance(value, list) else value)
            for key, value in report['scope'].items())),
        (2, 'Methods', _bullets(report['methods'])),
        (2, 'Tools actually executed', '\n\n'.join(_object_lines(t) for t in report['tools']) or 'None recorded.'),
        (2, 'Coverage and gaps', '\n\n'.join(_object_lines(c) for c in report['coverage']) or 'No coverage recorded.'),
    ]
    for f in report['findings']:
        result.append((2, f'{f["id"]} — {f["title"]}', _object_lines({key: f[key] for key in (
            'kind', 'severity', 'severity_reason', 'evidence_level', 'confidence', 'confidence_reason',
            'status', 'priority', 'priority_reason')})))
        result.append((3, 'Affected locations and prerequisites',
                       '\n\n'.join(_object_lines(l) for l in f['locations']) + '\n\n' + f['prerequisites']))
        for heading, key in [('Data flow', 'data_flow'), ('Counterevidence considered', 'counterevidence'),
                             ('Root cause', 'root_cause'), ('Impact', 'impact')]:
            result.append((3, heading, f[key]))
        result.append((3, 'Sanitized evidence', _bullets(f['evidence'])))
        reproduction = f['reproduction']
        reproduction_text = '\n\n'.join(
            f'{key.capitalize()}\n' + (_bullets(value) if isinstance(value, list) else value)
            for key, value in reproduction.items())
        result.append((3, 'Exploration and safe reproduction', reproduction_text))
        for heading, key in [('Root-cause correction', 'correction'), ('Mitigation (not a code fix)', 'mitigation'),
                             ('Compatibility and affected consumers', 'compatibility'),
                             ('Rollout and rollback', 'rollout_rollback')]:
            result.append((3, heading, f[key]))
        result.append((3, 'Regression tests', _bullets(f['regression_tests'])))
        result.append((3, 'Retest history', '\n\n'.join(_object_lines(r) for r in f['retests']) or 'No retest recorded.'))
        result.append((3, 'Verified mappings', '\n\n'.join(_object_lines(m) for m in f['mappings']) or 'Not mapped.'))
        for key in ('cvss', 'risk_acceptance', 'closure_reason'):
            if key in f:
                value = f[key]
                result.append((3, key.replace('_', ' ').capitalize(), _object_lines(value) if isinstance(value, dict) else value))
        result.append((3, 'Next action', f['next_action']))
    for title, key in [('Changes actually made', 'changes'), ('Limitations', 'limitations'),
                       ('Residual risk', 'residual_risks'), ('Next actions', 'next_actions')]:
        result.append((2, title, _bullets(report[key])))
    result.append((2, 'Assessment test records', '\n\n'.join(_object_lines(t) for t in report['tests']) or 'No tests recorded.'))
    result.append((2, 'Sources and freshness', '\n\n'.join(_object_lines(s) for s in report['sources']) or 'No sources recorded.'))
    result.append((2, 'Production changes', report['production_changes']))
    result.append((2, 'Persistence statement supplied by author', report['persistence']))
    return result


def _md_heading(text: str) -> str:
    # Headings are plain text, not a way to inject Markdown/HTML/images or links.
    text = text.replace('\r', ' ').replace('\n', ' ')
    return re.sub(r'([\\`*_{}\[\]()#+.!|<>~-])', r'\\\1', text)


def render_markdown(report: dict[str, Any]) -> str:
    validate_report(report)
    notice = ('SYNTHETIC EXAMPLE — no real target was assessed and the scenarios are fictional.'
              if report['example_only'] else 'CONFIDENTIAL — share only with authorized recipients.')
    lines = ['# ' + _md_heading(report['title']), '', '**' + notice + '**', '',
             'Generated offline from supplied records. Structure/status validation is not verification '
             'of evidence, severity, CVSS arithmetic or secret redaction.', '']
    for level, title, body in sections(report):
        # Evidence stays inert even if it contains markup, images or closing code fences.
        fence = '`' * max(3, 1 + max((len(m.group()) for m in re.finditer(r'`+', body)), default=0))
        lines += ['#' * level + ' ' + _md_heading(title), '', fence + 'text', body, fence, '']
    return '\n'.join(lines)


def render_html(report: dict[str, Any]) -> str:
    validate_report(report)
    title = html.escape(report['title'])
    notice = ('SYNTHETIC EXAMPLE — no real target was assessed; scenarios are fictional.'
              if report['example_only'] else 'CONFIDENTIAL — authorized recipients only.')
    chunks = []
    for level, heading, body in sections(report):
        chunks.append(f'<section><h{level}>{html.escape(heading)}</h{level}>'
                      f'<pre>{html.escape(body)}</pre></section>')
    return ('<!doctype html>\n<html lang="en"><head><meta charset="utf-8">'
            '<meta name="viewport" content="width=device-width,initial-scale=1">'
            '<meta http-equiv="Content-Security-Policy" content="default-src \'none\'; '
            'style-src \'unsafe-inline\'; base-uri \'none\'; form-action \'none\'">'
            '<meta name="referrer" content="no-referrer">'
            f'<title>{title}</title><style>'
            'body{font:16px/1.55 system-ui,sans-serif;max-width:1000px;margin:40px auto;padding:0 24px;color:#152537;background:#fff}'
            'h1{font-size:2.1rem;line-height:1.2}h2{margin-top:2.3rem;border-bottom:2px solid #dce3eb;padding-bottom:.4rem}'
            'h3{margin-top:1.6rem}pre{white-space:pre-wrap;overflow-wrap:anywhere;font:14px/1.6 ui-monospace,monospace;'
            'padding:16px;background:#f4f6f8;border:1px solid #dce3eb;border-radius:5px}'
            '.notice{padding:12px 16px;border-left:4px solid #9c4b00;background:#fff2df;font-weight:650}'
            '.subtle{font-size:.9rem;color:#40556b}@media print{body{margin:0;max-width:none;font-size:11pt}pre{font-size:9pt}'
            'h2,h3{break-after:avoid}section{break-inside:auto}.notice{background:none}}'
            '</style></head><body>' + f'<h1>{title}</h1><p class="notice">{html.escape(notice)}</p>'
            '<p class="subtle">Offline rendering. Supplied evidence, severity, CVSS arithmetic and '
            'secret redaction require human/agent review; no network or scripts are loaded.</p>' +
            ''.join(chunks) + '</body></html>\n')


def write_report(report: dict[str, Any], destination: Path) -> list[Path]:
    validate_report(report)
    if destination.exists() or destination.is_symlink():
        raise ReportError('Output directory already exists; choose a new private destination')
    if not destination.parent.is_dir():
        raise ReportError('Output parent must be an existing authorized directory')
    outputs = {
        'findings.json': json.dumps(report, ensure_ascii=False, indent=2) + '\n',
        'REPORT.md': render_markdown(report), 'REPORT.html': render_html(report),
    }
    try:
        destination.mkdir(mode=0o700, exist_ok=False)
    except FileExistsError as exc:
        raise ReportError('Output destination was created concurrently; nothing overwritten') from exc
    created: list[Path] = []
    try:
        for name, content in outputs.items():
            path = destination / name
            descriptor = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
            with os.fdopen(descriptor, 'w', encoding='utf-8', newline='\n') as handle:
                handle.write(content)
            created.append(path)
            if path.read_text(encoding='utf-8') != content:
                raise ReportError('Written report did not match on read-back')
    except OSError as exc:
        # Preserve any files already written; do not perform broad cleanup on a user destination.
        raise ReportError('Report write failed; inspect the new output directory for partial files') from exc
    return created


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input', type=Path, help='Authorized sanitized JSON report, at most 5 MiB')
    parser.add_argument('--output', type=Path, required=True, help='New private directory; never overwritten')
    args = parser.parse_args()
    report = load_report(args.input)
    created = write_report(report, args.output)
    print(f'Rendered and read back {len(created)} private report files; evidence truth not independently verified')
    for path in created:
        print(path)
    return 0


if __name__ == '__main__':
    try:
        raise SystemExit(main())
    except (ReportError, OSError, UnicodeError) as exc:
        raise SystemExit(f'Report generation failed: {exc}')

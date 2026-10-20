# Contributing

Inspect the current branch, revision and pending work, read AGENTS.md, and preserve others' changes. Propose material policy changes rather than silently weakening controls. Keep actual target secrets/findings out; examples must be synthetic and labeled.

## Files and sources of truth

`shared/` owns common policy, institutional source pointers, report schema and templates. `scripts/sync_shared.py --apply` copies these into each skill so a single skill is independently installable. Validation fails on drift. Maintain specialized checks inside their own skill's references; the main entry routes selectively, not by loading every reference for every small task.

`docs/topic-map.json` owns the original numbered 250-topic classification. Run `python3 scripts/build_topic_map.py --apply` after edits; `docs/topic-map.md` is derived. Do not renumber the user's list or equate conditional architecture/SRE topics with vulnerabilities. Supplemental requirements belong in docs/additional-controls.md and the relevant skill.

Source/version/mapping claims require actual evidence. Keep catalog pointers distinct from consulted references. Do not copy proprietary benchmark text or third-party implementations wholesale. This original kit is not affiliated with any named security project or institution.

## Local verification

From repository root, run:

```sh
python3 scripts/sync_shared.py --apply
python3 scripts/build_topic_map.py --apply
python3 scripts/validate_pack.py
python3 -m unittest discover -s tests -v
```

Python 3.10+ and standard library only; no installer/network/test target is needed. Report executed commands, results and untested compatibility. Inspect the diff and copied policy consistency. Tests cover packaging, JSON report structure/status rules, escaping and safe output behavior; they do not prove agent effectiveness, real vulnerabilities or current vendor settings.

## Git and release

Use cohesive Conventional Commits with English type/scope and a brief Brazilian Portuguese description, such as `feat(review): ampliar análise de respostas de API`. Do not create a commit per file/attempt or rewrite shared history. Apply the actual owner's branch/review/publication authorization; no fabricated reviewer or independent review claim. A build/validation record must identify its exact revision or candidate content manifest.

Only publish a GitHub location/commit after a successful remote action and read-back. A local ZIP is not a deployed or published repository. Do not add an arbitrary license grant on the owner's behalf; distribution licensing remains the owner's explicit decision.

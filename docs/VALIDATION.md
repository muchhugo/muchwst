# muchwst package verification

Verification date: 2026-10-19. This record describes the renamed muchwst candidate before its publication commit; WST stands for Web Security Toolkit. The final `MANIFEST.sha256` records the exact distributed file contents (excluding its own digest). Hashes provide consistency checks, not a signed provenance attestation.

## Executed checks

- Python 3.13.5: `python3 scripts/sync_shared.py --apply` synchronized the 64 generated common policy/schema/template files into eight independently portable skill directories.
- `python3 scripts/build_topic_map.py --apply` generated the complete 250-row table from canonical JSON. Categories: 43 core, 132 conditional, 49 supporting and 26 architectural/context topics. These are routing categories, not vulnerability counts.
- `python3 scripts/validate_pack.py` passed checks for skill name/description metadata, relative file references, self-contained skill folders, generated shared-copy consistency, topic IDs/order and JSON/Python syntax.
- `python3 -m unittest discover -s tests -v` passed **27 tests** covering report shape, selected status/evidence consistency, output escaping, non-overwriting output behavior, private POSIX file permissions and pack integrity.
- The installed `jsonschema` library's Draft 2020-12 validator accepted the schema and synthetic example. This was a separate local validation implementation, **not an independent reviewer**. The bundled scripts themselves use Python's standard library only.
- The report renderer created and read back JSON, Markdown and HTML for the clearly labeled synthetic example. No application code was executed and no fictional reproduction was represented as a real test.

## Not executed or verified

No target application security audit, real exploitation, penetration test, production scan, load/fuzz campaign, secret rotation, SSH/firewall change, Cloudflare configuration, dependency/security-tool installation or deployment occurred. No private target report was placed in this package.

No native discovery/installation or real workflow was runtime-tested inside Claude Code, Codex or another agent. The neutral Markdown/frontmatter layout and self-contained file references were checked; that does not guarantee agent obedience or detection quality. Python tests were run on 3.13.5, not every supported Python/OS combination.

Web search was unavailable. External reference links, current advisories/CVEs, latest institutional editions, exact OWASP requirement IDs, current Cloudflare features/plans and vendor compatibility were not remotely verified. The source catalog is explicitly marked as pointers, not consulted current research.

The renderer does not independently verify evidence truth, exploitability, author authorization, CVSS score arithmetic, legal compliance or complete secret redaction. It rejects selected inconsistent records and unsafe output reuse, but human/agent review remains necessary. No independent human security review or certification is claimed.

## Naming and publication

The owner selected `muchwst` (WST = Web Security Toolkit) and created `muchhugo/muchwst`. The main skill is `muchwst`; the seven focused skills use its prefix. Skill directory names, frontmatter, references, routing rows and validation expectations were updated together. All checks above were rerun on this renamed candidate, with 8 skills, 250 topics, 95 Markdown files, 384 internal references and 27 passing tests. The synthetic renderer outputs were regenerated in memory and compared byte-for-byte to the packaged examples; the JSON Schema was also checked again.

The original ZIP manifest was verified before editing. The new package is separate from `muchhugo/development-standards`, which was not modified. This record validates candidate file contents; successful remote publication requires a commit and read-back with matching Git tree hashes. Consult this repository's commit history for the publication revision, rather than treating this pre-commit note as a remote-write receipt.

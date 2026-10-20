# muchwst — Web Security Toolkit

**WST stands for Web Security Toolkit.** `muchwst` is the package name and its main skill.

**[Guia em português](docs/USAGE.pt-BR.md)** · **[Main skill](skills/muchwst/SKILL.md)** · **[250-topic classification](docs/topic-map.md)** · **[Report example](examples/synthetic-assessment/REPORT.md)**

Eight portable skills for evidence-based web application code review, safe security fixes and infrastructure hardening. Read the actual code and configuration, establish the trust boundary, produce a classified report, and retest a root-cause correction. This is a Markdown skill pack with optional offline report tools, **not a bundled autonomous scanner or a clone/installation of Strix**.

No framework, cloud provider, database, model or agent is required. The original `development-standards` repository remains separate; use its adopted local conventions when available, without making this pack depend on it.

## Skills

| Skill | Scope |
| --- | --- |
| [muchwst](skills/muchwst/SKILL.md) | Main workflow: code/PR coverage, threats, authentication/authorization, injection, browser storage, safe APIs, files, SSRF and real time |
| [muchwst-fix](skills/muchwst-fix/SKILL.md) | Verify a finding, correct its cause, preserve legitimate flows and report before/after retests |
| [muchwst-data](skills/muchwst-data/SKILL.md) | Tenant/RLS boundaries, transactions, monetary invariants, races, caches, replicas and jobs |
| [muchwst-supply-chain](skills/muchwst-supply-chain/SKILL.md) | Secrets, dependencies/advisories, package provenance, CI/CD, images and infrastructure state |
| [muchwst-vps](skills/muchwst-vps/SKILL.md) | SSH without lockout, actual exposed services, firewalls, proxies, patching, containers, logs and recovery |
| [muchwst-cloudflare](skills/muchwst-cloudflare/SKILL.md) | WAF and scanner abuse, route-specific bots/rate limits, TLS, origin protection, trusted headers and private caching |
| [muchwst-runtime](skills/muchwst-runtime/SKILL.md) | Resource abuse, streaming, bounded retries, observability, deployment/failure and recovery risks |
| [muchwst-ai](skills/muchwst-ai/SKILL.md) | AI/RAG/agent surfaces only: prompt injection, tool authorization, data isolation, model output and cost limits |

Each complete `skills/<name>/` directory is self-contained. `SKILL.md` is a short routing entry; read only the relevant references. Focused skills are optional workflows, **not a directive to launch eight agents in parallel**. The lead agent checks all delegated evidence and uses a proportionate cost/context budget.

## Modes and safeguards

**Review** is read-only. **Fix** changes the approved working copy when requested. **Verify** runs only authorized bounded tests. **Harden** plans environment-specific changes before an explicitly authorized live action. Owning a repository or installing a skill does not authorize scanning all referenced hosts, changing production, opening a firewall, rotating credentials or publishing private findings.

Never confuse a missing best practice with a proved vulnerability. Separate `vulnerability`, `hardening`, `reliability` and `governance`; severity, confidence, evidence and remediation status are independent. A code proof is valid evidence but not a claim of dynamic exploitation. A WAF mitigation does not fix a vulnerable application sink. Read [safety](shared/safety.md) and [evidence/reporting](shared/evidence-and-reporting.md).

## Always report

Every invocation produces a report, even with no findings or blocked access. Each finding includes severity and rationale, exact code/config location and revision, prerequisites, root cause and impact, sanitized evidence, how it was explored, safe reproduction with execution status, correction/mitigation, regression tests and retest status. Coverage explicitly records unread/truncated diff ranges and untested surfaces. No findings in reviewed scope is not a certificate that the application is secure.

For larger assessments, prefer private `REPORT.md` plus schema-checked `findings.json`. Optional HTML rendering is offline and escapes report content; no scripts, external assets or telemetry are included. **Reports from real targets never belong in this public toolkit.** The sample is labeled synthetic, not an assessment of a real project.

## Use with Claude Code, Codex or another agent

Use the host's documented local-skill loader for its **installed version**, or provide an authorized local checkout/connector and explicitly ask the agent to read `skills/muchwst/SKILL.md` and its linked references. Copy the whole selected skill directory, not just the entry point. Do not assume global paths, change user-wide settings, or overwrite existing skills without permission.

There is no host-specific API, model ID, automatic tool permission, external MCP requirement or executable install hook. Markdown/frontmatter and explicit-reading portability are intentional. **Native discovery/installation has not been runtime-tested in Claude Code, Codex or every agent.** File references do not automatically load themselves. See [usage](docs/USAGE.pt-BR.md) and [agent notes](docs/agent-integration.md).

## Browser and API rules

The main skill includes focused [browser storage](skills/muchwst/references/browser-storage.md) and [API contracts](skills/muchwst/references/api-contracts.md) references. They distinguish memory, cookies, local/session storage, IndexedDB and service-worker caches; opaque sessions, access/refresh tokens and JWT claims; CSRF and XSS; field-level response disclosure; validation, normalization, rich-content sanitization and context-correct output encoding. No rule says “every JWT must be a cookie” or “sanitize every string with one regex.”

## Institutions and currency

The [source catalog](shared/sources.md) points to OWASP ASVS/WSTG/Cheat Sheets/API Security, MITRE CWE, FIRST CVSS, NIST, CISA, CIS, SEI CERT and relevant primary vendor/specification material. **Live sources, current CVEs, newest standards editions and Cloudflare plan/features were not verified during authoring because web search was unavailable.** At assessment time verify and cite the applicable version; never invent requirement IDs or claim an institution endorsed this pack. The topic matrix is a routing aid, not official ASVS coverage or certification.

## Optional offline tooling

Python 3.10+ is used only for maintaining the pack and rendering a structured report; using the Markdown skills does not require Python. The scripts use the standard library and do not contact the network or scan targets.

```sh
# From this repository root:
python3 scripts/validate_pack.py
python3 -m unittest discover -s tests -v
python3 scripts/render_report.py examples/synthetic-assessment/findings.json   --output /tmp/muchwst-example-report
```

The renderer creates a **new** output directory and refuses to overwrite an existing one. It validates structure and selected status consistency, not the truth of a finding, CVSS mathematics or automatic secret redaction. Review/redact data and choose an authorized private output location before real use. Do not use the synthetic example as target evidence.

## Maintaining the pack

`shared/` is the editable source for safety, evidence, source catalog, report schema and common templates. Corresponding files inside each skill are **generated distribution copies** so skills remain portable on their own; do not edit copies independently. Run `python3 scripts/sync_shared.py --apply`, then validation/tests. In adoption, never copy a remote update over an approved target policy silently. Read [CONTRIBUTING.md](CONTRIBUTING.md) and [AGENTS.md](AGENTS.md).

The repository is [muchhugo/muchwst](https://github.com/muchhugo/muchwst). The publication commit and content manifest identify the delivered revision. No audit, host change, Cloudflare rule, security-tool installation or production action was executed by creating this kit.

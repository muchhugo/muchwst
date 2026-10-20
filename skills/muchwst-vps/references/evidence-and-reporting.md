# Evidence, severity and mandatory reporting

Every invocation ends with a report, including a review with zero findings, a failed reproduction, a blocked hardening change, or a documentation-only action. For a small task this may be a concise Markdown response. For a substantive assessment use the bundled report/finding templates and a machine-readable report when practical. No report destination authorization means a redacted response, not an unauthorized repository write.

## What qualifies as a finding

Trace **entry point → attacker-controlled input or identity → existing guards → sensitive operation/resource → observable impact**. Establish reachability, relevant configuration, required privileges, trust/tenant boundary and plausible impact. Include the exact revision and narrow code lines or configuration evidence. Inspect counterevidence: framework escaping, parameterization, shared middleware, database policy, upstream validation, deployment topology and downstream consumers. A regex match, scanner alert, missing library, missing header or theoretical best practice is not automatically an exploitable vulnerability.

Classify the **kind** separately: `vulnerability`, `hardening`, `reliability`, or `governance`. Never inflate a performance opportunity or compliance question into a confirmed security defect. Group instances sharing the same root cause while listing all evidenced affected paths; keep distinct causes separate.

Classify **evidence** separately: `confirmed-reproduction` (safe authorized test actually run), `confirmed-code` (complete code/config proof; exploitation was not run), or `suspected` (a material assumption remains). Hardening/governance observations may use `observation`. State confidence as `high`, `medium`, or `low` with a reason. Static proof can establish a defect without claiming dynamic exploitation. A failed reproduction does not prove a false positive when the environment, WAF or fixture prevents the path.

## Severity and priority

Use business impact, reachability, required privileges, victim interaction, confidentiality/integrity/availability, tenant spread, data sensitivity and compensating controls. These qualitative definitions are this toolkit's triage convention, not an automatic scanner score:

| Severity | Guidance, requiring contextual evidence |
| --- | --- |
| Critical | Credible broad compromise, severe unauthorized execution, systemic account/tenant takeover or comparably catastrophic impact with a realistic path |
| High | Serious unauthorized data access, privilege change, financial abuse or significant service compromise with supported preconditions |
| Medium | Material but constrained impact, limited scope or meaningful additional preconditions |
| Low | Limited security impact or a narrow weakness with substantial constraints |
| Informational | Observation or hardening opportunity without demonstrated harmful impact |

A missing CSP is not automatically High. An SQL sink is not automatically Critical without reachability/context. Performance/resource findings need an abuse/capacity path to be called a security vulnerability. Keep severity distinct from remediation priority: urgency can account for active exploitation evidence, exposure, business obligations and change risk.

CVSS is optional. If provided, name the exact version, include the complete vector and score, source/calculator and assumptions; validate their consistency. Otherwise use qualitative severity and explicitly omit CVSS. Never invent a CWE number, ASVS/WSTG requirement identifier, CVE, exploitation status, affected version or compliance certification. Verify exact mappings against a pinned source before labeling them; a general reference is acceptable.

## Per-finding report requirements

Use a stable ID and title; kind/severity and rationale; evidence/confidence and reason; remediation status; repository/revision and affected lines/endpoints; prerequisites and accounts/tenant roles; trust-boundary/root-cause narrative; impact and blast radius; minimal sanitized evidence; and exploit/reproduction details.

The reproduction must distinguish **what actually happened** from a proposed test: setup, owned identities, ordered steps or minimal request, expected secure behavior, observed behavior, execution status, and cleanup. Use placeholders for credentials and controlled hosts. Never claim a production breach from a local reproduction. When the issue was not exploited, write `Not dynamically reproduced` and supply the code proof and a proposed safe procedure.

Give the smallest root-cause fix, affected consumers, compatibility/migration risks, defense-in-depth alternatives, a regression test that fails before and passes after where executable, and deployment/rollback considerations. Document exploitation chains only when each link has evidence; never chain unrelated possibilities into an inflated Critical.

## Lifecycle and retesting

Use `open`, `mitigated`, `fixed-awaiting-retest`, `retest-passed`, `accepted-risk`, `false-positive`, or `not-applicable`. Keep remediation state independent of evidence and severity. A WAF rule can mitigate an application defect but does not make the application fixed. `accepted-risk` needs an authorized owner, reason and revisit date; an agent cannot accept risk for the user. Closing as `false-positive` requires specific counterevidence.

Retest the original path and relevant variants: permitted and forbidden roles, other tenants, alternate endpoints, error/failure handling, revocation, concurrency and cached/replicated state where applicable. Record the exact tested code revision, configuration revision and environment. A local pass is not proof of production deployment. Preserve the initial evidence and append results rather than erasing the original finding. A changed head/config requires reconsidering stale evidence.

The final report includes scope, methods/tools and their versions if executed, evidence sources, coverage with exclusions/gaps, prioritized findings, patches actually made, retests, residual risk and next action. Use `assessed`, `not-assessed`, `not-applicable` and `blocked` for coverage; never count an excluded or unread area as passed. Say **“No confirmed vulnerabilities found in the reviewed scope”**, not “the application is secure.” AI review, scanners and a checklist do not constitute certification, continuous monitoring or complete penetration testing.

## Output artifacts

Prefer a private `security-reports/<assessment-id>/` destination **only when authorized**, with `REPORT.md`, `findings.json`, a coverage ledger and minimal sanitized evidence. Avoid tracked public copies; `.gitignore` is only one layer, not protection for already tracked files. Read reports back after writing. The bundled JSON Schema defines the structured shape; a schema check validates structure, not truth or security.

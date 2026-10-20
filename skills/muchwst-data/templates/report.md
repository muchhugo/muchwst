# Security assessment report — template

CONFIDENTIAL TARGET REPORT. Do not commit an actual target report into the public toolkit. Replace/remove placeholders. For small tasks, use a concise report in the response with the same evidence distinctions.

## Summary

Assessment ID / report version: {{id_and_version}}
Target / repository / branch / revision / config revision: {{verified_identity}}
Environment and assessed period: {{actual_environment_and_times}}
Mode and authorized scope: {{review_fix_verify_or_harden_and_boundary}}
Overall result: {{what_was_actually_established}}

If no findings are confirmed, say “No confirmed vulnerabilities found in the reviewed scope.” Do not say the entire application is secure. Distinguish open, mitigated, patched and retested findings in counts. Count suspected vulnerabilities and non-vulnerability observations separately from confirmed vulnerabilities.

## Scope, methods and limits

Describe assets, entry points, roles/tenants and operations allowed; what was excluded; test-data/cost/request limits; target privacy and write boundaries. Record base/head and changed-file inventory for a diff review. Name tools, versions, commands and dates only when actually executed or verified. Separate source review, scanner leads, dynamic verification and walkthroughs.

## Coverage

| Surface / file / flow | Revision / ranges | Status | Method and evidence | Gap / reason |
| --- | --- | --- | --- | --- |
| {{scope_item}} | {{actual_revision_and_range}} | {{assessed_not-assessed_not-applicable_or_blocked}} | {{actual_method}} | {{remaining_gap}} |

An unread truncated diff, an inaccessible configuration or an unexecuted test is not an assessed/pass item. Link the full coverage ledger when the table would be too large. Reconcile moved revisions rather than silently reuse stale coverage.

## Threat model and relevant architecture

Summarize the actual actors, assets, trust boundaries, origin/edge/data/client topology and primary abuse goals. Link existing verified architecture. Do not invent infrastructure or insert a requirement for RLS, cache, sharding or microservices where none is justified.

## Prioritized findings

| ID | Title | Kind | Severity | Evidence / confidence | Remediation status | Priority |
| --- | --- | --- | --- | --- | --- | --- | --- |
| {{stable_id}} | {{finding_title}} | {{kind}} | {{severity}} | {{evidence_and_confidence}} | {{status}} | {{priority_and_reason}} |

Include the [finding record](finding.md) for each item. Explain score/priority assumptions, prerequisites and counterevidence. Do not publish actual secrets or unredacted customer data in proof requests/screenshots. Document proposed reproductions as unexecuted, not as attacks that occurred.

## Changes and retests

Describe patches/configuration actually changed, reviewed revision, before/after behavior, authorized local tests, allowed-flow tests and variants. Keep original evidence and append retests. A WAF mitigation is not a source fix; a local patch is not a production deployment. A runtime test passing behind a compensating control does not prove a vulnerable sink was removed.

## Residual risks and next actions

List high-priority unresolved items, uncertainty, blocked checks, rollout prerequisites, migration/revocation needs, rollback implications and proposed next actions. Risk acceptance requires an authorized owner, reason and revisit date. No automation, monitoring or future retest is claimed unless actually configured and authorized.

## Sources and provenance

For consulted institutional/vendor sources, record publisher, exact URL or local copy, version/edition, actual retrieval date and relevant section. Verify identifiers before mapping CWE/CVSS/ASVS/WSTG. List catalog-only pointers separately as not consulted. Repository lines, configuration and tests are the evidence for target-specific findings, not the presence of an OWASP URL.

## Persistence and disclosure

Destination and read-back status: {{authorized_private_path_and_actual_verification_or_no_write}}
Redaction check and report recipients/scope: {{actual_review}}
Production change status: {{unchanged_or_exact_authorized_actions_with_evidence}}

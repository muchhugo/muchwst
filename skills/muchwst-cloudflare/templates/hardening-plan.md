# Infrastructure hardening change — template

This is a proposed plan unless actual authorization and execution are recorded. Do not treat placeholders or this file as operator approval.

Target host / zone / account / environment: {{verified_scope}}
Owner, authorization and change boundary: {{actual_owner_and_approval}}
Observed current configuration / revision: {{redacted_evidence}}
Intended change and security invariant: {{exact_smallest_change}}
Vendor/OS/plan/version/syntax evidence: {{verified_sources_or_blocker}}

## Dependencies and recovery

Affected legitimate clients, APIs, webhooks, health checks, real-time paths, protocols, IPv4/IPv6 and subdomains: {{inventory}}
Protected administrative path and separately tested fresh access: {{evidence_or_not_ready}}
Provider console/rescue, credentials custody and recovery operator: {{confirmed_without_secret_values}}
Sanitized before-state, exact rollback steps and abort criteria: {{reviewed_plan}}
Maintenance/observation window and cost/request/resource bounds: {{approved_limits}}

## Ordered actions and checks

State the proposed minimal changes, configuration syntax validation, staged deployment/reload, bounded testing, false-positive monitoring and exact reversal. Do not flush existing rules, broadly bypass security, remove management access, enable HSTS preload or rotate live secrets by default. Record config IDs/revisions only when discovered, never invent them.

## Outcomes

Changes actually applied: {{none_or_exact_actions}}
Fresh management/application/legitimate integration tests: {{executed_results_or_gaps}}
Bad-path test and residual application defect status: {{mitigation_versus_fix}}
Effective configuration read-back: {{observed_or_unverified}}
Report/findings destination: {{authorized_private_destination_or_response}}

# {{stable_id}} — {{evidence_based_title}}

## Classification

Kind: {{vulnerability_hardening_reliability_or_governance}}
Severity and reason: {{critical_high_medium_low_or_informational_with_context}}
Evidence level: {{confirmed-reproduction_confirmed-code_suspected_or_observation}}
Confidence and reason: {{high_medium_or_low_and_remaining_assumptions}}
Remediation state: {{open_mitigated_fixed-awaiting-retest_retest-passed_accepted-risk_false-positive_or_not-applicable}}
Priority and reason: {{business_urgency_separate_from_severity}}
CWE / ASVS / WSTG / advisory mapping: {{verified_mapping_with_version_source_or_not_mapped}}
CVSS: {{optional_verified_version_vector_score_source_assumptions_or_not_scored}}

## Affected surface and root cause

Target, code/config revisions, exact file/line range and route/method: {{verified_location}}
Prerequisites: {{attacker_access_victim_interaction_roles_tenants_configuration}}
Data flow: {{entry_point_controlled_input_guards_sensitive_sink_impact}}
Existing controls and counterevidence considered: {{actual_checks}}
Root cause: {{why_the_authoritative_boundary_failed}}
Impact and blast radius: {{supported_confidentiality_integrity_availability_business_effects}}

## How it was explored and how to reproduce

Execution status: {{executed_in_authorized_fixture_or_not_dynamically_reproduced}}
Environment / code and configuration revisions: {{actual_test_identity}}
Setup: {{synthetic_records_owned_identities_and_controlled_hosts}}
Steps or minimal sanitized request: {{ordered_safe_actions_with_credential_placeholders}}
Expected secure result: {{invariant}}
Observed result: {{actual_observation_or_not_executed}}
Evidence: {{minimal_sanitized_code_test_output_or_safe_screenshot_reference}}
Cleanup: {{test_data_and_temporary_changes}}

A proposed procedure must be labeled proposed. Code proof is not a claim of live exploitation. Do not use real credentials, user records, metadata probes or external callback domains as proof. Negative reproduction with missing preconditions does not establish a false positive. Explain each evidenced link when chaining issues; do not combine unrelated hypotheses into a takeover claim.

## Correction and mitigation

Root-cause correction: {{smallest_complete_server_or_trust_boundary_fix}}
Affected consumers and compatibility: {{sibling_routes_clients_workers_storage_or_contracts}}
Defense in depth / containment: {{optional_waf_or_other_mitigation_distinct_from_fix}}
Migration/revocation/data-repair needs: {{separately_authorized_actions}}
Regression and permitted-use tests: {{meaningful_before_after_and_allowed_paths}}
Rollout and rollback: {{safe_order_owner_abort_conditions_and_reintroduced_risk}}

## Retest history

| Code/config revision | Environment | Case / method | Expected | Observed | Result / limitation |
| --- | --- | --- | --- | --- | --- |
| {{revision}} | {{environment}} | {{original_or_variant}} | {{secure_behavior}} | {{actual_result}} | {{passed_failed_blocked_or_not-run}} |

Closure reason / authorized risk owner when applicable: {{evidence_or_pending}}
Next action: {{concrete_followup}}

# Root-cause remediation and retest

## Establish the defect and acceptance condition

Verify the exact baseline and working tree; preserve unrelated work. Read the complete code path, relevant permission/storage/cache policies and installed API contracts. Record the security invariant in testable terms, such as “an authenticated member cannot read documents from a tenant to which they do not belong, through any document export path.” A broad label like “fix IDOR” is insufficient.

Confirm request scope: fix selected findings, all evidenced findings in a bounded area, or only propose changes. Separate immediate containment from durable correction and from recovery of previously exposed data. An exposed secret requires rotation/revocation and incident consideration; removing the literal only addresses one propagation path.

## Plan the smallest complete patch

Choose the authoritative shared boundary while preserving different consumers' legitimate behavior. Avoid a local special case that leaves bulk/admin/worker/real-time paths vulnerable. Document compatibility, cache invalidation, session revocation, data repair, provider changes and migration risks. Security fixes may need coordinated rollout across web instances, clients and workers; do not assume one process owns global truth.

When a migration is necessary, create a new migration and choose a safe expand/contract or repair path appropriate to the project. Do not change applied migrations. Test on synthetic data or an approved sanitized clone. Assess locks/runtime and the backward compatibility of old/new code during deployment. A destructive down migration is not a safe recovery plan.

## Demonstrate the regression

Prefer a deterministic local test that fails on the vulnerable baseline and passes on the patched implementation, asserting externally relevant behavior and data invariants. Keep fixtures owned and isolated. Assert denial/no side effect for forbidden users and success for permitted users; an endpoint that rejects everyone is not a correct authorization fix.

Include variants relevant to the root cause: another tenant, field/operation changes, batch/export routes, old tokens, concurrent duplicate requests, error/retry paths, cache hits, role revocation and reconnect. Use bounded concurrency with barriers or deterministic scheduling rather than flaky timing-only races. For browser controls, verify in a real supported browser when authorized; a command-line client's treatment of CORS is not browser evidence.

Do not weaken assertions, blanket-disable analyzers, remove failing tests, hide errors in casts or accept all inputs to make tests green. If baseline execution is impossible, state why and separate static proof from tests executed only after the patch. Record command, tool/environment, revision, result and safe evidence; do not invent a before-run.

## Reinspect the integrated change

Review the complete diff, installed contract changes, error behavior, imports/consumers, access boundaries and data consistency. Run the actual relevant existing checks. A whole test suite may be unnecessary for a small patch; a unit pass may be insufficient for a changed identity/proxy boundary. Use risk and project gates, not a fixed ritual.

After merges/base updates, recheck the final code/config. A result from a previous hash cannot be presented as a gate executed for the final artifact. Independent review is separate from the author agent's self-check. Follow the authorized Git workflow; do not auto-approve/merge or publish sensitive evidence into public PRs.

## Rollout, monitoring and rollback

Describe exact prerequisites, deploy ordering, minimal safe monitoring, owner and abort conditions. A canary must not leave vulnerable users knowingly exposed without an approved containment decision. Feature flags may reintroduce a vulnerability; document secure flag states. Reverting a security patch may restore the original defect, so consider forward fixes or limited functionality rather than automatic code rollback.

Keep infrastructure/WAF mitigations explicitly separate. A blocked reproducer behind WAF cannot prove the origin code no longer has the defect. When approved, verify corrected origin behavior in a private/staging path; never publicly expose an origin or remove production controls just for testing.

Update report statuses with actual evidence. `retest-passed` names the tested environment and revision, not a universal closure. If a dependency patch or live configuration must be applied by an operator, leave it `fixed-awaiting-retest` or `mitigated` as warranted and identify the remaining action.

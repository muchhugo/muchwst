---
name: muchwst-fix
description: "Fix evidenced web application vulnerabilities at the root cause and verify regressions. Use after a security finding or when the user requests review plus corrections. Preserve legitimate behavior, separate application fixes from edge mitigations, and produce a remediation and retest report."
---

# Web Security Fix

Read [safety](references/safety.md), [evidence/reporting](references/evidence-and-reporting.md) and [remediation workflow](references/remediation.md). Honor project instructions and actual authorization. This skill works alone with its bundled templates; `muchwst` is a useful precursor, not a required installed agent.

Confirm the finding, evidence and affected revision rather than trusting a scanner, issue description or another agent. Recover the full flow and existing protections. If a material assumption remains, label it and investigate before a speculative behavioral change.

Present a proportionate patch plan: invariant to restore, affected paths/consumers, tests, compatibility and deployment boundary. Continue routine authorized local edits without asking for approval per file. Do not deploy, rotate live secrets or alter infrastructure just because code fixes were requested.

Fix at the authoritative boundary and check sibling paths. Add an actual regression demonstrating the prior failure and the secure result where possible, plus permitted-use tests. Keep the patch cohesive, preserve applied migrations, and avoid unrelated cleanup. A test that only searches for a guard's text is not behavioral evidence.

Retest the original scenario, variants and relevant concurrency/failure paths. Record the code/config revision and environment for every observed result. Distinguish `mitigated`, `fixed-awaiting-retest` and `retest-passed`; a patch is not automatically a verified or deployed fix.

Always produce the [report](templates/report.md) with updated [findings](templates/finding.md), original evidence preserved, exact changes, before/after results, remaining risks, skipped checks and rollout/rollback notes. Use [structured report schema](references/report.schema.json) when JSON output is requested. Save privately and read back only under an authorized path.

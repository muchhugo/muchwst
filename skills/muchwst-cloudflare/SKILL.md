---
name: muchwst-cloudflare
description: "Review Cloudflare edge and web-origin security: WAF, rate limits, bots, scanner abuse, TLS, caching, trusted headers and origin bypass. Use with an explicitly scoped zone/application. Verify plan and current feature syntax, stage changes with rollback, and never substitute edge filtering for server authorization or a root-cause code fix."
---

# Cloudflare Hardening

Read [safety](references/safety.md), [evidence/reporting](references/evidence-and-reporting.md), [edge runbook](references/edge-runbook.md) and [source pointers](references/sources.md). No fixed plan entitlements, API fields, IP ranges, dashboard paths or managed-rule IDs are bundled. Verify them through current authorized documentation and the user's actual account/zone when needed.

Start from scoped read-only configuration or provided exports. Map hostname → proxied/DNS-only record → edge rules/cache/Workers → origin → application and separate HTTP from SSH/media/other protocols. Confirm allowed changes and exclusions. Lack of a connection or current docs is a reporting gap, not permission to guess a rule or alter another zone.

Prioritize exposed origin, broken TLS/trusted-header boundaries, cache leakage, exposed administration and route-specific abuse. A scanner label or volume graph is not proof of exploitation. Propose narrowly scoped controls with legitimate client tests and an observable staged rollout using [hardening plan](templates/hardening-plan.md).

Only apply an approved zone/ruleset change after validating supported syntax, phase/order and interactions with existing rules, integrations and plan. Use a non-enforcing observation mode when available; otherwise use an approved staging/shadow evaluation or bounded manual replay, not an invented paid feature. Preserve before-state and a tested reversal path. Do not remove origin access or enable HSTS preload without the separate consequences being understood and authorized.

Always deliver the [report](templates/report.md) and [findings](templates/finding.md), including before/after configuration, reason, tested browser/API/webhook/real-time behavior, false-positive checks, costs/availability limits, rollback and original application vulnerabilities still open. A WAF mitigation remains a mitigation; no edge setting proves the code is fixed.

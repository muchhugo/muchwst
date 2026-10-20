---
name: muchwst-data
description: "Review web application data isolation, financial and business invariants, database roles, transactions, caches, jobs and real-time delivery. Use for RLS, race conditions, replay, cross-tenant leaks and abuse-driven availability risks. Separate evidenced security defects from optional performance or distributed-system architecture."
---

# Web Data Security

Read [safety](references/safety.md), [evidence/reporting](references/evidence-and-reporting.md) and [data review](references/data-review.md). Use [sources](references/sources.md) for verified versioned references when available. Discover the actual database, ORM, cache, jobs, replicas and topology; do not require Redis, PostgreSQL, sharding or microservices merely to satisfy a list.

State the invariant and its authoritative owner: access to tenant data, one-time redemption, inventory, balances, ownership, durable event publication or bounded resource consumption. Trace both synchronous and asynchronous consumers across transaction and trust boundaries. Read the schema, migrations, policies, actual application roles, serialization and relevant query plans/configuration.

Use a role/tenant matrix and synthetic fixtures. For concurrent or replay defects, use deterministic bounded tests rather than live load or real financial actions. For database policies, test the real class of runtime role and session context rather than a privileged administrator connection. Avoid changing production to obtain evidence.

Review applicable sections, seek counterevidence, and classify each observation by actual impact. Missing indexes, full scans, lack of replicas or absence of an outbox are not vulnerabilities by themselves. Correct only when authorized; preserve applied migrations and compatibility across rolling versions.

Always return the [report](templates/report.md), including [findings](templates/finding.md), evidence, severity, safe reproduction/proposed tests, fixes, retests and coverage gaps. Use [JSON Schema](references/report.schema.json) for structured output. State which consistency/availability claims were proved and which remain assumptions.

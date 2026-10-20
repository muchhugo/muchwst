---
name: muchwst-runtime
description: "Review web runtime abuse resistance, resource bounds, queues, real-time lifecycle, deployment safety, observability and recovery. Use when operational behavior affects availability, integrity or confidentiality. Separate performance/SRE advice from exploitable defects; do not prescribe distributed infrastructure or run unbounded load tests."
---

# Web Runtime Security

Read [safety](references/safety.md), [evidence/reporting](references/evidence-and-reporting.md), [runtime review](references/runtime-review.md) and applicable [sources](references/sources.md). Establish the actual ingress, application, workers, data, cache and external-service topology from evidence.

Define the operation and invariant threatened by abuse or failure, plus the expected legitimate workload. Review size/time/concurrency/cost bounds, memory/connection lifecycle, queue and retry semantics, health/drain/failover behavior, logging and recovery. Distinguish an exploitable security path from an optimization, a resilience gap or a governance topic.

Use deterministic local fault fixtures and bounded workloads with synthetic data. Load/fuzz/chaos tests, production probes and paid cloud/model usage need explicit limits and target authorization. Do not benchmark a real service to failure or fabricate capacity/performance data when access is absent.

Propose the smallest scoped fix with before/after behavior, permitted traffic, metrics and recovery. Do not add sharding, Kubernetes, multi-region or service mesh solely to satisfy a checklist. Never prioritize availability by silently failing open authorization. Release controls and operational changes remain separately authorized.

Always return the [report](templates/report.md) and relevant [findings](templates/finding.md), coverage gaps, actual tests, configuration/revision, residual risks and measured versus proposed SLO/RTO/RPO values. No load test, failover, restore or monitoring deployment is implied by a code review.

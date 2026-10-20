# Availability, resource safety and operations

Institutional/technical pointers are in [sources](sources.md). Review the actual architecture; a conceptual topic is not a requirement to deploy its named technology.

## Resource consumption and bounded work

Trace attacker-influenced sizes, counts, regex patterns, queries, parser depth, uploads, decompression, conversions, expensive crypto, subscriptions and fan-out. Set bounded CPU/memory/time, body/header/response sizes, concurrent work, queue depth, file descriptors and paid calls appropriate to the operation. A frontend debounce or a request-count limit alone does not bound the cost of a single request.

Look for event-loop blocking, unhandled rejection/process termination, memory/socket/timer/listener leaks, unbounded streaming buffers, connection-pool exhaustion and disk/log growth. Prove the reachable failure/resource path; Big O, garbage collection, profiling/flame graphs, p99, cold starts and throughput are investigative tools, not automatic findings. Use synthetic bounded reproductions, not a live OOM or intentionally induced outage.

Apply timeouts/cancellation through dependent operations. If a client disconnects, background work should stop or continue only according to a deliberate durable-job contract. WebSockets/SSE require message/connection authorization, revocation and lifecycle checks in addition to upgrade-time controls. Resource cleanup must not accidentally revoke another user's session or close a shared global connection.

## Retry, queue and failure semantics

Use capped attempts, exponential delay/jitter when suitable, idempotent operations and a total deadline/budget. Avoid layers independently multiplying retries into storms. Respect meaningful throttling/backoff signals and guard against thundering herd after cache expiry/recovery. Bulkheads, load shedding and backpressure are options based on real failure boundaries, not mandatory libraries.

Verify durable jobs, ownership, tenant scoping, idempotency, deduplication, poison/dead-letter handling, ordering and cancellation. Assess at-least-once/exactly-once claims at the actual boundary. Do not guarantee a real-world payment/email executes exactly once from a broker flag. Identify the authority for a committed result and handle partial failure; don't turn an internal error into a successful user response.

## Health, shutdown and recovery

Inspect liveness versus readiness behavior, authentication of sensitive health detail, dependency checks and restart loops. Overly strict dependency probes can amplify outages; overly permissive readiness can send traffic to broken instances. Graceful shutdown/draining must consider in-flight transactions, active sockets, workers and message acknowledgment. Confirm actual service supervisor/orchestrator behavior rather than assuming Kubernetes.

Assess single points of failure, failover, replica lag, clock skew, stateful local assumptions and backup/restore only when present. Preserve data/permission consistency required by the operation during failover. Multi-region, availability zones, statelessness, sharding and autoscaling have tradeoffs; absence is not automatically a security defect. A fail-open permission fallback is different from an intentional degradation of a non-sensitive optional feature.

Define RTO/RPO and SLOs with the owner; distinguish targets from measured restore/failover outcomes. Recovery needs protected backups, key access and verified isolated restore. Disaster recovery, on-call, runbooks, postmortems and incident-response ownership are resilience/governance controls unless a concrete technical flaw is also established. Never claim certification or achieved availability from a document.

## Logs, metrics, tracing and privacy

Use meaningful structured events with safe correlation IDs and constrained actor/resource context. Redact credentials, authorization headers, session/refresh tokens, presigned URLs, raw prompts, personal data and unnecessary bodies. Protect audit-log access/integrity/retention; log enough for accountability without recording secrets. Separate security audit events from verbose debug telemetry.

Validate/escape untrusted fields for the log format and terminal/HTML display, limit event size and avoid unbounded attacker-controlled metric labels/cardinality. Distributed tracing/OpenTelemetry instrumentation can also leak headers and baggage. Verify actual exports, sampling, access, storage region and vendor data-transfer approvals rather than assuming a library is private by default.

Set actionable alerts with an owner and bounded cardinality/volume. Log rotation, error tracking and certificate/billing alerts need exercised response paths; creating a config is not evidence that anyone receives/acts on alerts. Alert fatigue is an operational issue, not a vulnerability score by itself.

## Delivery and governance

Inspect changes to resource limits, containers, health checks, migrations, feature flags, IaC/GitOps and deploy workflows. Ensure staging parity relevant to the test without copying live secrets or user data. Canary/blue-green rollout and rollback must preserve security invariants; a feature flag or rollback that restores an exploitable path needs explicit containment consideration.

Check build inputs, images, state/plan files and credential boundaries with the supply-chain skill when available. Pod disruption budgets, resource requests, VPCs/NAT/service mesh and ingress behavior are evaluated only if present. No package installation, infrastructure apply or production restart is implied.

Handle privacy, licensing, GDPR/LGPD, residency, SOC 2, PCI DSS and consent as scoped evidence/control questions, not legal certification. Establish applicable processing/jurisdiction and use qualified review for legal determinations. Email deliverability, bounces, SPF/DKIM/DMARC and chargebacks need business-specific controls; they are not generic proof of application compromise. Report confidentiality/integrity risks separately from commercial or compliance concerns.

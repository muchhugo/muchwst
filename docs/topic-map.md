# The original 250 topics — applicability map

Applicability/routing of the original 250 user topics; not official institutional coverage or 250 confirmed vulnerabilities.

**Not an official OWASP control mapping and not 250 required technologies.**

The authoring environment could not verify live institutional/vendor sources. Use [the source catalog](../shared/sources.md) with verified editions during a real review.

## Categories

- **core (43)**: Routinely consider the relevant web trust boundary; not an automatic finding.
- **conditional (132)**: Assess when the component/feature/processing exists or an evidenced risk makes it relevant.
- **supporting (49)**: Testing, assurance, operations or governance practice; not an independent exploit.
- **context (26)**: Architecture/conceptual tool; inspect actual assumptions without prescribing new infrastructure.

## Complete routing table

| # | Original topic | Applicability | Primary skill | Review criterion |
| --- | --- | --- | --- | --- |
| 1 | SQL Injection | core | [muchwst](../skills/muchwst/SKILL.md) | Trace parameterization and unsafe raw-query paths; prove reachability. |
| 2 | XSS | core | [muchwst](../skills/muchwst/SKILL.md) | Check stored, reflected and DOM rendering with contextual encoding. |
| 3 | CSRF | core | [muchwst](../skills/muchwst/SKILL.md) | Inspect ambient credentials and state-changing flows; do not confuse with CORS. |
| 4 | CORS | core | [muchwst](../skills/muchwst/SKILL.md) | Prove cross-origin protected-data exposure; public wildcard alone is not a defect. |
| 5 | SSRF | core | [muchwst](../skills/muchwst/SKILL.md) | Inspect outbound URL features, effective destinations and redirects when present. |
| 6 | IDOR | core | [muchwst](../skills/muchwst/SKILL.md) | Verify object and tenant authorization for reads, mutations and alternate paths. |
| 7 | Path Traversal | core | [muchwst](../skills/muchwst/SKILL.md) | Check final effective paths, archives, symlinks and authorization. |
| 8 | Mass Assignment | core | [muchwst](../skills/muchwst/SKILL.md) | Allowlist writable fields and enforce property-level permissions. |
| 9 | Clickjacking | core | [muchwst](../skills/muchwst/SKILL.md) | Match framing protection to legitimate embedding and demonstrated impact. |
| 10 | Content Security Policy | core | [muchwst](../skills/muchwst/SKILL.md) | Defense in depth with tested directives; absence alone is not High. |
| 11 | Security Headers | core | [muchwst](../skills/muchwst/SKILL.md) | Check effective browser policy, not obsolete blanket header requirements. |
| 12 | Input Validation | core | [muchwst](../skills/muchwst/SKILL.md) | Validate server trust boundaries, sizes and meaning; output safety is separate. |
| 13 | Server-Side Authorization | core | [muchwst](../skills/muchwst/SKILL.md) | Verify function, resource, tenant and property policy at authoritative boundaries. |
| 14 | Row-Level Security | conditional | [muchwst-data](../skills/muchwst-data/SKILL.md) | If used, check runtime roles, bypass paths, writes and pooled tenant context. |
| 15 | Least Privilege | core | [muchwst](../skills/muchwst/SKILL.md) | Check actual permissions of users, services, data roles and integrations. |
| 16 | RBAC | core | [muchwst](../skills/muchwst/SKILL.md) | Roles may need ownership, tenant and state constraints in addition. |
| 17 | Secrets Management | core | [muchwst-supply-chain](../skills/muchwst-supply-chain/SKILL.md) | Inventory secret lifecycle, delivery, access, logs and environment exposure. |
| 18 | .env in .gitignore | core | [muchwst-supply-chain](../skills/muchwst-supply-chain/SKILL.md) | Useful hygiene, not removal from history, artifacts or revocation of leaks. |
| 19 | API Key Rotation | core | [muchwst-supply-chain](../skills/muchwst-supply-chain/SKILL.md) | Review scopes and recovery; live rotation requires operator authorization. |
| 20 | Secret Scanning | supporting | [muchwst-supply-chain](../skills/muchwst-supply-chain/SKILL.md) | Treat results as redacted leads; do not validate live keys with third parties. |
| 21 | Hashing vs Encryption | core | [muchwst](../skills/muchwst/SKILL.md) | Choose according to recoverability and threat; no custom crypto. |
| 22 | Password Salting | conditional | [muchwst](../skills/muchwst/SKILL.md) | For stored passwords, use independent library-managed salts. |
| 23 | bcrypt & Argon2 | conditional | [muchwst](../skills/muchwst/SKILL.md) | Verify installed implementation, work factors, lengths and migration behavior. |
| 24 | JWT Expiry | conditional | [muchwst](../skills/muchwst/SKILL.md) | Validate signatures and applicable claims; decoding and expiry alone are insufficient. |
| 25 | Refresh Tokens | conditional | [muchwst](../skills/muchwst/SKILL.md) | Review storage, rotation, replay, concurrency and durable revocation. |
| 26 | OAuth 2.0 | conditional | [muchwst](../skills/muchwst/SKILL.md) | Verify actual flow, PKCE, redirect/state binding and trusted provider behavior. |
| 27 | OpenID Connect | conditional | [muchwst](../skills/muchwst/SKILL.md) | Validate identity issuer/audience/nonce and safe account linking. |
| 28 | Session Fixation | core | [muchwst](../skills/muchwst/SKILL.md) | Check regeneration and invalidation across authentication and elevation. |
| 29 | MFA | conditional | [muchwst](../skills/muchwst/SKILL.md) | Assess enrollment, recovery/removal and high-risk roles; absence is contextual. |
| 30 | Brute Force Protection | core | [muchwst](../skills/muchwst/SKILL.md) | Bound attempts/work without easy evasion, false lockout or data disclosure. |
| 31 | Account Enumeration | core | [muchwst](../skills/muchwst/SKILL.md) | Check body, status, timing and delivery distinctions in sensitive flows. |
| 32 | Timing Attacks | conditional | [muchwst](../skills/muchwst/SKILL.md) | Require bounded repeatable evidence; one latency difference is not proof. |
| 33 | File Upload Validation | conditional | [muchwst](../skills/muchwst/SKILL.md) | Authorize lifecycle and validate bounded content; isolate active formats. |
| 34 | Webhook Signature Verification | conditional | [muchwst](../skills/muchwst/SKILL.md) | Verify provider scheme on required raw bytes; add safe deduplication/replay handling. |
| 35 | TLS Certificate Expiry | conditional | [muchwst-vps](../skills/muchwst-vps/SKILL.md) | Inspect actual certificate/renewal evidence; do not imply monitoring was configured. |
| 36 | HSTS | conditional | [muchwst-cloudflare](../skills/muchwst-cloudflare/SKILL.md) | Stage after HTTPS verification; subdomains/preload need separate impact review. |
| 37 | Encryption at Rest | conditional | [muchwst-supply-chain](../skills/muchwst-supply-chain/SKILL.md) | Review keys, backups and access; it does not protect all runtime/plaintext exposure. |
| 38 | Dependency Vulnerabilities | core | [muchwst-supply-chain](../skills/muchwst-supply-chain/SKILL.md) | Verify resolved versions, dated advisories, reachability and build exposure. |
| 39 | Supply Chain Attacks | core | [muchwst-supply-chain](../skills/muchwst-supply-chain/SKILL.md) | Review packages, scripts, images, workflows, credentials and artifact trust. |
| 40 | Threat Modeling | core | [muchwst](../skills/muchwst/SKILL.md) | Use a small evidence-based model of assets, actors, boundaries and abuse goals. |
| 41 | Indexes | conditional | [muchwst-data](../skills/muchwst-data/SKILL.md) | Performance choice; a security finding needs a supported resource-abuse path. |
| 42 | EXPLAIN ANALYZE | supporting | [muchwst-data](../skills/muchwst-data/SKILL.md) | It executes statements; use only safe approved fixtures and limits. |
| 43 | N+1 Queries | conditional | [muchwst-data](../skills/muchwst-data/SKILL.md) | Assess actual bounded cost and abuse, not an automatic vulnerability. |
| 44 | Full Table Scans | conditional | [muchwst-data](../skills/muchwst-data/SKILL.md) | May be the correct plan; demonstrate cost/security effect before reporting. |
| 45 | Connection Pooling | conditional | [muchwst-data](../skills/muchwst-data/SKILL.md) | Check exhaustion, per-instance budgets and leaked tenant/session context. |
| 46 | Database Migrations | conditional | [muchwst-data](../skills/muchwst-data/SKILL.md) | Review permissions, locks, exposure and old/new version compatibility. |
| 47 | Down Migrations | conditional | [muchwst-data](../skills/muchwst-data/SKILL.md) | May destroy data; not a universal safe rollback requirement. |
| 48 | Transactions | conditional | [muchwst-data](../skills/muchwst-data/SKILL.md) | Identify actual atomic invariants and external side effects. |
| 49 | ACID | context | [muchwst-data](../skills/muchwst-data/SKILL.md) | Reason about needed guarantees; the label alone does not prove correctness. |
| 50 | Isolation Levels | conditional | [muchwst-data](../skills/muchwst-data/SKILL.md) | Verify actual driver/database semantics for the invariant. |
| 51 | Deadlocks | conditional | [muchwst-data](../skills/muchwst-data/SKILL.md) | Review lock order, bounded retries and idempotent transaction handling. |
| 52 | Optimistic Locking | conditional | [muchwst-data](../skills/muchwst-data/SKILL.md) | Use where version guards protect a demonstrated concurrent-write invariant. |
| 53 | Pessimistic Locking | conditional | [muchwst-data](../skills/muchwst-data/SKILL.md) | Use only where justified; inspect scope, timeouts and deadlock behavior. |
| 54 | Normalization | context | [muchwst-data](../skills/muchwst-data/SKILL.md) | Schema tradeoff, not a universal security requirement. |
| 55 | Denormalization | context | [muchwst-data](../skills/muchwst-data/SKILL.md) | Check consistency/access of duplicated data when actually used. |
| 56 | Foreign Keys | conditional | [muchwst-data](../skills/muchwst-data/SKILL.md) | Protect relevant integrity invariants and tenant relationships. |
| 57 | Unique Constraints | conditional | [muchwst-data](../skills/muchwst-data/SKILL.md) | Use appropriate durable constraints for race-sensitive uniqueness. |
| 58 | Cascading Deletes | conditional | [muchwst-data](../skills/muchwst-data/SKILL.md) | Verify approved deletion scope and cross-tenant/data-loss effects. |
| 59 | Soft Deletes | conditional | [muchwst-data](../skills/muchwst-data/SKILL.md) | Check all query paths; soft deletion is not privacy erasure. |
| 60 | UUIDs vs Auto-Increment | context | [muchwst-data](../skills/muchwst-data/SKILL.md) | Guessability differs; neither replaces resource authorization. |
| 61 | Cursor-Based Pagination | conditional | [muchwst](../skills/muchwst/SKILL.md) | Bound results and validate cursor authorization; not mandatory everywhere. |
| 62 | Full-Text Search | conditional | [muchwst-data](../skills/muchwst-data/SKILL.md) | Check access filters, query cost and data leakage when present. |
| 63 | Read Replicas | conditional | [muchwst-data](../skills/muchwst-data/SKILL.md) | Inspect access/consistency requirements where replicas exist. |
| 64 | Replication Lag | conditional | [muchwst-data](../skills/muchwst-data/SKILL.md) | Do stale reads re-grant permissions or violate an invariant? |
| 65 | Sharding | context | [muchwst-data](../skills/muchwst-data/SKILL.md) | Only inspect an actual architecture; do not add it for checklist compliance. |
| 66 | Partitioning | context | [muchwst-data](../skills/muchwst-data/SKILL.md) | Review actual routing/tenant/cost boundaries, not a universal prescription. |
| 67 | Hot Partitions | conditional | [muchwst-data](../skills/muchwst-data/SKILL.md) | Assess fairness/abuse and resource impact in an existing partitioned design. |
| 68 | Postgres VACUUM | conditional | [muchwst-data](../skills/muchwst-data/SKILL.md) | OS/database operations need evidence; do not blindly tune a production server. |
| 69 | Materialized Views | conditional | [muchwst-data](../skills/muchwst-data/SKILL.md) | Check access, freshness and derived sensitive data. |
| 70 | Backups | supporting | [muchwst-runtime](../skills/muchwst-runtime/SKILL.md) | Review protected storage, key recovery and actual restore evidence. |
| 71 | Testing Your Restores | supporting | [muchwst-runtime](../skills/muchwst-runtime/SKILL.md) | Only isolated approved restores; an existing backup is not proof of recovery. |
| 72 | Point-in-Time Recovery | conditional | [muchwst-data](../skills/muchwst-data/SKILL.md) | Verify configuration, retention, keys and measured recovery where required. |
| 73 | Change Data Capture | conditional | [muchwst-data](../skills/muchwst-data/SKILL.md) | Review data recipients, tenant boundaries and lifecycle when present. |
| 74 | Outbox Pattern | conditional | [muchwst-data](../skills/muchwst-data/SKILL.md) | Useful for specific atomic publication needs; not universal or exactly-once proof. |
| 75 | ORM Lazy Loading | conditional | [muchwst-data](../skills/muchwst-data/SKILL.md) | Inspect hidden query cost and accidental relationship disclosure. |
| 76 | CAP Theorem | context | [muchwst-data](../skills/muchwst-data/SKILL.md) | Architectural reasoning, not a vulnerability checklist requirement. |
| 77 | Eventual Consistency | conditional | [muchwst-data](../skills/muchwst-data/SKILL.md) | Assess whether staleness violates the particular security/business invariant. |
| 78 | Strong Consistency | conditional | [muchwst-data](../skills/muchwst-data/SKILL.md) | Require only where the invariant demands it, not for every read. |
| 79 | Raft Consensus | context | [muchwst-data](../skills/muchwst-data/SKILL.md) | Only relevant to systems actually using consensus; do not implement one during a fix. |
| 80 | Leader Election | context | [muchwst-data](../skills/muchwst-data/SKILL.md) | Review actual ownership/failover assumptions when present. |
| 81 | Split Brain | conditional | [muchwst-data](../skills/muchwst-data/SKILL.md) | Test bounded failure semantics if the topology can violate an invariant. |
| 82 | Quorums | context | [muchwst-data](../skills/muchwst-data/SKILL.md) | Inspect actual consistency configuration, not prescribed infrastructure. |
| 83 | Clock Skew | conditional | [muchwst-data](../skills/muchwst-data/SKILL.md) | Bound tolerance for expiry, locks, timestamps and distributed decisions. |
| 84 | Distributed Locks | conditional | [muchwst-data](../skills/muchwst-data/SKILL.md) | Check ownership, leases, fencing and failure handling where used. |
| 85 | Consistent Hashing | context | [muchwst-data](../skills/muchwst-data/SKILL.md) | An actual routing/cache design consideration, not a mandatory security control. |
| 86 | Bloom Filters | context | [muchwst-data](../skills/muchwst-data/SKILL.md) | Probabilistic results must not become final authorization truth. |
| 87 | Two-Phase Commit | context | [muchwst-data](../skills/muchwst-data/SKILL.md) | Only relevant if used; do not add distributed coordination speculatively. |
| 88 | CQRS | context | [muchwst-data](../skills/muchwst-data/SKILL.md) | Inspect actual read/write authorization and freshness; no required redesign. |
| 89 | Event Sourcing | context | [muchwst-data](../skills/muchwst-data/SKILL.md) | Check event access, replay, retention and state rules only when present. |
| 90 | Race Conditions | core | [muchwst-data](../skills/muchwst-data/SKILL.md) | Identify concurrent security/business invariants and deterministic safe tests. |
| 91 | Backpressure | conditional | [muchwst-runtime](../skills/muchwst-runtime/SKILL.md) | Bound queues, streams and producer/consumer work when relevant. |
| 92 | Load Shedding | conditional | [muchwst-runtime](../skills/muchwst-runtime/SKILL.md) | Protect service without silently failing open permissions. |
| 93 | Bulkheads | conditional | [muchwst-runtime](../skills/muchwst-runtime/SKILL.md) | Isolate actual failure/resource domains; no mandatory new library. |
| 94 | Jitter | conditional | [muchwst-runtime](../skills/muchwst-runtime/SKILL.md) | Use suitable bounded retry/recovery spreading, not random delay as a cure-all. |
| 95 | Retry Storms | conditional | [muchwst-runtime](../skills/muchwst-runtime/SKILL.md) | Check amplification across layers, budgets and idempotency. |
| 96 | Cascading Failures | conditional | [muchwst-runtime](../skills/muchwst-runtime/SKILL.md) | Trace actual dependencies and failure amplification. |
| 97 | Thundering Herd | conditional | [muchwst-runtime](../skills/muchwst-runtime/SKILL.md) | Check refresh/recovery fan-out and cache miss contention. |
| 98 | Cache Invalidation | conditional | [muchwst-data](../skills/muchwst-data/SKILL.md) | Review stale permissions, tenant keys and role-change invalidation. |
| 99 | Cache Hit Ratio | supporting | [muchwst-runtime](../skills/muchwst-runtime/SKILL.md) | A performance signal, not a security finding by itself. |
| 100 | TTLs | conditional | [muchwst-data](../skills/muchwst-data/SKILL.md) | Expiry policy must match revocation and durability requirements. |
| 101 | Cache Warming | context | [muchwst-runtime](../skills/muchwst-runtime/SKILL.md) | Performance/operations technique; check only if actual sensitive-data/cost risk exists. |
| 102 | Write-Through vs Write-Back | context | [muchwst-data](../skills/muchwst-data/SKILL.md) | Assess durability and stale authorization in the actual cache design. |
| 103 | Redis Eviction Policies | conditional | [muchwst-data](../skills/muchwst-data/SKILL.md) | Eviction must not discard required entitlement/revocation truth. |
| 104 | CDNs | conditional | [muchwst-cloudflare](../skills/muchwst-cloudflare/SKILL.md) | Review actual private caching, edge/origin trust and non-proxied exposure. |
| 105 | Cache-Control Headers | core | [muchwst](../skills/muchwst/SKILL.md) | Check effective policies through browser, worker, proxy and CDN. |
| 106 | ETags | conditional | [muchwst](../skills/muchwst/SKILL.md) | Verify conditional responses/cache keys do not cross identities or leak state. |
| 107 | Dead Letter Queues | conditional | [muchwst-data](../skills/muchwst-data/SKILL.md) | Control access, sensitive retention, retries and operator replay. |
| 108 | Poison Messages | conditional | [muchwst-runtime](../skills/muchwst-runtime/SKILL.md) | Bound retries/cost and avoid starving unrelated tenants/jobs. |
| 109 | At-Least-Once Delivery | conditional | [muchwst-data](../skills/muchwst-data/SKILL.md) | Require appropriate duplicate-safe effects and durable event identity. |
| 110 | Exactly-Once Semantics | conditional | [muchwst-data](../skills/muchwst-data/SKILL.md) | Name the exact boundary; broker claims do not cover arbitrary external effects. |
| 111 | Message Ordering | conditional | [muchwst-data](../skills/muchwst-data/SKILL.md) | Verify actual key/partition/consumer guarantees and stale event behavior. |
| 112 | Kafka Consumer Groups | conditional | [muchwst-data](../skills/muchwst-data/SKILL.md) | Only if Kafka exists; inspect scope, ownership and processing semantics. |
| 113 | Partition Keys | conditional | [muchwst-data](../skills/muchwst-data/SKILL.md) | Verify tenant/resource routing, order requirements and hot-key effects. |
| 114 | Background Jobs | conditional | [muchwst-data](../skills/muchwst-data/SKILL.md) | Authenticate initiation, authorize worker scope and validate bounded payloads. |
| 115 | Webhook Retries | conditional | [muchwst-data](../skills/muchwst-data/SKILL.md) | Make verified state transitions and side effects replay-safe. |
| 116 | DNS | conditional | [muchwst-cloudflare](../skills/muchwst-cloudflare/SKILL.md) | Inspect actual records, ownership, origin exposure and service dependencies. |
| 117 | DNS Propagation | supporting | [muchwst-cloudflare](../skills/muchwst-cloudflare/SKILL.md) | Stage changes and verify actual resolution; do not assume instant rollback. |
| 118 | HTTP Status Codes | core | [muchwst](../skills/muchwst/SKILL.md) | Preserve semantics while preventing sensitive disclosure/account enumeration. |
| 119 | HTTP Method Semantics | core | [muchwst](../skills/muchwst/SKILL.md) | Avoid unsafe state-changing retrieval and parser/method ambiguity. |
| 120 | Keep-Alive | conditional | [muchwst-runtime](../skills/muchwst-runtime/SKILL.md) | Assess connection budgets/timeouts and lifecycle; not an independent flaw. |
| 121 | HTTP/2 | conditional | [muchwst](../skills/muchwst/SKILL.md) | Inspect actual parsers/proxies and abuse limits; no protocol-name verdict. |
| 122 | WebSockets | conditional | [muchwst](../skills/muchwst/SKILL.md) | Authorize messages/resources and revoke already-open protected delivery. |
| 123 | Server-Sent Events | conditional | [muchwst](../skills/muchwst/SKILL.md) | Verify access, token handling, resume IDs, cancellation and buffers. |
| 124 | Long Polling | conditional | [muchwst](../skills/muchwst/SKILL.md) | Verify repeated access decisions, timeouts, resource limits and cleanup. |
| 125 | gRPC | conditional | [muchwst](../skills/muchwst/SKILL.md) | Inspect actual gateways, authentication, schemas and resource limits. |
| 126 | Protocol Buffers | conditional | [muchwst](../skills/muchwst/SKILL.md) | Validate application invariants and trust boundaries beyond serialization. |
| 127 | API Versioning | conditional | [muchwst](../skills/muchwst/SKILL.md) | Inventory deprecated routes and consistent protections across versions. |
| 128 | OpenAPI Specs | supporting | [muchwst](../skills/muchwst/SKILL.md) | Compare to runtime checks; a specification alone does not enforce policy. |
| 129 | Backward Compatibility | core | [muchwst-fix](../skills/muchwst-fix/SKILL.md) | Protect legitimate consumers without preserving a known security defect blindly. |
| 130 | Request Size Limits | core | [muchwst](../skills/muchwst/SKILL.md) | Bound parsing/processing/decompression cost before expensive work. |
| 131 | Compression | conditional | [muchwst-runtime](../skills/muchwst-runtime/SKILL.md) | Assess expansion, CPU, secrets/compression side channels and limits where relevant. |
| 132 | Latency vs Throughput | supporting | [muchwst-runtime](../skills/muchwst-runtime/SKILL.md) | Measurement context; not a vulnerability or universal target. |
| 133 | Egress Fees | supporting | [muchwst-runtime](../skills/muchwst-runtime/SKILL.md) | Assess abuse-driven cost separately from ordinary commercial optimization. |
| 134 | VPCs | conditional | [muchwst-vps](../skills/muchwst-vps/SKILL.md) | Inspect actual network boundaries/paths; no mandate to deploy a VPC. |
| 135 | Subnets | conditional | [muchwst-vps](../skills/muchwst-vps/SKILL.md) | Check reachability and segmentation evidence when used. |
| 136 | NAT Gateways | conditional | [muchwst-vps](../skills/muchwst-vps/SKILL.md) | NAT is not application authorization; inspect actual ingress/egress controls. |
| 137 | Firewalls | conditional | [muchwst-vps](../skills/muchwst-vps/SKILL.md) | Verify effective IPv4/IPv6/container rules and recoverable changes. |
| 138 | Security Groups | conditional | [muchwst-vps](../skills/muchwst-vps/SKILL.md) | Inspect cloud and host rules together and least-privilege service exposure. |
| 139 | Service Mesh | context | [muchwst-runtime](../skills/muchwst-runtime/SKILL.md) | Only if present; mesh names do not prove authentication or tenancy. |
| 140 | Ingress Controllers | conditional | [muchwst-vps](../skills/muchwst-vps/SKILL.md) | Verify routes, trusted headers, private services and effective settings. |
| 141 | Health Checks | conditional | [muchwst-runtime](../skills/muchwst-runtime/SKILL.md) | Avoid sensitive detail exposure and misleading/overly broad checks. |
| 142 | Liveness vs Readiness Probes | conditional | [muchwst-runtime](../skills/muchwst-runtime/SKILL.md) | Inspect real restart/routing semantics without amplifying outages. |
| 143 | Graceful Shutdown | conditional | [muchwst-runtime](../skills/muchwst-runtime/SKILL.md) | Handle active transactions, sockets and jobs during actual shutdown. |
| 144 | Connection Draining | conditional | [muchwst-runtime](../skills/muchwst-runtime/SKILL.md) | Preserve bounded valid in-flight work and prevent resource leaks. |
| 145 | Stateless Services | context | [muchwst-runtime](../skills/muchwst-runtime/SKILL.md) | Architecture choice; check accidental cross-user/process state instead of prescribing. |
| 146 | Failover | conditional | [muchwst-runtime](../skills/muchwst-runtime/SKILL.md) | Verify protected invariants and distinguish tested recovery from a design claim. |
| 147 | Multi-Region | context | [muchwst-runtime](../skills/muchwst-runtime/SKILL.md) | Optional topology; assess only actual latency, data and consistency implications. |
| 148 | Availability Zones | context | [muchwst-runtime](../skills/muchwst-runtime/SKILL.md) | Deployment/recovery design, not a security mandate for every project. |
| 149 | Single Points of Failure | conditional | [muchwst-runtime](../skills/muchwst-runtime/SKILL.md) | Report contextual resilience risks without automatically calling them exploitable. |
| 150 | Disaster Recovery | supporting | [muchwst-runtime](../skills/muchwst-runtime/SKILL.md) | Check owners, protected backups and measured recovery exercises. |
| 151 | RTO & RPO | supporting | [muchwst-runtime](../skills/muchwst-runtime/SKILL.md) | Distinguish owner-approved targets from demonstrated recovery results. |
| 152 | SLAs | supporting | [muchwst-runtime](../skills/muchwst-runtime/SKILL.md) | Business commitments need actual policy/legal review, not an invented guarantee. |
| 153 | SLOs | supporting | [muchwst-runtime](../skills/muchwst-runtime/SKILL.md) | Use meaningful observed service measures and approved targets. |
| 154 | Error Budgets | supporting | [muchwst-runtime](../skills/muchwst-runtime/SKILL.md) | Operational decision framework, not a vulnerability score. |
| 155 | Incident Response | supporting | [muchwst-runtime](../skills/muchwst-runtime/SKILL.md) | Record containment/evidence/recovery owners; no incident action is implied. |
| 156 | On-Call | supporting | [muchwst-runtime](../skills/muchwst-runtime/SKILL.md) | Confirm actual response ownership rather than inventing staffing. |
| 157 | Runbooks | supporting | [muchwst-runtime](../skills/muchwst-runtime/SKILL.md) | Keep actionable tested recovery instructions with access boundaries. |
| 158 | Postmortems | supporting | [muchwst-runtime](../skills/muchwst-runtime/SKILL.md) | Learn causes without fabricating incident history or exposing sensitive data. |
| 159 | Chaos Engineering | supporting | [muchwst-runtime](../skills/muchwst-runtime/SKILL.md) | Needs explicit scoped disruption approval; not a routine review command. |
| 160 | Graceful Degradation | conditional | [muchwst-runtime](../skills/muchwst-runtime/SKILL.md) | Degrade optional function without silently failing open authorization. |
| 161 | Autoscaling | conditional | [muchwst-runtime](../skills/muchwst-runtime/SKILL.md) | Check limits and abuse-driven costs where configured; no universal fix. |
| 162 | Horizontal vs Vertical Scaling | context | [muchwst-runtime](../skills/muchwst-runtime/SKILL.md) | Architecture/capacity tradeoff; verify cross-instance invariants when relevant. |
| 163 | Cold Starts | conditional | [muchwst-runtime](../skills/muchwst-runtime/SKILL.md) | Assess actual latency/resource behavior, not automatic severity. |
| 164 | Capacity Planning | supporting | [muchwst-runtime](../skills/muchwst-runtime/SKILL.md) | Use workload evidence and budgets, not invented p99/capacity numbers. |
| 165 | Load Testing | supporting | [muchwst-runtime](../skills/muchwst-runtime/SKILL.md) | Only authorized bounded targets; no saturation or financial effects by default. |
| 166 | Memory Leaks | conditional | [muchwst-runtime](../skills/muchwst-runtime/SKILL.md) | Trace reachable growth/lifecycle and bound a safe reproduction. |
| 167 | OOM Killer | conditional | [muchwst-runtime](../skills/muchwst-runtime/SKILL.md) | Inspect relevant resource limits/failure paths without causing a live outage. |
| 168 | Structured Logging | core | [muchwst-runtime](../skills/muchwst-runtime/SKILL.md) | Useful safe events with redaction, integrity and no injected control characters. |
| 169 | Log Levels | supporting | [muchwst-runtime](../skills/muchwst-runtime/SKILL.md) | Production debug verbosity may expose data; review actual emitted content. |
| 170 | Log Rotation | supporting | [muchwst-runtime](../skills/muchwst-runtime/SKILL.md) | Bound disk/retention and preserve incident evidence appropriately. |
| 171 | Distributed Tracing | conditional | [muchwst-runtime](../skills/muchwst-runtime/SKILL.md) | Protect headers, baggage, sampling and telemetry recipients. |
| 172 | OpenTelemetry | conditional | [muchwst-runtime](../skills/muchwst-runtime/SKILL.md) | Inspect actual exporter/configuration; instrumentation is not privacy by default. |
| 173 | Correlation IDs | supporting | [muchwst-runtime](../skills/muchwst-runtime/SKILL.md) | Use safe bounded IDs that do not embed tokens or personal information. |
| 174 | Metrics Cardinality | conditional | [muchwst-runtime](../skills/muchwst-runtime/SKILL.md) | Avoid unbounded attacker-controlled labels and sensitive identifiers. |
| 175 | p99 Latency | supporting | [muchwst-runtime](../skills/muchwst-runtime/SKILL.md) | Measure honestly; tail latency is evidence context, not a vulnerability itself. |
| 176 | Alert Fatigue | supporting | [muchwst-runtime](../skills/muchwst-runtime/SKILL.md) | Actionable ownership/noise is an operations concern, not a security score. |
| 177 | Error Tracking | conditional | [muchwst-runtime](../skills/muchwst-runtime/SKILL.md) | Redact stack context/PII before sending to approved recipients. |
| 178 | Profiling | supporting | [muchwst-runtime](../skills/muchwst-runtime/SKILL.md) | Use scoped safe data and limits; profiles can contain sensitive material. |
| 179 | Flame Graphs | supporting | [muchwst-runtime](../skills/muchwst-runtime/SKILL.md) | Diagnostic artifact, not proof of a vulnerability without a data/control path. |
| 180 | Infrastructure as Code | conditional | [muchwst-supply-chain](../skills/muchwst-supply-chain/SKILL.md) | Review privileged changes, secrets, plan/state and deployment trust. |
| 181 | Terraform State | conditional | [muchwst-supply-chain](../skills/muchwst-supply-chain/SKILL.md) | Control encryption/access and artifacts; sensitive variable marking is not redaction. |
| 182 | GitOps | conditional | [muchwst-supply-chain](../skills/muchwst-supply-chain/SKILL.md) | Verify trusted reconciliation inputs and permissions; review is not apply permission. |
| 183 | Blue-Green Deployments | conditional | [muchwst-runtime](../skills/muchwst-runtime/SKILL.md) | Check actual routing/old-new security invariants; not required universally. |
| 184 | Canary Releases | conditional | [muchwst-fix](../skills/muchwst-fix/SKILL.md) | Stage verified fixes without silently leaving users exposed; report rollout limits. |
| 185 | Rollbacks | core | [muchwst-fix](../skills/muchwst-fix/SKILL.md) | A reverted security fix may reopen a defect; define a safe recovery strategy. |
| 186 | Feature Flags | conditional | [muchwst-fix](../skills/muchwst-fix/SKILL.md) | Inspect secure defaults and flag paths that can re-enable a vulnerability. |
| 187 | Environment Parity | supporting | [muchwst-runtime](../skills/muchwst-runtime/SKILL.md) | Match relevant behavior without copying production secrets or data. |
| 188 | Staging Environments | supporting | [muchwst-runtime](../skills/muchwst-runtime/SKILL.md) | Use approved isolated fixtures; staging does not mean unlimited test authority. |
| 189 | 12-Factor Apps | context | [muchwst-runtime](../skills/muchwst-runtime/SKILL.md) | Design guidance, not mandatory security compliance or a proof of safety. |
| 190 | Multi-Stage Builds | conditional | [muchwst-supply-chain](../skills/muchwst-supply-chain/SKILL.md) | Check copied artifacts, cache and layers for leaked secrets. |
| 191 | Non-Root Containers | conditional | [muchwst-vps](../skills/muchwst-vps/SKILL.md) | Apply least privilege with required paths/capabilities; verify effective runtime identity. |
| 192 | Image Scanning | supporting | [muchwst-supply-chain](../skills/muchwst-supply-chain/SKILL.md) | Validate image/digest/advisories and exposure; scanner count is not final risk. |
| 193 | Resource Requests & Limits | conditional | [muchwst-runtime](../skills/muchwst-runtime/SKILL.md) | Inspect actual scheduler/runtime constraints and legitimate workload effects. |
| 194 | Pod Disruption Budgets | conditional | [muchwst-runtime](../skills/muchwst-runtime/SKILL.md) | Only if relevant orchestration exists; assess actual drain/recovery behavior. |
| 195 | Semantic Versioning | supporting | [muchwst-supply-chain](../skills/muchwst-supply-chain/SKILL.md) | Version labels do not prove compatibility or security; inspect actual changes. |
| 196 | Lockfiles | core | [muchwst-supply-chain](../skills/muchwst-supply-chain/SKILL.md) | Use resolved provenance/version evidence; pins alone do not establish trust. |
| 197 | Reproducible Builds | supporting | [muchwst-supply-chain](../skills/muchwst-supply-chain/SKILL.md) | Compare actual trusted inputs/artifacts; do not assert reproducibility from a lockfile. |
| 198 | Branch Protection | supporting | [muchwst-supply-chain](../skills/muchwst-supply-chain/SKILL.md) | Inspect authorized settings; missing governance is not automatically a code vulnerability. |
| 199 | Public S3 Buckets | conditional | [muchwst](../skills/muchwst/SKILL.md) | Distinguish intentional public assets from private data exposed by policy/ACL. |
| 200 | Presigned URLs | conditional | [muchwst](../skills/muchwst/SKILL.md) | Authorize issuance and constrain bearer capability scope/expiry/logging. |
| 201 | Cloud Billing Alerts | supporting | [muchwst-runtime](../skills/muchwst-runtime/SKILL.md) | Notifications may lag and are not hard spend caps without provider evidence. |
| 202 | Unit Tests | supporting | [muchwst-fix](../skills/muchwst-fix/SKILL.md) | Prove a meaningful invariant with both denied and legitimate flows. |
| 203 | Integration Tests | supporting | [muchwst-fix](../skills/muchwst-fix/SKILL.md) | Exercise real relevant boundaries with safe fixtures and permissions. |
| 204 | End-to-End Tests | supporting | [muchwst-fix](../skills/muchwst-fix/SKILL.md) | Verify actual browser/API flows in the authorized test environment. |
| 205 | Contract Testing | supporting | [muchwst-fix](../skills/muchwst-fix/SKILL.md) | Check public fields, errors and compatibility; contracts alone are not authorization. |
| 206 | Flaky Tests | supporting | [muchwst-fix](../skills/muchwst-fix/SKILL.md) | Investigate nondeterminism; retries/skips do not erase regression evidence. |
| 207 | Mocking | supporting | [muchwst-fix](../skills/muchwst-fix/SKILL.md) | Mock dangerous effects but do not mock away the guard/sink being verified. |
| 208 | Regression Tests | core | [muchwst-fix](../skills/muchwst-fix/SKILL.md) | Prefer fail-before/pass-after proof plus legitimate behavior at the tested revision. |
| 209 | Smoke Tests | supporting | [muchwst-fix](../skills/muchwst-fix/SKILL.md) | Check basic deployed/tested behavior without claiming comprehensive coverage. |
| 210 | Property-Based Testing | supporting | [muchwst-fix](../skills/muchwst-fix/SKILL.md) | Use bounded invariant-driven cases and preserve minimal failures. |
| 211 | Fuzzing | supporting | [muchwst](../skills/muchwst/SKILL.md) | Only authorized bounded fixtures; do not run a public fuzz campaign implicitly. |
| 212 | Error Handling | core | [muchwst](../skills/muchwst/SKILL.md) | Preserve semantics, avoid disclosure and fail-open behavior. |
| 213 | Edge Cases | core | [muchwst](../skills/muchwst/SKILL.md) | Test boundary values and states that affect real contracts/security invariants. |
| 214 | Off-by-One Errors | conditional | [muchwst](../skills/muchwst/SKILL.md) | Link an actual boundary error to access, quota, expiry or other impact. |
| 215 | Floating Point Math | conditional | [muchwst-data](../skills/muchwst-data/SKILL.md) | Evaluate the domain and precision needed; use in UI alone is not a security defect. |
| 216 | Storing Money as Floats | conditional | [muchwst-data](../skills/muchwst-data/SKILL.md) | Use deliberate exact monetary representation and currency-aware rounding/ranges. |
| 217 | Time Zones | conditional | [muchwst-data](../skills/muchwst-data/SKILL.md) | Inspect expiry/billing/business dates with explicit semantics. |
| 218 | Daylight Saving Time | conditional | [muchwst-data](../skills/muchwst-data/SKILL.md) | Verify date-sensitive invariants; no need to add time logic where absent. |
| 219 | Unicode | conditional | [muchwst](../skills/muchwst/SKILL.md) | Check canonical identity/encoding rules without mutating exact passwords/tokens. |
| 220 | Character Encoding | conditional | [muchwst](../skills/muchwst/SKILL.md) | Prevent decoding disagreement and use sink-appropriate output encoding. |
| 221 | Thread Safety | conditional | [muchwst-data](../skills/muchwst-data/SKILL.md) | Inspect shared state and real runtime concurrency, not only language labels. |
| 222 | Event Loop Blocking | conditional | [muchwst-runtime](../skills/muchwst-runtime/SKILL.md) | Trace reachable expensive work and bounded resource abuse. |
| 223 | Unhandled Promise Rejections | conditional | [muchwst-runtime](../skills/muchwst-runtime/SKILL.md) | Inspect actual runtime failure behavior and error/recovery controls. |
| 224 | Integer Overflow | conditional | [muchwst-data](../skills/muchwst-data/SKILL.md) | Validate bounded values/conversions at monetary, size and security boundaries. |
| 225 | Garbage Collection | context | [muchwst-runtime](../skills/muchwst-runtime/SKILL.md) | Runtime behavior to investigate when relevant; not a security requirement itself. |
| 226 | Schema Validation | core | [muchwst](../skills/muchwst/SKILL.md) | Execute request/response boundary schemas; types alone are not runtime validation. |
| 227 | Debouncing | context | [muchwst](../skills/muchwst/SKILL.md) | UI behavior, not protection against direct server calls. |
| 228 | Big O Notation | context | [muchwst-runtime](../skills/muchwst-runtime/SKILL.md) | Reasoning tool for cost; actual reachability/limits determine security impact. |
| 229 | Technical Debt | supporting | [muchwst](../skills/muchwst/SKILL.md) | Separate maintainability backlog from demonstrated exploitable defects. |
| 230 | Dead Code | conditional | [muchwst](../skills/muchwst/SKILL.md) | Prove reachability/unreachability, including dynamic paths; no blanket deletion. |
| 231 | Merge Conflicts | core | [muchwst-fix](../skills/muchwst-fix/SKILL.md) | Review the actual final integrated result, not only the previous branch evidence. |
| 232 | GDPR | supporting | [muchwst-runtime](../skills/muchwst-runtime/SKILL.md) | Determine applicable processing/evidence with qualified review; no legal certification. |
| 233 | PII Handling | core | [muchwst](../skills/muchwst/SKILL.md) | Minimize authorized fields, retention, logs, caches and external transfers. |
| 234 | Audit Logs | core | [muchwst-runtime](../skills/muchwst-runtime/SKILL.md) | Capture safe useful security events with integrity/access/retention controls. |
| 235 | Data Residency | conditional | [muchwst-runtime](../skills/muchwst-runtime/SKILL.md) | Verify actual replicas/backups/telemetry/providers and applicable obligations. |
| 236 | SOC 2 | supporting | [muchwst-runtime](../skills/muchwst-runtime/SKILL.md) | Governance/assurance context; a checklist cannot certify compliance. |
| 237 | PCI DSS | conditional | [muchwst-runtime](../skills/muchwst-runtime/SKILL.md) | Payment processing scope and current applicable requirements need qualified verification. |
| 238 | Cookie Consent | conditional | [muchwst-runtime](../skills/muchwst-runtime/SKILL.md) | Review actual cookie purposes/processing and jurisdiction; not every cookie is optional. |
| 239 | Software Licenses | supporting | [muchwst-supply-chain](../skills/muchwst-supply-chain/SKILL.md) | Track provenance/obligations; no invented legal conclusions. |
| 240 | SPF, DKIM & DMARC | conditional | [muchwst](../skills/muchwst/SKILL.md) | Check actual senders/DNS plan; mail authentication is not API authorization. |
| 241 | Email Bounce Handling | conditional | [muchwst-runtime](../skills/muchwst-runtime/SKILL.md) | Prevent abuse/disclosure and review provider events when email is used. |
| 242 | Chargebacks | conditional | [muchwst](../skills/muchwst/SKILL.md) | Business/payment risk; verify price/entitlement/webhook/refund invariants. |
| 243 | Bot Protection | conditional | [muchwst-cloudflare](../skills/muchwst-cloudflare/SKILL.md) | Use supported signals and legitimate-client tests; no blanket scanner/user-agent trust. |
| 244 | Prompt Injection | conditional | [muchwst-ai](../skills/muchwst-ai/SKILL.md) | If AI/tools exist, prove unauthorized effects and enforce policy outside the model. |
| 245 | Hallucinated Packages | core | [muchwst-supply-chain](../skills/muchwst-supply-chain/SKILL.md) | Verify actual package existence/provenance/API before an authorized installation. |
| 246 | Real-time streaming | conditional | [muchwst](../skills/muchwst/SKILL.md) | Validate access/revocation, buffering, cancellation, costs and sensitive event output. |
| 247 | Context Windows | conditional | [muchwst-ai](../skills/muchwst-ai/SKILL.md) | Review isolation/retention and context budgets; size does not prove memory safety. |
| 248 | Evals | supporting | [muchwst-ai](../skills/muchwst-ai/SKILL.md) | Use bounded adversarial and allowed-flow tests; one pass is not assurance. |
| 249 | Model Version Pinning | conditional | [muchwst-ai](../skills/muchwst-ai/SKILL.md) | Record actual versions/alias limits and re-evaluate changes when the feature exists. |
| 250 | Reading the maxed LOC Diff | core | [muchwst](../skills/muchwst/SKILL.md) | Interpret as complete large/truncated-diff review: recover pages/files or disclose exact gaps. Never silently cap coverage. |

Item 250 is interpreted as full coverage of large/truncated diffs, not permission to skip files after a maximum line count. Record missing ranges and recover source when possible.

See [supplemental controls](additional-controls.md) for browser/API requirements and other web surfaces added beyond the original list. Security impact requires actual evidence; classification here is only a routing decision.

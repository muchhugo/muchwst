# Data boundaries, integrity and resilience

Primary pointers: OWASP Authorization/API guidance, installed database/ORM manuals and the relevant vendor's delivery semantics in [sources](sources.md). Version-specific policy/transaction behavior must be verified; this is not a demand for one database architecture.

## Isolation, RLS and database privileges

Trace resource ownership and tenant predicates through joins, nested queries, exports, search, soft deletes, materialized views, CDC and jobs. Verify read and write policies, including insertion and the new state after updates. Understand runtime roles versus migrations/admin roles. With PostgreSQL RLS, inspect ownership, superuser/`BYPASSRLS`, forced-policy configuration where applicable, views/functions and security-definer paths; do not prove safety only with a role that bypasses policies.

Verify how tenant/actor context is set and cleared across pooled connections and transactions. A session variable left on a reused connection can cross tenant boundaries. SQL filtering, RLS and server authorization may complement one another; the absence of RLS alone does not prove unauthorized access. Use two tenants and real policy-equivalent application roles in a disposable test database.

Apply least privilege to schema changes, ordinary data access, backups and analytics. Keep privileged service credentials outside clients and avoid using migration roles for ordinary requests. Check object storage, cache and message permissions separately; a database policy does not cover all those surfaces.

## Transactions and business invariants

Identify exact atomic boundaries and failure points. Enforce unique/foreign-key/check constraints for invariants the database can express; application checks before writes may race. Confirm isolation-level behavior, lock ordering, retryable errors and rollback semantics in the actual driver/ORM. Transactions do not automatically prevent every lost update or cross-service side effect.

Check optimistic version guards and pessimistic locks where justified. Retry a bounded, safe unit with idempotent side effects and jitter, not an arbitrary subsection that duplicates a charge or message. Use atomic state transitions for refresh tokens, one-time links, redemption, orders and entitlements. Check concurrent access and revoked identities across app instances.

Store monetary values using an intentional precise representation such as decimal or currency-aware integer minor units; never assume every currency has two decimals. Define rounding, overflow and allowed ranges at boundaries. Validate server-derived prices and sums. Race conditions or imprecise arithmetic are security findings only when a supported integrity/abuse path is established, not because a numeric type appears in unrelated UI code.

Soft deletion is not erasure and must not let users regain access through another query. Cascades need a confirmed deletion policy and tenant boundaries. UUIDs versus sequential IDs affect guessability and operational tradeoffs, not whether authorization is necessary. Normalization, denormalization and schema style are contextual choices, not universal security requirements.

## Query cost and database operations

Bound filters, pagination, batch sizes, sorting, search complexity, regexes and result payloads at the server. Protect tenant fairness and expensive queries against abuse. Indexes, N+1 behavior, full scans, lazy loading, materialized views and pool sizing are performance/reliability topics unless an evidenced confidentiality/integrity/availability impact exists. A planner may correctly choose a sequential scan.

`EXPLAIN ANALYZE` executes the statement. Even SELECT can invoke side-effecting functions, and rollback is not a guarantee against all external effects. Do not run it against production or mutating queries by default. Use approved safe fixtures, plain plan inspection where appropriate, bounded timeouts and sanitized representative data. Do not tune VACUUM, partitions or connection limits blindly.

Review migrations for data exposure, privileged execution, long locks, partial deployment and old/new code compatibility. Preserve applied migrations. Down migrations can destroy data; choose a verified forward-fix/restore strategy rather than auto-reversal. Backups, restore tests and point-in-time recovery need separate storage access control, encrypted transport/storage as appropriate, key recovery, retention and a measured recovery exercise in an isolated environment. A backup existing is not proof it can be restored; an untested RTO/RPO is a target, not an achieved guarantee.

## Caches, replicas and permissions

Verify tenant/user/action cache keys, private cache controls, invalidation on access changes, bounded TTLs and failure behavior. A cache should not be the sole durable record for an entitlement that must survive eviction. Inspect eviction and restart behavior when that affects security. TTL expiry is not necessarily immediate authorization revocation.

Use the consistency source required by the invariant. Read-replica lag or eventual consistency can leak/re-grant access after role removal if the application relies on stale policy. Test behavior under cache misses, stale entries, reconnect and replica delay using safe fixtures. Do not prescribe strong consistency globally; constrain the operations that require it. Include ETags and conditional responses in cross-tenant tests.

## Queues, events and background jobs

Authenticate/authorize job initiation and scope worker execution to the intended actor/resource. Validate payloads, bound attempts/cost, handle poison messages and separate dead-letter access/retention. At-least-once delivery requires duplicate-safe processing; ordering guarantees depend on the actual partition/key/consumer contract.

An outbox can coordinate committed data with event publication when needed, but it still needs durable publication/retry/deduplication semantics. “Exactly once” must name the actual boundary; broker features do not automatically make external payments/emails exactly once. Check failure after a side effect but before acknowledgment, retries, replays, delayed events and event identity collisions.

## Distribution and availability

Only review Raft, leader election, quorums, split brain, distributed locks, sharding, consistent hashing, CQRS, event sourcing or two-phase commit when the system actually uses or needs them. Do not implement a consensus algorithm or distributed architecture as a security fix without separate scope.

When locks coordinate privileged writes, assess lease expiry, ownership, fencing and clock/network faults. A Redis lock with a TTL is not a universal correctness proof. Bound clocks/tokens and recovery behavior. Check retry storms, thundering herd, backpressure, load shedding, fan-out and cascading failures with limited tests. Prefer reduced functionality to fail-open permission checks; recoverable data paths may have different approved availability policies.

Bound streaming buffers, memory and outstanding jobs; propagate cancellation and clean up sessions/connections. Measure resource/cost risk in the relevant context. Load/chaos testing and infrastructure tuning are separately authorized operations, not routine code review side effects.

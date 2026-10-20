# APIs, proxies, caches and real-time connections

Reference pointers: OWASP API guidance, IETF HTTP semantics and actual framework/proxy docs in [sources](sources.md). Verify runtime behavior; do not infer a control from a protocol name.

## API boundaries

Inventory public/private/admin endpoints, deprecated versions, server-side action endpoints, GraphQL operations, gRPC gateways and internal routes exposed through ingress. Compare runtime authorization/validation with OpenAPI or other contracts; a spec is not enforcement. Check method semantics, errors without sensitive stack traces, explicit request/body/header/response limits and bounded pagination/batching/query complexity. Error handling must not turn auth/database failures into success.

Inspect GraphQL field/object authorization and cost/depth/batching limits where used. Disabled introspection alone is not security. Rate/size limits must protect the operation's true cost, including expensive hashes, regex processing, conversions, queries and fan-out. Test limits with bounded safe cases, not saturation of a real service. Debouncing in a browser is not a server-side abuse control.

## Trusted proxies and parsing

Document the full edge → proxy → server chain. Trust forwarded client IP/scheme/host headers only from authenticated/configured trusted hops; origin requests must not let a direct caller forge a trusted client IP. Use a configured public origin for security-sensitive links. Restrict accepted Host/SNI/routing as part of the deployment policy.

Review inconsistent HTTP framing/normalization, duplicate headers, conflicting content length/transfer handling and path/method decoding across layers when those components are in scope. Request smuggling/cache poisoning candidates need complete chain and version evidence; do not fire desynchronization tests at production or shared infrastructure without separate explicit scope and safe facilities. Use maintained parsers rather than handwritten fixes.

## Cache isolation

Private responses, auth/session flows and signed downloads need explicit cache policy that survives browser, service worker, proxy, application and CDN layers. Assess tenant/user/role/locale/origin keys and `Vary`, authorization responses and conditional requests/ETags. Test using two owned users/tenants; a cache hit is not evidence of leakage unless another identity receives protected content. “Do not cache cookies” is not a complete key/policy design.

Avoid caching responses whose permissions can change without a defined invalidation/revalidation policy. Check error caching, content negotiation, unkeyed headers/query parameters and path normalization mismatches that might permit cache deception or poisoning. Check whether a stale read can re-grant revoked permissions. Low cache hit ratio is a performance observation, not itself a vulnerability.

## WebSockets, SSE, long polling and streaming

Authenticate establishment, validate browser origins where relevant, and authorize each channel/resource/action. Include tenant isolation, message validation/size, connection quotas, reauthentication/revocation, reconnection/resume IDs and bounded buffers. Confirm a lost role or session actually stops future protected delivery; a still-open connection may outlive HTTP middleware checks.

Cloudflare/WAF behavior at the HTTP upgrade is not per-message application authorization. A reverse proxy or CDN for HTTPS does not automatically protect unrelated TCP/UDP media/services. For SSE or streamed responses, test cancellation, backpressure, buffering/flush behavior, errors after headers, resource cleanup and token leakage in URLs. Framework streaming support is not a proof of secure lifecycle handling. Long-lived workers/services must enforce the same authorization invariant across instances.

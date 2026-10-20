# Files, outbound requests and integrations

Use the relevant OWASP SSRF, File Upload, Path Traversal, Secrets and vendor webhook references in [sources](sources.md). A public WAF does not necessarily observe the server's outbound fetches or background file processing.

## SSRF and external fetches

Inventory URL importers, previews, image/PDF renderers, document converters, callbacks, webhooks configured by users and AI tools that fetch URLs. Prefer fixed trusted integrations or narrowly defined destination/scheme/port allowlists. For user-selected URLs, validate parsed destinations, all relevant resolved IPv4/IPv6 addresses and each redirect; protect against private/link-local/loopback access, alternative representations, DNS rebinding and credentials in URLs. A hostname regex or preflight DNS check alone does not ensure the actual connection reaches the approved address.

Enforce the policy in the actual HTTP client/transport, including redirect and proxy behavior, preserving TLS hostname/certificate checks when connecting to validated addresses. Add egress network restrictions, response/time/redirect/decompression limits and no credential forwarding to untrusted destinations. Cover both synchronous handlers and workers. Do not test against real metadata endpoints or arbitrary internal hosts; use a local controlled fixture and report assumptions when runtime tests are unavailable.

## Paths, archives and uploads

Prefer object identifiers resolved by a trusted storage layer to arbitrary user paths. For filesystem use, enforce the allowed root on the final effective path and review decoding, symlinks, races and platform-specific separators. String prefix comparisons without a path boundary are not sufficient. Avoid archive extraction paths outside the intended directory and bound entry counts, expanded size, nesting and decompression ratio.

Authorize upload initiation, object association, download, replacement and deletion. Verify extension policy, declared and detected content type, safe parser behavior, size, quotas and filename generation; no single MIME/extension check proves content is safe. Process risky formats in a constrained environment. Use private storage by default, and serve active user content from an isolated origin with appropriate content type/disposition and no privileged application cookies. Antivirus scanning can complement isolation but is not a guarantee.

For public storage, distinguish intentionally public assets from accidental exposure of private objects. Review bucket/object policies, ACLs when used, access logging and account roles rather than assuming one “private” setting covers everything. Presigned URLs are bearer capabilities: gate issuance by resource/tenant/operation, limit scope/expiry, prevent logs/referrers from leaking them, and document provider-specific revocation limits. Expiry does not authorize issue to the wrong user.

## Webhooks and state changes

Use the provider's actual versioned signature scheme/library and compare as specified, commonly against the original raw body before transformations. Bind signatures to the intended endpoint/context when supported. Apply timestamp windows with bounded clock tolerance and replay protection where relevant, keeping retry semantics intact. A timestamp check alone is not event deduplication.

Process deduplication and business state atomically with a durable unique event/operation key scoped to the provider/account. Acknowledge only according to the verified provider contract and make retries safe after partial failures. Use transaction/outbox coordination when a committed state change must produce an event. Do not fulfill a payment from an unverified callback body or client redirect. Secret overlap/rotation must follow verified provider behavior; never rotate live signing keys as a review side effect.

## Other integration boundaries

Check outbound credentials, least-privilege scopes, TLS verification, timeouts, retry policy, idempotency, response schema and trusted endpoint ownership. Validate redirects and imported data; a third-party success response does not authorize a local privileged change. Avoid logging provider payloads that contain personal data or tokens. Review email-link creation for trusted public origins rather than attacker-controlled Host headers. SPF/DKIM/DMARC help mail-domain authentication but do not authorize application requests; deploy DNS changes cautiously and verify actual senders.

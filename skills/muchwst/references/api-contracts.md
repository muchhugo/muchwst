# API disclosure, validation and output safety

Related reading: [identity/authorization](identity.md), [input/rendering](inputs-browser.md), [browser storage](browser-storage.md) and [protocols/caching](protocols-realtime.md). Sources: OWASP REST Security, Input Validation, XSS, Logging and API Security plus IETF HTTP and Problem Details pointers in [sources](sources.md). Schemas document/enforce shape only when actually executed; they do not establish authorization or safe output by themselves.

## Minimize what crosses the boundary

Trace request identity and requested fields through the query, model, serializer/DTO, response schema, actual HTTP body, headers, client hydration, logs and caches. Prefer explicit allowlists of returned fields appropriate to the endpoint and role. Do not serialize a complete database/ORM entity and rely on removing a few sensitive keys. A new column, nested relationship or exception object can bypass such a blacklist. Limit both fields fetched and fields serialized where feasible.

Exclude password hashes/salts where unnecessary, reset/verification tokens, provider credentials, signing material, session/refresh tokens outside their intended delivery channel, private internal notes, unnecessary emails/PII, infrastructure paths and debug internals. Not every ID, email or timestamp is intrinsically forbidden: disclose it only for a legitimate authorized contract, not by accident. Check nested objects, pagination totals, exports, admin/support tools, search suggestions, GraphQL fields, real-time messages and error branches too.

Authorize at **function, object and property** levels on the server. A user allowed to see a resource may not be allowed to read its billing/internal fields or change its owner/role. Use explicit writable-field schemas for mass assignment; the server assigns trusted actor, tenant, price, permissions and derived state. A client-side schema or a hidden form field does not constrain a caller using raw requests.

Test the actual serialized response with two roles/two tenants and forbidden-field assertions. Ensure legitimate fields still work. A type definition or snapshot that never exercises the handler is not sufficient proof. Avoid logging a full response body just to prove a sensitive field is absent; use synthetic records and redacted assertions.

## Errors and response contracts

Keep stable public error codes and safe messages, consistent semantics and a non-sensitive support/correlation ID when useful. Keep stack traces, SQL, connection strings, paths, dependency versions, raw third-party errors, credentials and private user data out of public errors. Record needed operational detail privately with access/retention limits and redaction. A request ID must not encode a secret or sensitive identity.

Use appropriate HTTP semantics: missing/invalid authentication commonly differs from forbidden access, malformed input, conflict or throttling. Use a deliberate not-found policy where resource existence must be concealed. Do not normalize all failures to `200`, or return vague errors that cause a client to treat an operation as successful. Sensitive login/recovery/enrollment flows may require intentionally uniform outward responses to avoid account enumeration; inspect body, status, timing and other observable effects together.

A consistent success/error envelope or Problem Details format can help, but no single envelope is mandatory. Additional `detail`, validation-error or debugging fields must not expose rejected secrets or internals. Validate the actual production error handler and framework debug mode. After a streaming response has started, report errors through the documented safe protocol rather than append raw exceptions.

Set correct content type, avoid dangerous content sniffing, and protect sensitive response caching and referrers. Do not send bearer tokens in URLs, redirects or analytics. Headers, `Location`, signed URLs, ETags and timing can disclose information too. A minimized JSON body alone is not complete disclosure protection.

## Validate, sanitize and encode: different jobs

1. **Parse and validate input:** enforce content type, schema, allowed keys, types, bounds, units, maximum lengths/depth/items, enums and business constraints on the server. Apply resource limits before expensive parsing, hashing, decompression or execution when possible. Reject or intentionally handle duplicates/ambiguity and cross-layer decoding disagreements. Validate parameters, query, body, headers, uploads, queue messages, webhook data and restored browser state at their real trust boundaries.
2. **Normalize only with a defined contract:** handle Unicode, case and canonical formats consistently where the business meaning requires it. Never silently trim/change passwords, opaque tokens, signature bytes or identifiers with exact semantics. Verify webhook signatures using the provider's required raw bytes before any destructive transformation.
3. **Sanitize allowed rich content:** when users may submit HTML or similar active content, use a maintained parser/sanitizer with explicit element/attribute/URL policies. Test relevant renderer/parser versions. Don't “sanitize everything” with regex or delete punctuation from every string; that can corrupt data while missing the exploitable context.
4. **Encode or render safely at the sink:** use context-appropriate HTML/attribute/URL/JavaScript/CSS rendering and framework-safe JSON-in-HTML serialization. For plain text, use safe text APIs rather than raw HTML. Valid JSON served as JSON is different from that JSON embedded in a script element. Avoid escaping twice or storing one presentation-specific escaping as the canonical raw value unless the contract requires it.
5. **Use safe APIs for execution:** parameterized SQL values, validated identifiers, structured non-shell process calls and safe deserialization modes. HTML sanitization does not prevent SQL injection; SQL binding does not prevent XSS. Authorization remains a separate required check.

Apply trust-boundary rules deliberately, not by adding redundant validation everywhere without understanding the data flow. Output schemas/DTOs enforce a public contract and minimize fields; they do not make every included string safe for every browser sink. Centralize shared validation/serialization while preserving per-role/per-operation policy.

## Useful regression matrix

Use synthetic allowed/forbidden fields and controlled identities. Cover unknown/nested fields, oversized input, null/absent/incorrect types, exact byte-sensitive values, malicious markup versus legitimate text, cross-tenant identifiers, unauthorized role fields, validation failures and internal exceptions. Test actual cookie/token/error/cache behavior, not only helper functions. Check direct HTTP calls without frontend validation and permitted UI flows after the patch. Record which cases were executed and which are proposed.

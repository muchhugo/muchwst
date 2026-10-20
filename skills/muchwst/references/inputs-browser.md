# Input processing and browser trust boundaries

Reference pointers: OWASP injection, XSS, CSRF, input-validation, CSP and HTTP-header guidance in [sources](sources.md). Verify the actual framework and version; do not assume escaping, request parsing or middleware defaults.

## Injection and validation

Trace SQL inputs to the executed query. Parameterize values through the driver/ORM; allowlist dynamic identifiers/order clauses that cannot be bound as values. An ORM can still contain unsafe raw queries; use of an ORM or string concatenation alone is not the finding. Include NoSQL operators, shell commands, templates, expression engines, LDAP/XML parsers and unsafe deserialization when present. Prefer non-shell structured APIs and maintained safe parser modes over custom escaping.

Validate schema, types, sizes, ranges, enums, nested depth, allowed fields and business invariants at each trust boundary. Reject or intentionally handle duplicate keys, ambiguous encodings, prototype-mutating keys and parser disagreement relevant to the stack. Canonicalize with a defined policy; avoid repeated decoding that turns previously safe strings into instructions. Output encoding and authorization are separate from input validation. Do not “sanitize everything” with one regex or escape data prematurely in storage.

## XSS and content rendering

Distinguish stored, reflected and DOM-based paths. Inspect rich text/Markdown, HTML injection APIs, template raw-output escapes, browser URL/navigation sinks, SVG, embeds, attributes, event handlers and DOM/`postMessage` data. Apply context-correct output encoding; use a maintained sanitizer with explicit element/attribute/URL policies when users intentionally supply markup. Validate message origin/source and message schema; never treat messages from any window as trusted commands.

Check actual auto-escaping and sanitized types before reporting a candidate. HTML encoding is not JavaScript/CSS/URL safety. JSON serialized into HTML needs framework-safe embedding. Content Security Policy is defense in depth, not a substitute for safe rendering. Use harmless local markers or owned test records for authorized reproduction, not data-stealing scripts or real user sessions.

## CSRF and CORS are different controls

CSRF concerns actions using ambient credentials, commonly cookies. Assess login, logout and state-changing endpoints as well as obvious form submissions. Use appropriate CSRF tokens/session-bound patterns and origin checks with understood proxy trust; `SameSite` is complementary and must fit legitimate cross-site flows. Avoid state-changing GET semantics. JSON content type alone is not a universal defense; inspect accepted parsers, simple requests, overrides and actual credential behavior. A bearer-token API may have different exposure, but check whether cookies or fallback auth are still accepted.

CORS governs browser cross-origin access; it is not authentication, general API access control or protection against non-browser clients. A public resource may legitimately use a wildcard origin. To establish a vulnerability, show how an untrusted origin can read or act on protected data with the relevant credentials/flow. Check exact origin matching, reflected origins, `null`, subdomain ownership and credential settings. Browsers reject some invalid wildcard/credential combinations; a header string alone does not prove data theft. Preflight restrictions do not prevent every simple request. Where responses vary by allowed origin, verify caching and `Vary` behavior.

## Browser controls and headers

Evaluate clickjacking through CSP `frame-ancestors` and compatible framing controls according to intended embedding. Apply appropriate content types, `X-Content-Type-Options`, referrer policy and cookie flags. Document omissions as hardening unless there is an evidenced attack path. Do not impose obsolete HPKP or legacy browser XSS-filter requirements as modern universal controls.

Design CSP from actual script/style/connect/frame needs. Per-response nonces must be unpredictable and correctly scoped; static reused nonces do not provide the intended property. Test report-only before an authorized enforce rollout where useful, and remember report-only does not block execution. Avoid broad unsafe exceptions without a reason. Protect the reporting endpoint and redact URLs/tokens. Cross-origin isolation headers such as COOP/COEP/CORP need feature compatibility tests, including login popups and embeds; don't enable them indiscriminately.

HSTS affects future browser behavior and requires verified HTTPS. `includeSubDomains` and preload require inventory and separate approval; they can break forgotten subdomains and cannot be undone instantly for clients with stored policy. Check the response that actually reaches the browser through the CDN/proxy. Do not duplicate conflicting policies across layers.

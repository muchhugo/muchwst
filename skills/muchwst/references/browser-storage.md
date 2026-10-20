# Browser storage, cookies and token lifecycle

Read this for browser authentication, token refresh, account switching, client persistence and offline features. Related references: [identity](identity.md), [API contracts](api-contracts.md), [browser input/rendering](inputs-browser.md), and the OWASP Session Management/HTML5 and browser documentation pointers in [sources](sources.md). Verify the actual browser/framework behavior; no storage choice makes an application immune to XSS, CSRF, a malicious extension or a compromised device.

## Inventory before prescribing a location

Trace every write/read of cookies, `localStorage`, `sessionStorage`, IndexedDB, Cache Storage, service workers, in-memory stores, persisted state libraries, URL parameters/fragments, `history.state`, hydration payloads and cross-tab messages. Record field purpose, sensitivity, identity/tenant, access by scripts/server, lifetime, encryption/key location, and behavior at refresh, logout, role changes and account switching. A storage wrapper or library does not remove this requirement.

| Material | Starting recommendation, subject to the actual architecture | What to prove |
| --- | --- | --- |
| Theme, language and non-sensitive UI preferences | `localStorage` is often appropriate | Treat restored values as untrusted; bound/validate them; no authority over identity, role, price or permissions |
| Temporary non-sensitive tab state | Memory or `sessionStorage` when persistence is useful | Tab-scoped lifetime is not confidentiality; sensitive drafts need an explicit shared-device/offline policy |
| First-party browser session | Prefer an opaque session identifier in a server-set cookie with appropriate flags and server-side session state, or an established equivalent design | CSRF controls, regeneration, expiry/revocation, narrow scope, trusted HTTPS and application compatibility |
| Browser OAuth/OIDC tokens behind a backend-for-frontend (BFF) | Prefer provider tokens held on the backend and a protected browser session cookie where the architecture allows it | BFF/session security, CSRF and no accidental tokens in browser JSON/hydration/logging |
| Access bearer token in a browser-only/direct API design | Prefer short-lived memory storage when feasible; document the reload/refresh flow and residual XSS exposure | An in-memory token can still be used/exfiltrated by active injected script; do not call it XSS-proof |
| Refresh token in a first-party browser flow | Prefer backend-held refresh state or a narrowly scoped server-set `HttpOnly`, `Secure` cookie when appropriate | Rotation, absolute/idle expiry as designed, replay handling, atomic multi-tab refresh, CSRF on refresh/logout and revocation |
| API secrets, password hashes, private signing keys or provider service credentials | Never intentionally deliver server secrets to browser storage or client bundles | Check build-time public variables, source maps, serialized state, caches and debugging output as well as source |
| CSRF token and OAuth transaction state/PKCE verifier | Use the maintained framework/flow's intentional short-lived design | Some values must be readable by legitimate client code; don't move every item named “token” to HttpOnly and break the defense/flow |
| User content, offline drafts or encrypted client data | Minimize; require a product-specific sensitivity/offline/shared-device/key-recovery policy | Persistence and key access determine the risk; client encryption with a key accessible to the same injected script is not an XSS defense |

These are recommendations, not a rule that every JWT belongs in a cookie. Native/mobile/desktop clients have different storage and credential boundaries; do not force a browser-cookie design onto them. A browser-only OAuth application that cannot use a BFF needs explicit residual-risk analysis and provider-supported protections, not an impossible promise of secrecy from same-origin script.

`localStorage`, `sessionStorage` and IndexedDB are accessible to permitted same-origin JavaScript; `sessionStorage` is not a secure vault merely because it is scoped to a tab. Any permitted script or relevant XSS can compromise accessible credentials. Moving a token between these stores does not fix the underlying XSS. Browser storage values can also be edited by the user; never trust a restored role, tenant, identity, entitlement or price on the server.

## Cookie review

Prefer server-set cookies for session/refresh credentials so `HttpOnly` can apply. Inspect `Secure`, `HttpOnly`, `SameSite`, name/prefix, Domain, Path, expiration and browser behavior in the actual first-party or cross-site flow. Use host-only scope when possible; avoid broad parent-domain cookies that unnecessarily trust subdomains. Path reduces where cookies are sent but is not a robust isolation boundary between mutually untrusted applications on the same host.

`HttpOnly` prevents ordinary JavaScript from reading the cookie value; it does not stop injected scripts from performing authenticated actions. `Secure` restricts transmission to secure channels; it is not encryption of browser storage at rest. `SameSite` is based on sites, not exact origins; sibling subdomains may still require explicit trust/CSRF review. Legitimate cross-site login, embeds and integrations need tested policy rather than blanket `Strict`. Where `SameSite=None` is actually needed, validate required flags and current browser behavior instead of assuming credentials will always be available.

Use cookie prefixes only according to their verified semantics and requirements. Check session regeneration on login/elevation, shadowed/duplicate cookie names, correct deletion scope and explicit expiry. Don't prescribe a fixed session length for every product. Validate the resulting `Set-Cookie` and effective behavior through CDN/proxy/browser, including errors, redirects and refresh responses. Never weaken TLS to make cookies work locally; use an explicit isolated development configuration.

## JWT and refresh-token handling

A signed JWT's payload is normally readable; a signature is not encryption. Do not include passwords, hashes, API secrets or unnecessary personal/internal data in claims. Validate signature, purpose, trusted issuer, audience, expiry and bounded clock skew before using claims. Do not accept a decoded token as authentication, an ID token as an arbitrary API access token, or a valid historical role claim as proof of current permission when revocation requirements demand fresh state.

For opaque local refresh tokens, prefer storing a suitable non-reversible server-side verifier rather than plaintext where lookup/validation permits it; provider tokens that must be presented to another system need protected recoverable storage instead. Bind family/actor/client metadata as the design requires. Make rotation and replay/family-reuse decisions atomic and persistent across instances. A distributed cache may assist but should not accidentally erase revocation truth on eviction. Document and test any concurrency grace policy; two legitimate tabs must not cause endless renewal or accidental permanent lockout.

Review renewal failures, logout, password reset, account disable/removal, lost MFA and signing-key rotation. Verify server-side invalidation in addition to deleting local values. Cookie deletion alone does not revoke a copied credential; expiry alone may not meet the required revocation interval. Do not rotate live keys as an incidental review action.

## Persistence, caches and logout

Scope persisted stores, query caches, service-worker responses, BroadcastChannel/postMessage handling and offline queues to the correct identity/tenant. Verify that switching accounts on the same browser cannot show or submit the previous account's data. A pending request or refresh from account A must not overwrite account B's session. Test back navigation, reload, a second tab and reconnection in a controlled environment.

Minimize persistence of protected responses and use appropriate `Cache-Control` through every layer. `Cache-Control: no-store` does not erase existing localStorage/IndexedDB entries, and cookie flags do not protect a cached API body. Clear only application-owned relevant state under the approved logout/data-retention policy. Broad `Clear-Site-Data`, origin-wide cache deletion or shared-cookie deletion can affect other applications; assess and approve that scope instead of deleting all browser data blindly.

## Required review evidence

Provide a storage inventory and data-flow table, the actual cookie configuration, token issuance/refresh/clear paths, server revocation behavior and authorized behavioral tests. Report storage risk in context, with evidence and preconditions. Persistent JS-readable refresh tokens deserve scrutiny, but do not claim a demonstrated XSS or account takeover merely from a storage API call. Keep the recommended architecture and an evidenced exploitable defect clearly distinct.

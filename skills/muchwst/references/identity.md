# Identity, sessions, authorization and abuse

Apply only to real flows. Primary reading pointers: OWASP Authorization, Authentication, Session Management and Password Storage cheat sheets, API Security, ASVS, NIST Digital Identity and IETF/OIDC documents in [sources](sources.md). Pin actual editions for exact control mappings.

## Server-side access decisions

Map actor → operation → resource → tenant → permitted fields → state transition. Check anonymous, ordinary user, resource owner, same-tenant non-owner, other-tenant user, administrator and revoked/disabled identities where those roles exist. Verify both reads and mutations, bulk endpoints, exports, search, downloads, nested resources, invitations, support impersonation, jobs and real-time subscriptions.

Authentication does not authorize the resource. Check IDOR/BOLA, function-level permissions and field-level overexposure/mass assignment. Apply policy on the server for every relevant request and state transition. UUIDs, hidden UI buttons, unpredictable IDs and a frontend role check do not replace object-level authorization. RBAC may need ownership, tenant, relationship or state checks in addition to role membership. Deny by default at the appropriate boundary without accidentally denying permitted flows.

Derive identity/tenant from the verified session and authorized route context, not an untrusted body/header alone. Verify a selected tenant actually belongs to the actor. Scope queries to accessible objects or use an equivalent central policy, and use explicit allowlists of writable/serializable fields. Trace shared guards before reporting a missing check. Database RLS can be useful but is not mandatory for every architecture; when used, inspect the actual runtime role, bypass paths, policies and pooled connection context with `muchwst-data`.

Test loss of access as well as initial access: password/session reset, role changes, removal from a tenant, logout, disabled account, key revocation and already-open subscriptions. A checked JWT at connection time may leave a removed member subscribed indefinitely. Decide the revocation guarantee from product requirements and verify the full delivery path; don't promise instantaneous global revocation without evidence.

## Credentials and password lifecycle

Use maintained password-hashing libraries and version-appropriate, benchmarked work factors. Argon2id is a candidate when supported; evaluate an existing bcrypt deployment rather than replace it blindly. Check implementation-specific bcrypt byte-length limits and reject or intentionally handle oversized input without silent truncation. Do not replace password hashing with a fast general hash, reversible encryption or a custom cryptosystem.

Use independently generated salts through the library; a salt is not a secret. A pepper is an optional separate secret with its own rotation/recovery implications. Rehash safely upon successful authentication when policy changes. Bound hashing work and input length to avoid turning a costly verifier into a resource-exhaustion path; rate-limit attempts without exposing per-user status.

Review enrollment, recovery, email/phone changes, reset-token entropy/single use/expiry, reauthentication for sensitive changes, notifications and revocation of affected sessions. Recovery must not bypass the intended authentication assurance. Avoid logging secrets and avoid leaking account existence through response bodies, status, timing, delivery behavior or different rate limits. Timing claims require repeatable bounded evidence, not one slow request. Prefer library constant-time comparisons for fixed-format secrets; this does not equalize an entire endpoint automatically.

MFA/passkeys require secure setup, challenge binding, expiry, origin/relying-party validation where applicable, rate limits, recovery and removal controls. Missing MFA is a risk-dependent hardening issue, not automatically a high-severity defect in every app. Keep administrator access and high-risk actions explicit. Do not weaken recovery merely to pass a test.

## Sessions, JWTs and refresh flows

For cookies, inspect `Secure`, `HttpOnly`, appropriate `SameSite`, lifetime and narrow domain/path according to the actual flow. Check session ID regeneration after login/privilege elevation to prevent fixation; invalidate old sessions according to policy. Cookie flags are complementary and do not replace CSRF or access control.

Validate JWT signatures with an allowed algorithm/key type, issuer, audience, expiry and other applicable claims, using bounded clock tolerance. Decoding is not validation. Do not trust attacker-selected key URLs/algorithms; constrain discovery/JWKS to verified issuers and handle key changes safely. Keep ID tokens separate from access tokens and purpose-bind tokens. Claims cached in a valid token may not satisfy current authorization/revocation requirements.

Review refresh-token storage, rotation, expiry, replay/family-reuse handling and revocation. Concurrent refreshes across tabs/instances need an atomic, intentional policy that does not create unlimited reusable tokens or accidental account lockouts. Document any grace window and prove its bounds. Avoid bearer tokens in URLs, browser logs, analytics and persistent insecure storage; evaluate storage choices against both XSS and CSRF rather than applying a slogan.

## OAuth and OpenID Connect

Use maintained libraries and the deployed provider's verified flow. Check authorization-code flows, PKCE where required/applicable, exact registered redirect handling, state/session binding, OIDC nonce and issuer/audience validation. An ID token or unverified email is not arbitrary permission to link an existing account. Protect account linking/unlinking and issuer mix-up paths. Treat provider metadata and redirects as trust boundaries. Neither OAuth nor OIDC removes local resource authorization.

## Business logic and abuse

Review membership invites, coupon/redemption limits, refunds, subscriptions, ownership transfers, consent, quotas and privileged support operations. The server derives prices/currency/entitlements; clients do not choose them. Tie paid entitlements to verified payment events and idempotent state transitions. Rate limits should reflect actor/resource/action and real shared IP behavior; IP-only throttles and CAPTCHA do not establish identity. Include concurrency/replay, archived/deleted objects and failure-state tests when applicable. Use `muchwst-data` for atomic invariants.

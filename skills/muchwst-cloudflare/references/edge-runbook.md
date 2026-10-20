# Cloudflare edge and origin runbook

Use [sources](sources.md) for official vendor pointers. Their current content and plan availability are not bundled verification. Inspect actual scope/permissions, plan, zone, active products, ruleset versions and request flow before recommending exact expressions, API calls or dashboard actions. Never embed static provider CIDRs, stale managed-rule identifiers or invented bot-score access.

## 1. Topology and origin protection

Inventory proxied and DNS-only hostnames, A/AAAA/CNAME paths, old/subdomain records, Workers/routes and exposed origin services from authorized sources. A proxied DNS record does not close the origin's public ports. Avoid expanding into reconnaissance of unknown hosts. Check known approved direct-origin routes with bounded owned probes only if testing is authorized.

Protect web ingress with appropriate network restrictions plus origin authentication/routing where required. Use current published IPv4/IPv6 ranges only after verification if source filtering is chosen; plan updates and recovery so a stale list cannot lock out valid traffic. Limit them to relevant service ports, not every service. A source IP associated with a shared proxy network does not alone authenticate the user's zone. Verify the supported origin authentication design and how it binds requests to the intended application/hostname.

For Authenticated Origin Pulls or an equivalent, inspect whether the configured certificate/trust model uniquely binds the intended deployment; a broadly shared trust root/certificate is not automatically exclusive to one zone. Cloudflare Tunnel may reduce public origin exposure when deliberately selected, but requires connector identity/access/routing controls and verification that alternate public listeners are not still open. Neither mechanism should be prescribed as a universal one-click fix.

Restrict default vhosts and intended Host/SNI routing. Protect SSH, database, cache, media and unrelated TCP/UDP services independently; ordinary proxied HTTP/HTTPS does not automatically protect them. Preserve needed operator, monitoring and renewal paths without making a broad bypass accessible to untrusted traffic.

## 2. TLS and browser transport

Verify browser-to-edge and edge-to-origin separately. Prefer authenticated, certificate-validated encryption to the origin; assess the actual Full (strict) or equivalent configuration, certificate name/trust/expiry and renewal. Flexible/unencrypted-origin arrangements cannot be described as end-to-end HTTPS. An Origin CA certificate and a public browser-trusted certificate have different intended trust paths; don't expose an origin directly and assume browsers will trust it.

Deploy HTTPS redirects and HSTS only after mapping the actual route and subdomains. HSTS includeSubDomains/preload needs explicit approval, compatibility and recovery analysis; removing a header does not instantly undo browser-stored/preloaded state. Keep one coherent effective header policy across edge, Workers, proxy and application.

## 3. WAF, scanners and bots

Inspect existing managed/custom rules, execution order/phases, skip/bypass rules, URL decoding/normalization and log evidence before writing new controls. Start with vulnerability-specific mitigations and known unwanted exposure, plus route-sensitive request limits. Deny unintended access to environment/repository/backup files only after ensuring the route/pattern is truly unintended and the normalized path matches what the origin serves. A WAF deny is defense in depth; remove the accidentally served file or unsafe route at the origin too.

Avoid blanket user-agent blocking, all-CLI bans, broad country/ASN deny lists or assuming residential/bot classifications are infallible. Such measures may reduce noise but can block legitimate integrations, privacy tools, accessibility tools and users. Tie actions to supported signals, route risk, observed abuse and a verified application need. Record false positives, expiry/review and unblock procedures.

Use managed challenges only on routes/clients that can complete them. APIs, native clients, webhooks, health checks and WebSocket/SSE flows may not support browser challenges. Design narrow, verified service authentication and route-specific limits instead. Do not create broad “skip all security” rules for an API or trust a request-supplied secret header without considering exposure and origin enforcement. A legitimate integration exception must be specific and authenticated as appropriate, not just `User-Agent contains provider`.

Managed-rule updates and emergency virtual patches can change behavior; document rule/version/phase evidence and review expiration. Do not claim a clean WAF dashboard means no vulnerability or incident. Do not generate hostile scanner traffic at a public service solely to exercise a rule.

## 4. Rate limits and cost controls

Define the protected operation and resource: login/recovery, search/export, upload/conversion, billing, connection establishment or AI inference. Set thresholds from observed legitimate workloads and explicit safety budgets, not one global requests-per-minute number. Aggregate per actor/tenant/resource where supported and privacy-appropriate, while considering shared IPs, NAT, proxy spoofing, IPv6 rotation and distributed instances.

Check exact feature/plan support before using bot scores, counting fields, advanced expressions, log mode or rate-limit windows. If unavailable, report the limitation and propose supported application/proxy controls rather than invent availability. Edge limits reduce incoming pressure; application limits must still protect authenticated expensive operations, direct ingress and asynchronous costs. Budget alerts notify and may lag; they are not hard spending caps unless the provider explicitly implements such a control.

## 5. Trust forwarded headers correctly

Only trust `CF-Connecting-IP`, `X-Forwarded-For`, scheme/Host or equivalent fields on the verified trusted ingress path. Restrict direct-origin access and configure the framework/proxy's trusted-hop handling correctly. Account for Workers or internal subrequests and documented header transformations. A caller bypassing the edge must not forge a trusted IP to evade limits or cause a victim's IP to be banned. Test both edge and approved direct/private paths, not only a header printout.

## 6. Cache and disclosure

Inventory Cache Rules/page rules, Workers and origin response policies. Bypass shared caching for authenticated/private/session/reset responses unless a specifically justified partitioned design has been proven. Verify cookie/auth query/header behavior, cache keys, `Vary`, ETags, redirects and error caching with two owned identities. Do not assume that a Set-Cookie header or a browser `no-store` policy automatically defeats every custom Worker or edge override.

Check cache deception/poisoning candidates against normalization and origin route interpretation. Signed URLs are credentials/capabilities; cache scope and logs must respect their contract. A cache purge is an operational action with availability/cost impact, and cannot revoke information already disclosed. Inspect response headers after all transformations; client-side inspection alone cannot establish origin policy.

## 7. Rollout and verification

Preserve a sanitized before-state, actual rule IDs/order/config revision, known legitimate fixtures, test plan, owner, exact rollback and monitoring windows. Rule syntax acceptance is not semantic correctness. Test normal browser login/recovery, authorized APIs, payment/provider webhook delivery, allowed crawlers when intentional, file upload/download, health checks and real-time reconnects as relevant. Include false-positive observations, configuration conflicts and supported status/log evidence.

Use staged enforcement with the features actually available. External requests and real provider transactions remain separately scoped. A dashboard acknowledgment is not an end-to-end test; distinguish saved, deployed and observed-active configuration. Keep the original code finding `mitigated` until an appropriate source fix and retest justify a different state. Never remove production defenses to obtain a more dramatic reproduction.

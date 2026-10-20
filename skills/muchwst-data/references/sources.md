# Source catalog and freshness policy

**Verification status:** these are recognized reference pointers supplied from established knowledge. Their live contents, newest editions, current advisories, vendor feature availability and external-link reachability were **not fetched or verified during creation of this bundle** because web search was unavailable. This catalog is not a claim that every linked control was consulted. Do not invent a retrieval date or call an edition “latest”.

At assessment time, use authorized browsing or verified versioned local copies. Record publisher, URL/file, edition/revision, retrieval date when actually retrieved, relevant section and applicability. Prefer primary sources for API behavior, vendor advisories and framework defaults. If browsing remains unavailable, continue source-based review, use installed source/types and label freshness limits. Do not assert the absence of current CVEs, legal compliance or support for a Cloudflare feature without current evidence.

## Independent and institutional references

| Reference | Use | Pointer |
| --- | --- | --- |
| OWASP ASVS | Select applicable application security requirements; pin edition before requirement IDs or coverage claims | https://owasp.org/www-project-application-security-verification-standard/ |
| OWASP WSTG | Structured testing methods; run only authorized applicable tests | https://owasp.org/www-project-web-security-testing-guide/ |
| OWASP Cheat Sheet Series | Implementation guidance for auth, sessions, authorization, injection, SSRF, files, cryptography and logging | https://cheatsheetseries.owasp.org/ |
| OWASP API Security project | API authorization, resource consumption, inventory and trust boundaries | https://owasp.org/www-project-api-security/ |
| OWASP Top Ten | Awareness and risk grouping, not a complete verification specification | https://owasp.org/www-project-top-ten/ |
| OWASP SAMM | Security practice improvement, not an individual vulnerability score | https://owaspsamm.org/ |
| OWASP GenAI Security Project | LLM/agent threat considerations; verify project taxonomy/version when used | https://genai.owasp.org/ |
| MITRE CWE | Root-cause classification; verify exact weakness and mapping | https://cwe.mitre.org/ |
| FIRST CVSS | Optional standardized severity vectors; score separately from business priority | https://www.first.org/cvss/ |
| NIST SSDF, SP 800-218 | Secure development practices and supply-chain processes | https://csrc.nist.gov/publications/detail/sp/800-218/final |
| NIST Digital Identity Guidelines | Authentication, credential and lifecycle guidance; verify applicable publication/revision | https://csrc.nist.gov/projects/digital-identity-guidelines |
| NIST Cybersecurity Framework | Risk, governance, response and recovery context | https://www.nist.gov/cyberframework |
| CISA Secure by Design | Root-cause prevention, secure defaults and product accountability | https://www.cisa.gov/securebydesign |
| CISA Known Exploited Vulnerabilities | Current exploitation prioritization only after a dated live/catalog check | https://www.cisa.gov/known-exploited-vulnerabilities-catalog |
| CIS Benchmarks | Platform-specific hardening baseline; verify version, applicability and licensing before using control text | https://www.cisecurity.org/cis-benchmarks |
| SEI CERT secure coding | Language-specific coding failure modes and defenses | https://wiki.sei.cmu.edu/confluence/display/seccode/SEI+CERT+Coding+Standards |
| ANPD | Brazilian privacy guidance when the actual processing requires it; no legal certification implied | https://www.gov.br/anpd/pt-br |

## Specific technical pointers

The following documents identify useful subjects, not a live dependency on a particular revision:

- [OWASP Authorization](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html), [IDOR](https://cheatsheetseries.owasp.org/cheatsheets/Insecure_Direct_Object_Reference_Prevention_Cheat_Sheet.html) and [Session Management](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html).
- [SQL Injection Prevention](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html), [XSS Prevention](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html), [CSRF Prevention](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html) and [SSRF Prevention](https://cheatsheetseries.owasp.org/cheatsheets/Server_Side_Request_Forgery_Prevention_Cheat_Sheet.html).
- [File Upload](https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html), [Password Storage](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html), [Secrets Management](https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html), [Logging](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html) and [HTTP Headers](https://cheatsheetseries.owasp.org/cheatsheets/HTTP_Headers_Cheat_Sheet.html).
- IETF [RFC 9700 — OAuth 2.0 Security Best Current Practice](https://www.rfc-editor.org/rfc/rfc9700), [RFC 8725 — JWT Best Current Practices](https://www.rfc-editor.org/rfc/rfc8725), [RFC 9106 — Argon2](https://www.rfc-editor.org/rfc/rfc9106), [RFC 8446 — TLS 1.3](https://www.rfc-editor.org/rfc/rfc8446) and [RFC 9110 — HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110). Exact RFC numbers identify fixed documents; they do not imply no updates or errata exist.
- [OpenID Connect specifications](https://openid.net/developers/specs/): validate issuer, audience, nonce and flow for the actual implementation.
- [PostgreSQL documentation](https://www.postgresql.org/docs/): match server version for RLS, transactions, planner behavior and recovery.
- [OpenSSH manuals](https://www.openssh.com/manual.html), the installed OS/vendor manuals, and [Docker documentation](https://docs.docker.com/): verify service, firewall and container behavior locally.
- [Cloudflare documentation](https://developers.cloudflare.com/), [WAF](https://developers.cloudflare.com/waf/), [SSL/TLS](https://developers.cloudflare.com/ssl/), [Cache](https://developers.cloudflare.com/cache/), [Cloudflare Tunnel](https://developers.cloudflare.com/cloudflare-one/connections/connect-networks/) and [published IP ranges](https://www.cloudflare.com/ips/): verify the user's plan, zone/account settings, exact rule syntax, trust boundary and current address ranges before changes. Do not embed stale CIDR lists in this kit.
- [GitHub security documentation](https://docs.github.com/en/code-security), [OSV](https://osv.dev/) and [OpenSSF](https://openssf.org/): investigate dependency provenance and advisories; a scanner's result still requires reachability/context review.

## Browser storage and API implementation pointers

These links are also **unvisited reading pointers**, not sources claimed as retrieved during authoring:

- [OWASP HTML5 Security](https://cheatsheetseries.owasp.org/cheatsheets/HTML5_Security_Cheat_Sheet.html), [Input Validation](https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html), [REST Security](https://cheatsheetseries.owasp.org/cheatsheets/REST_Security_Cheat_Sheet.html), [Error Handling](https://cheatsheetseries.owasp.org/cheatsheets/Error_Handling_Cheat_Sheet.html) and [Mass Assignment](https://cheatsheetseries.owasp.org/cheatsheets/Mass_Assignment_Cheat_Sheet.html).
- [MDN Web Storage](https://developer.mozilla.org/en-US/docs/Web/API/Web_Storage_API), [Set-Cookie](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie), [Cache-Control](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Cache-Control) and [Clear-Site-Data](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Clear-Site-Data): verify browser support and actual header semantics before recommending a specific deployment change.
- IETF [RFC 9457 — Problem Details for HTTP APIs](https://www.rfc-editor.org/rfc/rfc9457): an optional response-format reference, not an authorization or redaction mechanism.

## Citation practice

Cite a source near a recommendation when that source was actually consulted. Label unvisited catalog entries as suggested reading. Cite concrete repository lines/commit/config and observed tests for findings; general OWASP links cannot prove a target is vulnerable. Without access, report the missing evidence rather than fabricate exact mappings, CVEs, plan limits, laws or dates. This package is not affiliated with, endorsed by, or a substitute for any named institution or the Strix project.

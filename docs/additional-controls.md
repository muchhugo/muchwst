# Supplemental browser/API and web controls

The 250-item matrix preserves the original list. These additions make later user requirements explicit and close common web-surface gaps. They are not claims of a complete OWASP control mapping.

| Added focus | Primary reference | Required review outcome |
| --- | --- | --- |
| Cookies, localStorage, sessionStorage, IndexedDB, memory and service-worker caches | [Browser storage](../skills/muchwst/references/browser-storage.md) | Data/sensitivity/lifetime/authority inventory, not blanket approval of one storage API |
| BFF or opaque browser session versus direct browser bearer tokens | [Browser storage](../skills/muchwst/references/browser-storage.md) | Architecture-specific choice with XSS/CSRF and recovery tradeoffs |
| JWT readable claims, issuance, validation, refresh families and revocation | [Identity](../skills/muchwst/references/identity.md) | Verified signature/purpose/claims and bounded, atomic lifecycle |
| Shared-browser account switching, multiple tabs and stale private caches | [Browser storage](../skills/muchwst/references/browser-storage.md) | No cross-account disclosure or stale refresh overwriting a new account |
| Explicit API response DTOs, nested/property-level authorization and errors | [API contracts](../skills/muchwst/references/api-contracts.md) | Real serialized output includes only authorized necessary fields |
| Server validation, normalization, sanitization and sink encoding | [API contracts](../skills/muchwst/references/api-contracts.md) | Each stage has the right control; exact signed bytes/passwords are not corrupted |
| NoSQL/command/template injection, unsafe deserialization and XML parsers | [Inputs](../skills/muchwst/references/inputs-browser.md) | Trace controlled data to an actual unsafe sink and existing parser defenses |
| OAuth account linking, recovery and privilege revocation | [Identity](../skills/muchwst/references/identity.md) | Verified issuer/identity/action binding and no recovery bypass |
| HTTP parser disagreement, request smuggling, cache poisoning/deception and Host misuse | [Protocols](../skills/muchwst/references/protocols-realtime.md) | Full trusted-hop/configuration evidence; no production desync experiments by default |
| postMessage origin/source/schema and malicious rendered URLs | [Inputs](../skills/muchwst/references/inputs-browser.md) | Data from another window or markup cannot become a privileged command |
| SSRF redirects/DNS changes, archives/symlinks, decompression and upload isolation | [Files](../skills/muchwst/references/files-integrations.md) | Protect actual effective connections/paths and bound risky processing |
| Logs/metrics/traces as disclosure and injection surfaces | [Runtime](../skills/muchwst-runtime/references/runtime-review.md) | Redaction, bounded cardinality, controlled sinks/recipients and integrity |
| Hostile repository/tool content targeting the reviewing agent | [Safety](../shared/safety.md) | No instruction promotion, scope expansion, suppressed reporting or secret exfiltration |
| LGPD and actual Brazilian privacy processing where applicable | [Runtime](../skills/muchwst-runtime/references/runtime-review.md) | Applicable evidence/questions; no unsupported legal or certification claims |

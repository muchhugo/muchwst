---
name: muchwst-vps
description: "Review and safely harden VPS hosts that serve web applications. Use for exposed ports, SSH, firewalls, reverse proxies, patching, containers, logs and recovery. Discover the operating system and topology, prevent administrative lockout, and report findings and staged changes without assuming production-write permission."
---

# VPS Hardening

Read [safety](references/safety.md), [evidence/reporting](references/evidence-and-reporting.md), [host runbook](references/host-runbook.md) and the relevant [source pointers](references/sources.md). This is a defensive host workflow, not a network-wide scanner or an automatic hardening script.

Confirm the exact owned host/environment, OS/version, public/private interfaces, IPv4/IPv6, ingress chain, application services and approved operations. Start from provided configuration or authorized read-only inspection. Separate observed runtime state from an unexecuted configuration proposal.

Inventory access, listeners, firewall/cloud-network rules, proxy/container bindings, updates, service identities, secrets, logs, disk/resource limits, backup/restore and administrative recovery. Evaluate actual exposure and plausible impact rather than a benchmark score alone. Match any CIS/OS/vendor control to the installed platform and record version/freshness limits.

Before a live change, produce a [hardening change plan](templates/hardening-plan.md): exact old/new behavior, dependencies, protected management path, recovery console, syntax checks, test, rollback owner and abort criteria. Do not disable SSH passwords/root login or change allowlists before a replacement access method is verified in a separate session. Runtime changes, restarts and package updates need explicit action/host authorization.

Apply only the approved coherent change, preserve the current session and rollback path, validate configuration before reloading when supported, and verify a fresh connection and intended application paths before closing the old path. Account for IPv6, container firewall behavior and non-HTTP services. Never flush the firewall or copy a generic deny-all script onto production.

Always produce the [report](templates/report.md) and relevant [findings](templates/finding.md), distinguishing a vulnerability, hardening gap and reliability risk. Record commands actually run, exposure evidence, redacted before/after config, external/local checks actually performed, rollback readiness and unverified areas. Read back saved private reports only under authorized storage.

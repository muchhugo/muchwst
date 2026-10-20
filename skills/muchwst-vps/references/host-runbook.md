# Host protection with recoverable changes

Read [safety](safety.md) before tools. Use [sources](sources.md) for installed OS, OpenSSH, container, proxy and applicable CIS guidance. Never assume a firewall manager, service manager, distribution, default port or cloud console exists. Do not download/run an unaudited hardening script.

## 1. Inspect the actual attack surface

Record OS/release/support evidence, kernel/service packages, listener-to-process mapping, interface bindings, cloud firewall/security groups, host firewall, forwarding/NAT, IPv4/IPv6, reverse proxy, containers, tunnels, scheduled jobs and administrative users. Inspect authorized configuration and read-only runtime state; don't expose `.env` values or private keys in reports. A process bound to all interfaces is not automatically public if enforceable network controls block it; prove the full path.

Separate public web ports from SSH, databases, caches, metrics/debug dashboards, queue/admin APIs and media/TCP/UDP services. Databases and caches should not be Internet-accessible by accident. Prefer private/loopback bindings and narrow authenticated access where appropriate. Explicitly record intentionally public services and their application authentication/rate/resource controls. Do not close a UDP media port merely because a generic web-server guide mentions only HTTPS.

A reverse proxy or Cloudflare HTTP proxy is not a firewall for every service on the VPS. Check DNS-only records and direct IP access without scanning unrelated hosts. Restrict the web origin to the intended authenticated ingress/trusted paths where compatible, keeping required health checks and management separate.

## 2. Protect administrator access without lockout

Require an approved recovery path: provider console/rescue, verified access credentials stored appropriately, and an operator who can restore the prior configuration. Test the intended non-root/key-based or approved stronger access in a second session before removing the current method. Limit privileged accounts, review sudo and authorized-key ownership/permissions, and remove stale access only with authorization. Protect against unintended forwarding or agent exposure according to the actual workflows.

Validate the effective SSH configuration, including include files and conditional match blocks, using the installed server's documented validation mechanism before reload. Confirm the actual reload/restart behavior. Never assume a running session proves future login works. Keep management allowlists synchronized with actual operator/VPN addresses, including IPv6. A port change can reduce noise but is not substantive authentication protection.

Require a separately approved scope for account removal, credential rotation, authentication changes or firewall writes. Two-factor and bastion/VPN access are architectural controls to evaluate, not scripts to install automatically. Avoid publishing hostnames/IPs or access rules that reveal a private topology in a public report.

## 3. Firewall and network policy

Choose the actual authoritative manager; do not mix ad hoc iptables/nftables/UFW/cloud rules without understanding precedence and persistence. Inspect effective rules, default policies, established connection handling, egress, forwarding, ICMP/IPv6 needs, container bridges and restart persistence. Some container-published ports traverse paths not protected by the expected host rule; verify end-to-end behavior with the installed stack instead of promising that one firewall covers everything.

Stage allow rules and validate a replacement management path before tightening defaults. Do not flush rules, deny all inbound, disable IPv6 blindly or broadly allow a proxy network to every port. A temporary auto-revert may be useful when deliberately configured and tested with an operator; never claim it exists until it does. Include a bounded external check from an owned authorized source only if remote probing is in scope.

For web origins behind Cloudflare, use the dedicated Cloudflare skill's topology and origin-authentication reasoning when available. Network source filtering alone may not prove requests belong to the intended zone/application. Keep administrative paths independent of broad public proxy IP ranges.

## 4. Patching, services, containers and secrets

Use supported packages and verify actual advisory/patch status when sources are available. Unsupported/EOL claims need dated vendor evidence; don't invent the latest secure version. Plan compatibility, service restarts, reboot and rollback for an approved maintenance change. Unattended updates need an explicit operational policy, not an assumption that every service can reboot safely.

Run services with the least privileges they require. Review filesystem ownership, executable/config write permissions, capabilities, process isolation, exposed Docker socket, privileged containers, mounts and container user. Do not use world-writable permissions or root execution to solve deployment friction. Containers share important host boundaries and are not a blanket security guarantee.

Protect service environment files and mounted secrets with scoped access. Separate deployment/admin credentials from runtime identity and apply least privilege to backups and monitoring agents. Never copy secrets into image layers, public artifacts or debug responses. Non-root and read-only filesystems need compatibility testing; don't break required write paths without providing a constrained replacement.

## 5. Reduce scanner abuse, not legitimate traffic

Limit exposed surface first. Close unused services, disable debug mode, protect administrative routes, deny access to unintended repository/environment/backup artifacts, and enforce request/header/body/decompression/time limits. For suspicious clients, prefer relevant rate/behavior controls and verified narrow patterns to user-agent strings or blanket country/ASN bans. User-Agent is attacker-controlled; “blocked scanners” does not mean the application has no exploitable path.

An SSH/HTTP abuse tool such as Fail2ban or an equivalent may help when deliberately selected, installed and tested. It must parse the correct trusted client address: behind a proxy, banning the proxy can block everyone, while trusting a forged forwarding header can let a caller frame another user. Never automatically ban from untrusted user-supplied log strings. Set expiry, bounded storage, false-positive monitoring and an operator unban/recovery procedure. Don't auto-install a named tool or claim it protects traffic you have not traced.

## 6. Proxy, TLS and runtime limits

Check virtual-host/SNI routing, default vhost, trusted forwarded headers, HTTPS redirects, certificate ownership/expiry/renewal, TLS verification and safe error pages. Test renewal in an authorized non-disruptive environment; do not revoke/reissue live certificates as an inspection step. Keep edge-to-origin encryption/authentication distinct from browser-to-edge TLS.

Use timeouts, request/connection limits, bounded workers/pools and graceful drain appropriate to uploads, WebSockets/SSE and background jobs. A generic short timeout may break valid streaming; removing all timeouts can enable exhaustion. Measure with bounded tests and keep limits differentiated by route/workload.

## 7. Detection and recovery

Retain structured, access-controlled logs with useful request/actor/config change context and redaction; prevent log injection and unbounded disk consumption. Monitor failed auth, unusual privilege changes, blocked traffic, resource saturation, certificate renewal, backups and unexpected listeners. Alerting thresholds need actual workload evidence and an owner; installed software alone does not establish incident coverage.

Backups need separate protected storage, key recovery, retention and restore exercises into an isolated approved target. Report measured recovery times separately from RTO/RPO targets. Preserve evidence during an incident; don't wipe logs, delete suspicious files or reboot blindly in the name of hardening. Containment, forensic acquisition and destructive recovery need an incident plan/authorization.

## Report exit condition

Show assessed versus unknown layers, observed exposure, the risk and evidence for each recommendation, exact approved changes, recovery checks and residual risk. Do not report “VPS secured” from a configuration checklist or local listener output. A configuration proposal is not applied, and a syntax-valid rule is not a verified production control.

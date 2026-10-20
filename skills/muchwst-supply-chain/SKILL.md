---
name: muchwst-supply-chain
description: "Review web project secrets, dependencies, builds, containers, CI/CD and artifact provenance. Use for exposed credentials, vulnerable dependencies, unsafe pull-request workflows and supply-chain risks. Validate reachability and current advisories when available; do not equate an audit alert with a confirmed exploitable defect."
---

# Web Supply Chain Security

Read [safety](references/safety.md), [evidence/reporting](references/evidence-and-reporting.md), [supply-chain checks](references/supply-chain.md) and applicable [sources](references/sources.md). Confirm repository/revision, runtime manifests/lockfiles, build contexts, CI trust boundaries and allowed evidence destinations.

Do not execute an untrusted package script, downloaded scanner, contributor workflow or container build to review it. Start with static inspection and existing verified tools. Any external scanner/service must have explicit permission to receive source, dependency metadata or findings. Never upload secrets.

Trace dependencies from exact installed/locked versions to reachable functionality and deployed artifacts. Check primary advisories and exploitation catalogs only when accessible, recording the date/version/source. With no current advisory access, report that limitation; do not call the dependencies clean or invent a CVE.

For leaked credentials, record sanitized location/fingerprint and scope; do not use the credential to test another service. Separate removing the literal, revoking/rotating, investigating use and cleaning history under an approved procedure. Review build/runtime leakage separately from Git hygiene.

Correct only the requested scope, avoid blind major upgrades, and test actual application contracts. Preserve supply-chain controls and authorized Git workflows. Always emit a [report](templates/report.md) with classified [findings](templates/finding.md), evidence, impact, reproduction or exposure path, fix, verification and residual risk; [JSON Schema](references/report.schema.json) is available.

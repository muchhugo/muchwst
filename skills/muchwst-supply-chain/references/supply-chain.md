# Secrets, dependencies and delivery

Primary reading pointers: OWASP Secrets Management, NIST SSDF, CISA Secure by Design/KEV, OpenSSF, OSV and platform/vendor manuals in [sources](sources.md). Current advisory claims require a dated check; named controls are not a certification.

## Secrets and exposed configuration

Inspect authorized source and relevant Git history only within scope, build contexts, images/layers, generated browser bundles/source maps, CI logs/artifacts, examples, IaC state, backups and runtime logging. Treat `.env`, API keys, signing keys and credentials according to sensitivity. `.env` in `.gitignore` does not remove tracked files/history, stop a Docker COPY, or revoke a leaked key. `.env.example` is acceptable only with nonfunctional placeholders. Frontend “environment variables” included in a bundle are public.

Classify credentials using actual service/documented privileges: some public client identifiers are intentionally public, but must have appropriate server enforcement and scope restrictions. Do not report every token-shaped string as a secret or display the value. Use redacted paths and fingerprints; avoid putting exact secret hashes into public reports when they enable correlation of sensitive incidents.

Plan rotation/revocation with an owner, overlap or failover where supported, affected consumers and post-rotation validation. History rewrite and cache/artifact cleanup need separate authorization and coordination. Encryption at rest does not make runtime or committed plaintext harmless. For encryption, use maintained authenticated schemes and key management appropriate to the threat; protect backups and restore keys separately. Hashing versus encryption is determined by whether recovery is needed and what the secret protects.

## Dependency provenance and reachability

Inventory direct/transitive/runtime/build/dev dependencies, vendored code, plugins and base images from actual manifests and lockfiles. Verify exact package identity, registry/source, ownership/provenance and API existence before adding a package suggested by an AI. Typosquatting, dependency confusion and hallucinated packages are supply-chain risks, not reasons to auto-install a plausible name.

For an advisory, record ecosystem, affected/fixed versions, source/date, actual resolved version, reachable vulnerable behavior, deployment exposure and mitigation. A dev dependency can still execute in a privileged build; a transitive package may be unreachable at runtime. Do not dismiss or confirm solely from those labels. Scanner severity is input to triage, not final application severity. Lockfiles and version pins improve reproducibility but do not automatically establish trust or absence of vulnerabilities.

Choose the smallest maintained compatible fix after reading migration notes and verified APIs. Check for malicious lifecycle scripts before installing in an isolated authorized environment. Do not use audit auto-fix with forced breaking upgrades as a default. SBOMs, signatures, attestations and reproducible builds add evidence but need trusted identities, verification and applicable threat models; absence alone is not automatically Critical.

## CI/CD trust boundaries

Read workflow triggers, permissions, runner trust, scripts, cache/artifact use and repository events. Untrusted fork/PR code must not run with privileged tokens/secrets. In particular, inspect workflows that combine a trusted/base-context trigger with checkout or execution of contributor-controlled content. Prefer minimum token permissions, protected deployment approvals and narrowly scoped short-lived identities where supported.

Verify action/plugin provenance and immutable references when appropriate; a pin must be to an inspected real artifact, never a fabricated SHA. Guard against shell interpolation from branch names, issue/PR titles, artifacts and inputs. Prevent a less-trusted job from poisoning caches/artifacts consumed by privileged jobs. Self-hosted runners and persistent workspaces require isolation/cleanup design; don't erase an operator's workspace during review.

Remote branch protection/rulesets, review requirements and secret scanning settings are governance controls to inspect when authorized. Do not silently change them. A missing rule on a solo project is not a code vulnerability by itself. Review the actual final integrated artifact and protect release credentials; semantic version labels do not prove backward compatibility or security.

## Containers and infrastructure source

Review build context exclusions, multi-stage artifact boundaries, secret mounts rather than copied build arguments/files, users/capabilities, filesystem permissions, rootless/non-root suitability and exposed ports. Multi-stage builds can still leak secrets via copied outputs/cache. Do not publish privileged containers, mount the host socket or make files world-writable as a convenience fix.

Assess image provenance/scanning and patches against the deployed digest/version. Resource limits, network policy and read-only filesystems should match needed behavior. Review IaC state encryption/access and state/plan artifact handling; those files can contain sensitive values even if source variables are marked sensitive. Do not auto-apply Terraform/GitOps plans, alter secrets, or rebuild production while reviewing configuration.

## Licensing and external services

Record dependency-license/provenance questions as governance unless they also introduce a technical security defect. Do not invent legal conclusions. Check which external tools receive source, logs, dependency inventories or model prompts. An AI coding agent or security SaaS is a data-transfer boundary; connection availability is not user approval to upload confidential findings.

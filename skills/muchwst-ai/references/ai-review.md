# LLM, RAG and agent boundaries

Use OWASP GenAI and primary model/tool documentation from [sources](sources.md), recording versions and freshness. This module does not claim current coverage of every AI threat taxonomy or every model's guarantees.

## Prompt injection and tool access

Treat user text, retrieved documents, websites, repository comments, messages, images and tool results as untrusted data. Indirect instructions must not be promoted into privileged system instructions. Test whether an attacker-controlled source can cause unauthorized disclosure or a forbidden tool action, not merely make the model produce an unusual sentence.

Enforce permissions, tenant/resource constraints, allowlisted tool capabilities and validated arguments outside the model. Bind identity to the server session, not tool-generated fields. Revalidate permissions and resource state at execution time. Use explicit confirmation for consequential user actions and prevent a model/tool result from confirming itself. A “do not reveal secrets” prompt or prompt escaping is not an authorization boundary.

Constrain tool egress, file paths, shell/code execution and network destinations with the same web safeguards as other untrusted inputs. Prefer narrowly scoped service APIs to arbitrary command execution. Tool results should not choose unrelated next targets or silently expand the user's scope. Sandboxing must be verified rather than claimed from a library name.

## RAG, memory and output

Enforce retrieval access filters using trusted tenant/actor context before data enters model context; don't retrieve all tenants and ask the model to hide the others. Check document ingestion permissions, embedding/vector namespaces, index deletion and access changes. Scope conversations, memory, prompt caches and output caches to the appropriate users/tenants. Long context windows do not guarantee isolation or instruction retention.

Treat generated HTML, Markdown URLs, SQL, code, email and tool arguments as untrusted output. Use normal contextual rendering/validation and server-side authorization. Don't execute model-generated SQL or package installation directly. Restrict external content fetches, uploads and source citations to avoid SSRF/exfiltration. Redact prompts/logs/evaluation corpora and preserve data-handling/retention constraints for external providers.

## Cost, streaming and evaluation

Bound request/context/output sizes, loop/tool budgets, concurrency, token/time budgets, retries and per-actor cost; handle cancellation, streaming buffers and client disconnects. A frontend limit does not protect a directly called API. Never run unbounded paid evaluations or public fuzz campaigns as part of a skill test.

Pin or record supported model/tool/prompt versions when feasible and explicitly report when a provider alias can change. Evals must cover allowed behavior as well as hostile/indirect input, tenant isolation, tool refusal, error handling and side effects. Repeat nondeterministic cases with a justified bounded budget and preserve failure evidence. Do not claim statistical assurance from one example or a safety boundary from model behavior alone.

Distinguish a model hallucination, unreliable output, policy objection and a genuine exploitable application security issue. Explain the sensitive asset or operation and why independent controls failed. Keep hallucinated-package checks in the supply-chain workflow too, including cases where the coding agent itself is influenced by repository text.

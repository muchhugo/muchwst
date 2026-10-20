---
name: muchwst-ai
description: "Review web applications that expose LLM, RAG or agent features for prompt injection, unauthorized tools, cross-tenant retrieval and cost or data exposure. Use only when AI features are present. Treat model output as untrusted and verify external authorization, validation and side-effect boundaries."
---

# Web AI Security

Read [safety](references/safety.md), [evidence/reporting](references/evidence-and-reporting.md) and [AI checks](references/ai-review.md). Use [sources](references/sources.md) for institution/vendor guidance with verified versions when available. If the web application has no AI surface, report not applicable rather than adding one or auditing every model topic.

Map user input, retrieved content, model context, tools, permissions, memory, outputs, streaming and side effects. Identify what untrusted material can influence and which independent server control constrains it. Do not treat a clever prompt as authorization to access data or execute a tool.

Use synthetic local documents and mock tools to demonstrate a policy violation without leaking secrets or triggering real purchases, emails, cloud writes or external callbacks. Bound inference costs, input/output size, tool steps and retries; record model/tool versions only when actually known. If model access is unavailable, perform code-based boundary review and report runtime/evaluation gaps.

Always produce the [report](templates/report.md) with [findings](templates/finding.md), concrete impact, prompt/context conditions sanitized for reproduction, root-cause fix outside the prompt when needed, regression/eval results and remaining limits. A model refusal or one passing evaluation is not proof that the application boundary is secure. Use [JSON Schema](references/report.schema.json) when structured output is required.

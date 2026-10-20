# Como usar o muchwst

**WST é a abreviação de Web Security Toolkit.** O nome do pacote e da skill principal é `muchwst`. Repositório: [muchhugo/muchwst](https://github.com/muchhugo/muchwst).

São oito skills independentes para revisar aplicações web, corrigir vulnerabilidades confirmadas e avaliar VPS/Cloudflare. A entrada principal é [`muchwst`](../skills/muchwst/SKILL.md). Ela usa as referências pertinentes e encaminha para outras skills apenas quando a aplicação exigir. Não abre oito subagentes automaticamente e não precisa de uma stack específica.

## Usar agora sem instalação

Disponibilize esta pasta ao agente pelo checkout local ou por um conector autorizado. No projeto que será revisado, envie:

```text
Leia skills/muchwst/SKILL.md no pacote muchwst
que disponibilizei e siga suas referências conforme a superfície do projeto.

Faça uma revisão de segurança do projeto atual. Primeiro confira as
instruções locais, stack, versões, branch/hash, alterações pendentes e
fronteiras de confiança. Apresente um plano curto e mantenha um registro
de cobertura. Se o diff estiver truncado, recupere o restante ou registre
a lacuna; não considere que revisou arquivos que não leu.

Esta etapa é de leitura e análise. Não altere produção, VPS, Cloudflare,
credenciais ou dados reais; não faça varreduras externas sem autorização.
Use provas no código e testes locais seguros somente quando estiverem
no escopo autorizado. Diferencie falha comprovada, suspeita e melhoria.

Inclua cookies, localStorage, sessionStorage, IndexedDB, caches, JWT,
refresh, logout, troca de contas, autorização e respostas das APIs.
Avalie dados expostos, validação e codificação/sanitização no contexto
correto, não simplesmente uma limpeza genérica de todas as strings.

No fim, entregue relatório com classificação, evidência, impacto,
pré-requisitos, reprodução segura, resultado observado, sugestão de
correção e teste de regressão. Diga o que não foi testado e se as fontes
estavam atualizadas. Salve somente em destino privado autorizado;
sem essa autorização, entregue o relatório nesta conversa, redigido
sem segredos nem dados pessoais.
```

Informe uma área, funcionalidade ou PR para uma revisão menor. Um pedido de revisão de aplicação inteira pode ser dividido em partes rastreáveis; uma amostra não é uma auditoria completa. Links não carregam referências sozinhos: o agente deve ler os arquivos.

## Pedir correções e reteste

```text
Use a skill muchwst-fix para corrigir os achados [IDs] na cópia
local/branch autorizada. Confirme cada falha no fluxo real antes de editar.

Apresente a correção mínima na causa raiz e preserve os fluxos legítimos.
Crie/execute a regressão segura no ambiente de testes autorizado, quando
possível, mostrando antes/depois e variantes relevantes. Não faça
refatoração geral, deploy, rotação de segredos ou alteração de infraestrutura.

Atualize o relatório sem apagar as evidências originais. Diferencie
mitigado, corrigido aguardando reteste e reteste aprovado; informe o hash
e o ambiente realmente testados. Um bloqueio no WAF não fecha a falha
no código. Não declare que a correção chegou à produção sem prova.
```

“Revise e corrija” pode autorizar as edições locais delimitadas sem pedir confirmação por arquivo. Isso não autoriza operações remotas ou testes em terceiros. Alterações realmente sensíveis precisam de escopo e autorização próprios.

## VPS e Cloudflare

Use `muchwst-vps` para o host e `muchwst-cloudflare` para a borda. Peça primeiro a inspeção de configurações fornecidas ou leitura remota já autorizada. Identifique servidor/zona, ambiente, interfaces/protocolos, clientes e integrações legítimas e limites de acesso.

O plano deve preservar SSH/console de recuperação, registrar configuração anterior, validar sintaxe, testar acesso novo e trazer reversão. As skills verificam também IPv6, portas de containers, origem acessível diretamente, confiança em IPs encaminhados, cache de respostas privadas e recursos que dependem do plano do Cloudflare.

Bloqueio de scanner não é garantia de segurança. User-Agent pode ser falsificado; desafios de navegador podem quebrar APIs/webhooks. Exceções devem ser específicas e controles no servidor continuam necessários. Nenhum IP, comando, regra gerenciada ou recurso pago é presumido disponível.

## Instalação por agente

Cada pasta `skills/<nome>/` tem `SKILL.md`, referências, schema e modelos completos. Instale/copie a pasta inteira pelo mecanismo documentado da sua versão do Claude Code, Codex ou outro agente; confira o destino e o escopo antes de gravar. Não instale na pasta global de todos os projetos por conveniência e não substitua instruções existentes sem ler.

Não há um instalador que altere seu sistema. A descoberta automática dentro desses agentes não foi testada nesta entrega. O uso por leitura explícita funciona como instrução em Markdown sem depender de comandos ou APIs exclusivos, desde que o agente realmente consiga ler os arquivos; isso não garante que todo agente siga as instruções corretamente.

## Relatórios

Toda execução termina em relatório, mesmo sem achados. Para cada falha, o modelo pede localização/hash, classe, gravidade e justificativa, confiança, nível de evidência, impacto, condições, como foi explorada ou como testar, resultado esperado/observado, correção, mitigação e reteste. A frase “não reproduzido dinamicamente” é obrigatória quando só houve análise do código. CVSS é opcional e só entra com vetor/versão/valor conferidos; classificação qualitativa não exige inventar pontuação.

Arquivos de uma avaliação real são privados por padrão. Não os coloque neste repositório público. O JSON segue [`report.schema.json`](../shared/report.schema.json); o Markdown usa os modelos. Há um exemplo **sintético**, não uma avaliação real, em [`examples/synthetic-assessment`](../examples/synthetic-assessment/REPORT.md).

O script opcional gera Markdown e HTML localmente a partir do JSON, sem rede, scanners, scripts no HTML ou dependências Python externas:

```sh
python3 scripts/render_report.py caminho/privado/findings.json   --output caminho/privado/nova-pasta-do-relatorio
```

A pasta de saída precisa ser nova. O script valida estrutura e algumas consistências de status; não verifica sozinho a veracidade do achado, o cálculo CVSS nem se todos os segredos foram removidos. Revise o material antes de salvar/compartilhar.

## O que aconteceu com os 250 tópicos

A [matriz](topic-map.md) preserva os 250 itens, classifica sua aplicabilidade e aponta a skill responsável. Nem todo tópico é uma vulnerabilidade: índices, sharding, Raft, CQRS, SOC 2, SLOs e métricas não devem virar requisitos universais de uma aplicação web. Quando um tema operacional realmente afeta confidencialidade, integridade ou disponibilidade de forma demonstrável, ele pode originar um achado de segurança.

As [adições](additional-controls.md) cobrem os pontos de navegador/API reforçados depois da lista e lacunas importantes de superfície. O pacote usa um [catálogo institucional](../shared/sources.md) com OWASP, NIST, CISA, MITRE/CWE, FIRST/CVSS, CIS e outros. A busca web estava indisponível: conteúdo atual, CVEs, edições recentes, recursos/planos do Cloudflare e links externos **não foram verificados ao criar o pacote**. Cada revisão deve registrar o que conseguiu consultar de fato.

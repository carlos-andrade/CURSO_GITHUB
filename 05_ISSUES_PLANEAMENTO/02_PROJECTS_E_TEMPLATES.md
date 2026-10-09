# 05.2 — GitHub Projects e templates

> **Cabeçalho histórico**  
> Projeto: CURSO_GITHUB  
> Repositório: https://github.com/carlos-andrade/CURSO_GITHUB  
> Módulo: 05 — Issues e planeamento  
> Finalidade: organizar trabalho relacionado e padronizar a entrada de pedidos.  
> Estado: conteúdo desenvolvido; configuração prática pelo aluno pendente.  
> Última atualização: 2026-10-09.

## GitHub Projects

Projects permite organizar Issues e Pull Requests numa vista de trabalho, por exemplo tabela ou quadro. Campos, vistas e automações disponíveis podem variar conforme a configuração e a evolução do produto.

Comece por definir o objetivo do projeto e um conjunto pequeno de campos úteis, como estado, prioridade, responsável e data-alvo. Evite adicionar campos que ninguém atualiza ou que não ajudam numa decisão.

## Fluxo mínimo sugerido

1. Criar ou abrir um Project autorizado para o repositório/organização.
2. Definir estados com significado claro, por exemplo: `Todo`, `In progress`, `Review`, `Done`.
3. Adicionar Issues e PRs existentes.
4. Criar uma vista de tabela para triagem e uma vista de quadro se o fluxo visual for útil.
5. Definir quem mantém os estados atualizados.
6. Testar qualquer automação com um item não crítico antes de a aplicar em massa.

Não confunda o estado de um cartão com a conclusão técnica: “Done” deve seguir a definição de pronto do projeto, não apenas o fecho administrativo.

## Templates

Templates de Issues e Pull Requests ajudam a recolher contexto de forma consistente. Um bom template pede informação necessária sem tornar a submissão excessivamente longa.

Modelo simples para defeitos:
- O que aconteceu?
- O que esperava que acontecesse?
- Como reproduzir?
- Qual o ambiente relevante?
- Que evidência não sensível existe?

Modelo simples para PR:
- Objetivo e alteração.
- Testes executados e resultados.
- Riscos e limitações.
- Checklist de documentação, diff e segredos.

## Exercício verificável

Crie um Project de treino, adicione duas Issues e um PR (ou registe a limitação de permissões), crie duas vistas e confirme que os itens mantêm ligação ao trabalho original. Em seguida, redija um template curto de Issue.

## Critérios de aceitação

- [ ] O Project tem objetivo explícito.
- [ ] Os estados têm definições compreensíveis.
- [ ] Os itens apontam para Issues/PRs reais.
- [ ] O template recolhe contexto, resultado esperado e evidência.
- [ ] Não existe automação em massa sem teste prévio.

## Referência oficial

https://docs.github.com/en/issues/planning-and-tracking-with-projects/learning-about-projects/about-projects

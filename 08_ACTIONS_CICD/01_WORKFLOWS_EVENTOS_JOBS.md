# 08.1 — Workflows, eventos, jobs e steps

> **Cabeçalho histórico**  
> Projeto: CURSO_GITHUB  
> Repositório: https://github.com/carlos-andrade/CURSO_GITHUB  
> Módulo: 08 — GitHub Actions e CI/CD  
> Finalidade: compreender a estrutura de um workflow e escolher eventos de execução adequados.  
> Estado: conteúdo desenvolvido; workflow de treino a executar pelo aluno.  
> Última atualização: 2026-10-09.

## Objetivos

No final, deverá conseguir explicar o papel de um workflow, evento, job, step, runner e action, além de ler o resultado de uma execução.

## Modelo mental

- **Workflow:** ficheiro YAML em `.github/workflows/` que descreve uma automatização.
- **Evento:** acontecimento que inicia a execução, como `push`, `pull_request` ou `workflow_dispatch`.
- **Job:** conjunto de steps executado num runner.
- **Step:** comando ou action dentro de um job.
- **Runner:** ambiente de execução fornecido pelo GitHub ou autogerido.
- **Action:** componente reutilizável usado num step.

Os jobs podem executar em paralelo, salvo quando existem dependências explícitas. Use `needs` para declarar dependências entre jobs.

## Exemplo mínimo

Crie, num repositório de treino, `.github/workflows/validar-exemplo.yml`:

```yaml
name: Validar exemplo

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]
  workflow_dispatch:

permissions:
  contents: read

jobs:
  verificar:
    runs-on: ubuntu-latest
    steps:
      - name: Obter o código
        uses: actions/checkout@v5
      - name: Confirmar execução
        run: echo "Workflow executado"
```

A versão da action é um exemplo; confirme a versão estável recomendada no projeto e fixe dependências de acordo com a política de segurança. Em YAML, a indentação é significativa. O bloco `on` pode ser interpretado como booleano por alguns parsers YAML genéricos antigos; o GitHub Actions aplica a sua própria interpretação do formato de workflow.

## Como testar

1. Guarde o ficheiro na pasta exata `.github/workflows/`.
2. Faça commit e push para `main` no repositório de treino.
3. Abra o separador **Actions**.
4. Selecione o workflow e abra a execução mais recente.
5. Expanda cada job e step.
6. Registe o evento, o commit, o estado final e a saída do step.
7. Faça uma alteração documental e confirme se o evento esperado volta a iniciar o workflow.

## Ler uma falha

- **Workflow não aparece:** confirme caminho, extensão YAML e sintaxe.
- **Não iniciou:** confirme evento, branch, filtros e permissões.
- **Job falhou:** abra o primeiro step com falha e leia a mensagem concreta.
- **Action falhou:** confirme entradas, permissões e versão.
- **Tempo excedido:** investigue comandos bloqueados ou dependências externas.

Não repita execuções sem alterar ou compreender a causa. Registe a primeira falha, a hipótese, a correção e o resultado posterior.

## Exercício verificável

Crie um workflow com os eventos `push` e `workflow_dispatch`, execute-o e guarde a ligação da execução bem-sucedida. Depois provoque uma falha controlada num repositório de treino, identifique o step e reverta a alteração de teste.

## Critérios de aceitação

- [ ] O ficheiro está em `.github/workflows/`.
- [ ] A sintaxe é aceite pelo GitHub.
- [ ] O aluno identifica evento, job e step.
- [ ] A execução é ligada a um commit concreto.
- [ ] Uma falha é diagnosticada a partir dos logs.
- [ ] As permissões estão limitadas ao necessário.

## Referência oficial

https://docs.github.com/en/actions/writing-workflows

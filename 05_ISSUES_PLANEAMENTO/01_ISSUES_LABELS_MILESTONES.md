# 05.1 — Issues, labels e milestones

> **Cabeçalho histórico**  
> Projeto: CURSO_GITHUB  
> Repositório: https://github.com/carlos-andrade/CURSO_GITHUB  
> Módulo: 05 — Issues e planeamento  
> Finalidade: transformar pedidos, defeitos e ideias em trabalho rastreável.  
> Estado: conteúdo desenvolvido; exercício real pelo aluno pendente.  
> Última atualização: 2026-10-09.

## Quando criar uma Issue

Use uma Issue para registar um defeito, uma tarefa, uma pergunta de trabalho ou uma proposta que precise de discussão e acompanhamento. Antes de abrir uma nova, procure duplicados e verifique se o projeto já tem um processo definido.

## Estrutura de uma Issue útil

- **Título:** específico e pesquisável.
- **Contexto:** onde e em que condições ocorre o problema ou necessidade.
- **Resultado esperado:** o que deve ser verdade quando o trabalho terminar.
- **Passos para reproduzir:** quando se trata de um defeito.
- **Resultado atual:** comportamento observado, com evidência segura.
- **Critérios de aceitação:** condições verificáveis para fechar a Issue.
- **Âmbito e limitações:** o que não está incluído.

Evite títulos vagos como “Urgente”, “Corrigir” ou “Melhorar tudo”. Não publique tokens, palavras-passe, dados pessoais ou detalhes privados.

## Labels

As labels ajudam a filtrar e classificar. Um esquema simples pode incluir:

- `bug`: comportamento incorreto.
- `documentation`: documentação.
- `enhancement`: melhoria funcional.
- `question`: questão a esclarecer.
- `good first issue`: tarefa adequada a quem está a começar, quando isso for verdadeiro.

Os nomes e cores não são universais; alinhe-os com as convenções do repositório. Evite criar muitas labels redundantes.

## Milestones

Uma milestone agrupa Issues e Pull Requests associados a um objetivo ou entrega. Defina um nome, um resultado esperado e, quando útil, uma data realista. Uma milestone não substitui a descrição nem os critérios de aceitação de cada Issue.

## Exercício

Crie uma Issue no repositório de treino para melhorar uma lição do curso. Inclua contexto, resultado esperado, três critérios de aceitação e uma label apropriada. Se não tiver permissão para criar Issues, use o modelo abaixo num ficheiro local e registe a limitação.

## Modelo

```markdown
## Contexto
[O que motivou a tarefa?]

## Resultado esperado
[O que deve ficar diferente?]

## Critérios de aceitação
- [ ] ...
- [ ] ...
- [ ] ...

## Evidência / passos de reprodução
[Informação segura e verificável]

## Fora do âmbito
[O que esta tarefa não pretende resolver]
```

## Critérios de aceitação

A Issue permite que outra pessoa compreenda o trabalho sem depender de mensagens privadas; os critérios podem ser verificados; e a classificação corresponde ao conteúdo.

## Referência oficial

https://docs.github.com/en/issues/tracking-your-work-with-issues/about-issues

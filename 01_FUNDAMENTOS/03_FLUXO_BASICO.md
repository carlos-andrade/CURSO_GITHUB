# 01-03 — Fluxo básico de trabalho

> **Cabeçalho histórico**  
> Projeto: CURSO_GITHUB  
> Repositório oficial: https://github.com/carlos-andrade/CURSO_GITHUB  
> Módulo: 01 — Fundamentos  
> Lição: 01-03  
> Finalidade: aplicar um ciclo completo de alteração e verificação.  
> Estado: publicado; execução pelo aluno pendente.

## Resultado esperado

Executar uma alteração pequena, guardar a versão no repositório e confirmar que o conteúdo publicado corresponde ao pretendido.

## Fluxo conceptual

1. Criar ou abrir um repositório.
2. Confirmar a branch e o ficheiro que será alterado.
3. Alterar apenas o necessário.
4. Rever o conteúdo e o diff.
5. Registar a alteração num commit.
6. Enviar as alterações para o remoto (push), quando estiver a trabalhar localmente.
7. Abrir o GitHub e confirmar o resultado publicado.
8. Guardar a evidência e registar o estado.

Na interface web, a edição e o commit podem ocorrer no mesmo ecrã. No Git local, as etapas são normalmente explícitas: editar, rever, preparar, commit e push.

## Prática guiada pela interface web

1. Abrir o repositório de treino.
2. Criar `NOTAS.md` com três linhas de conteúdo fictício.
3. Usar a opção de commit para guardar o ficheiro.
4. Abrir o commit e confirmar a mensagem e o ficheiro alterado.
5. Abrir o ficheiro na branch esperada e comparar o conteúdo.
6. Registar as URLs do ficheiro e do commit.

**Resultado esperado:** o ficheiro existe na branch selecionada e o histórico mostra a alteração.

## Exercício autónomo

Editar uma linha de `NOTAS.md` para corrigir ou clarificar o texto. Criar outro commit, comparar os dois commits e registar uma diferença observável.

## Critérios de aceitação

- [ ] O ficheiro existe no repositório e na branch esperada.
- [ ] O commit tem mensagem descritiva.
- [ ] O conteúdo publicado corresponde ao pretendido.
- [ ] O diff mostra apenas as alterações esperadas.
- [ ] As URLs de evidência estão registadas.
- [ ] Não foram publicados segredos nem dados privados.

## Diagnóstico rápido

Se o ficheiro não aparecer, confirmar a branch, o repositório e se o commit foi realmente criado. Se o conteúdo estiver incorreto, editar de novo e criar um commit corretivo; não ocultar o erro nem apagar histórico sem compreender o impacto.

## Fontes oficiais

- GitHub Docs — Quickstart: https://docs.github.com/en/get-started/quickstart
- GitHub Docs — Committing changes: https://docs.github.com/en/pull-requests/committing-changes-to-your-project/creating-and-editing-commits/about-commits

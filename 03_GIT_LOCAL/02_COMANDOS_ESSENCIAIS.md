# 03-02 — Comandos essenciais do Git

> **Cabeçalho histórico**  
> Projeto: CURSO_GITHUB  
> Repositório oficial: https://github.com/carlos-andrade/CURSO_GITHUB  
> Módulo: 03 — Git local e linha de comandos  
> Lição: 03-02  
> Finalidade: inspecionar, preparar, registar e verificar alterações localmente.  
> Estado: publicado; execução local pendente.

## Antes de começar

Executar os comandos dentro de um repositório de treino. Confirmar a pasta atual e nunca usar comandos de alteração de histórico em trabalho importante sem compreender o impacto.

## Ciclo de trabalho mínimo

```bash
git status
git diff
# editar um ficheiro, por exemplo README.md
git status
git diff
git add README.md
git diff --staged
git commit -m "docs: atualiza README"
git status
git log --oneline -5
```

A linha de edição é uma instrução para o aluno, não um comando literal. Antes do `git add`, substituir `README.md` pelo caminho do ficheiro que pretende preparar.

## O que faz cada comando

- `git status`: mostra branch e estado dos ficheiros.
- `git diff`: mostra alterações ainda não preparadas.
- `git add`: prepara alterações para o próximo commit.
- `git diff --staged`: mostra o conteúdo que será incluído no commit.
- `git commit`: cria um registo no histórico a partir do que está preparado.
- `git log --oneline -5`: apresenta os cinco commits mais recentes de forma compacta.

## Exercício guiado

1. Criar um ficheiro `NOTAS.md` com duas linhas fictícias.
2. Executar `git status` e observar o ficheiro não acompanhado.
3. Preparar apenas `NOTAS.md` com `git add NOTAS.md`.
4. Executar `git diff --staged` e confirmar o conteúdo.
5. Criar um commit com uma mensagem descritiva.
6. Executar `git status` e `git log --oneline -5`.

## Critérios de aceitação

- [ ] Sei distinguir alterações não preparadas de alterações preparadas.
- [ ] Revisei o diff antes do commit.
- [ ] O commit contém apenas a alteração pretendida.
- [ ] O histórico mostra o novo commit.
- [ ] A árvore de trabalho fica limpa, ou sei explicar o que permanece pendente.

## Erros frequentes

- **Fazer `git add .` sem rever o estado:** pode preparar ficheiros inesperados. No início, adicionar explicitamente o ficheiro pretendido.
- **Commit vazio ou sem a alteração esperada:** verificar `git status` e `git diff --staged` antes de repetir.
- **Mensagem vaga:** descrever a alteração e não apenas o facto de ter trabalhado.

## Fonte oficial

- Git Reference: https://git-scm.com/docs
- Git Book — Recording Changes to the Repository: https://git-scm.com/book/en/v2/Git-Basics-Recording-Changes-to-the-Repository

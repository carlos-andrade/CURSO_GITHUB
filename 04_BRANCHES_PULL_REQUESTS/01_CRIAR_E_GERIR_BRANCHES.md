# 04.1 — Criar e gerir branches

> **Cabeçalho histórico**  
> Projeto: CURSO_GITHUB  
> Repositório: https://github.com/carlos-andrade/CURSO_GITHUB  
> Módulo: 04 — Branches e Pull Requests  
> Finalidade: praticar alterações isoladas sem trabalhar diretamente na branch principal.  
> Estado: conteúdo desenvolvido; execução prática pelo aluno pendente.  
> Última atualização: 2026-10-09.

## Objetivos

No final, deverá conseguir explicar por que razão se usa uma branch, criar uma branch a partir da base correta, verificar a branch ativa e publicar a branch no GitHub.

## Conceitos

- **Branch:** linha de desenvolvimento com um nome, apontando para um commit.
- **Base:** branch ou commit a partir do qual o trabalho começa.
- **HEAD:** referência para o commit/branch atualmente selecionado.
- **Branch principal:** normalmente `main`; deve receber alterações integradas e verificadas, não trabalho experimental direto.

Uma branch não é uma cópia independente completa do repositório. É uma referência móvel para uma sequência de commits.

## Pela interface do GitHub

1. Abra o repositório de treino e confirme o nome e a branch atual.
2. Abra o seletor de branches.
3. Introduza um nome descritivo, por exemplo `docs/primeira-alteracao`.
4. Crie a branch a partir de `main`, depois de confirmar que essa é a base pretendida.
5. Faça uma alteração pequena num ficheiro de treino e confirme que a interface indica a branch de trabalho.
6. Registe o nome da branch e o commit de base no relatório do exercício.

## Pela linha de comandos

Execute dentro da pasta do repositório:

```bash
git status
git switch main
git pull --ff-only
git switch -c docs/primeira-alteracao
git branch --show-current
git status
```

Se a branch local `main` não existir ou o repositório não estiver sincronizado, pare e resolva essa condição antes de continuar. Não execute comandos destrutivos para contornar um estado desconhecido.

Para publicar a branch:

```bash
git push -u origin docs/primeira-alteracao
```

## Exercício verificável

- [ ] Confirmar o repositório e a branch base.
- [ ] Criar `docs/primeira-alteracao`.
- [ ] Confirmar a branch ativa com `git branch --show-current`.
- [ ] Fazer uma alteração pequena e intencional.
- [ ] Confirmar o diff com `git diff`.
- [ ] Publicar a branch, se houver acesso remoto configurado.

## Critérios de aceitação

O exercício está concluído quando o aluno consegue identificar a branch ativa, explicar a sua base, mostrar a alteração isolada e demonstrar que `main` não foi alterada diretamente.

## Recuperação segura

Se criou a branch errada, não apague alterações sem as inspecionar. Execute `git status`, preserve qualquer trabalho útil e só depois decida se deve mudar de branch ou criar outra.

## Evidência a guardar

Nome da branch, base usada, saída de `git branch --show-current`, resumo de `git status` e captura de ecrã ou ligação para a branch publicada.

## Referência oficial

https://docs.github.com/en/get-started/using-git/about-git-branches

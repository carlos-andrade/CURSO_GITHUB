# 04.4 — Resolver conflitos de merge

> **Cabeçalho histórico**  
> Projeto: CURSO_GITHUB  
> Repositório: https://github.com/carlos-andrade/CURSO_GITHUB  
> Módulo: 04 — Branches e Pull Requests  
> Finalidade: compreender conflitos e resolvê-los sem descartar trabalho inadvertidamente.  
> Estado: conteúdo desenvolvido; execução prática pelo aluno pendente.  
> Última atualização: 2026-10-09.

## O que é um conflito?

Um conflito ocorre quando Git não consegue combinar automaticamente alterações concorrentes. É necessário decidir qual conteúdo final representa corretamente a intenção do projeto. Nem todo conflito resulta de alterações na mesma linha, e nem toda combinação automática está semanticamente correta.

## Preparação

- Trabalhe num repositório de treino.
- Confirme `git status` e guarde qualquer alteração útil.
- Identifique a branch atual e a branch que será integrada.
- Não comece a resolução com um diretório de trabalho que já contenha alterações não compreendidas.

## Passos de resolução

1. Atualize a referência remota: `git fetch origin`.
2. Confirme a branch de trabalho: `git branch --show-current`.
3. Integre a base pretendida, usando a estratégia definida pelo projeto. Exemplo, se a equipa usa merge:
   `git merge origin/main`
4. Se houver conflito, execute `git status) e identifique os ficheiros marcados.
5. Abra cada ficheiro e localize os marcadores `<<<<<<<`, `=======` e `>>>>>>>`.
6. Compare as duas versões e produza o conteúdo final correto. Não elimine marcadores sem decidir o conteúdo.
7. Remova todos os marcadores, guarde o ficheiro e reveja-o integralmente.
8. Execute as verificações adequadas e confirme o diff.
9. Marque o ficheiro como resolvido com `git add caminho/do/ficheiro`.
10. Termine o merge com `git commit` apenas quando o estado e a mensagem do Git indicarem que é necessário.
11. Confirme `git status) e publique a branch se for apropriado.

Se a estratégia usada for rebase, os comandos e a forma de continuar são diferentes. Não misture procedimentos de merge e rebase; siga a política do projeto.

## Abortar com segurança

Se não compreende a resolução e ainda não concluiu a operação, consulte o estado e a ajuda do comando em uso. `git merge --abort` pode cancelar um merge em curso, mas não é uma garantia de recuperar alterações preexistentes em todos os estados. Nunca execute reset destrutivo como tentativa automática de resolver conflitos.

## Exercício verificável

Num repositório de treino, crie duas branches que alterem a mesma linha de um ficheiro de texto. Integre uma branch na outra, resolva o conflito, mostre o diff final e confirme que o conteúdo reflete ambas as intenções quando apropriado.

## Critérios de aceitação

- [ ] Identifica os ficheiros em conflito.
- [ ] Explica as duas versões concorrentes.
- [ ] Remove os marcadores sem perder conteúdo necessário.
- [ ] Executa a validação relevante.
- [ ] Confirma o estado final do repositório.

## Referência oficial

https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/addressing-merge-conflicts

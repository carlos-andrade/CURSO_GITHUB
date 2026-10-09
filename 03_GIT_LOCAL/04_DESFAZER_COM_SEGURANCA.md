# Desfazer alterações com segurança

> Projeto: CURSO_GITHUB | Módulo 03 | Lição 04

Antes de qualquer reversão:
1. Executar `git status`.
2. Inspecionar `git diff` e `git diff --staged`.
3. Identificar se a alteração já foi publicada.
4. Criar uma cópia ou branch de recuperação quando apropriado.

Distinguir alterações locais não commitadas, commits locais e commits já partilhados. Comandos como `reset --hard` podem eliminar alterações locais; não os usar sem compreender o impacto.

Preferir práticas explícitas e documentadas; para desfazer um commit partilhado, avaliar `git revert`.

Referência: https://git-scm.com/docs/git-revert
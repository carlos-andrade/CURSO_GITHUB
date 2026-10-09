# 03-04 — Desfazer alterações com segurança

> **Cabeçalho histórico**  
> Projeto: CURSO_GITHUB  
> Repositório oficial: https://github.com/carlos-andrade/CURSO_GITHUB  
> Módulo: 03 — Git local e linha de comandos  
> Lição: 03-04  
> Finalidade: escolher uma recuperação compatível com o estado da alteração.  
> Estado: publicado; os comandos devem ser praticados apenas em repositório de treino.

## Regra principal

Antes de qualquer reversão, executar `git status` e inspecionar `git diff` e `git diff --staged`. Identificar se a alteração está no diretório de trabalho, na área de staging, num commit local ou num commit já partilhado.

## Caso A — Retirar um ficheiro do staging sem apagar as alterações

```bash
git restore --staged README.md
git status
```

O ficheiro deixa de estar preparado para o próximo commit, mas as alterações locais são mantidas.

## Caso B — Descartar alterações locais não commitadas

```bash
git diff -- README.md
git restore README.md
git status
```

**Atenção:** `git restore README.md` descarta as alterações não commitadas desse ficheiro. Só executar se tiver confirmado que não precisa delas. Criar uma cópia antes se existir qualquer dúvida.

## Caso C — Desfazer um commit já partilhado

Em trabalho colaborativo, avaliar `git revert` para criar um novo commit que inverte o efeito de um commit anterior:

```bash
git log --oneline -5
git revert ID_DO_COMMIT
```

Substituir `ID_DO_COMMIT` pelo identificador correto. Ler a mensagem apresentada, resolver eventuais conflitos e rever o resultado antes de o publicar.

## Operações que exigem cautela especial

- `git reset --hard` pode descartar alterações locais e mover a referência atual.
- `git clean` pode remover ficheiros não acompanhados.
- `git push --force` pode substituir histórico remoto e afetar outras pessoas.

Não usar estes comandos como tentativa genérica de corrigir um erro. Confirmar alvo, estado, impacto e existência de cópia recuperável; se não compreender o efeito, parar e pedir revisão.

## Exercício autónomo

Num repositório descartável, criar uma alteração não commitada, inspecionar o diff e praticar apenas a retirada do staging. Não praticar descarte irreversível num projeto real.

## Critérios de aceitação

- [ ] Identifico em que estado está a alteração.
- [ ] Distingo retirar do staging de descartar alterações.
- [ ] Sei quando `git revert` é preferível para um commit partilhado.
- [ ] Não executo operações destrutivas sem compreender o efeito.
- [ ] Registo o resultado observado.

## Fontes oficiais

- Git Reference — restore: https://git-scm.com/docs/git-restore
- Git Reference — revert: https://git-scm.com/docs/git-revert
- Git Reference — reset: https://git-scm.com/docs/git-reset

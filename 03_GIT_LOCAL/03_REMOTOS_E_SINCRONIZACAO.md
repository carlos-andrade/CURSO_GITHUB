# 03-03 — Remotos e sincronização

> **Cabeçalho histórico**  
> Projeto: CURSO_GITHUB  
> Repositório oficial: https://github.com/carlos-andrade/CURSO_GITHUB  
> Módulo: 03 — Git local e linha de comandos  
> Lição: 03-03  
> Finalidade: compreender como sincronizar commits entre o repositório local e o remoto.  
> Estado: publicado; teste local pendente.

## Conceitos

Um remoto é uma referência para outro repositório, normalmente alojado no GitHub. O nome convencional é `origin`, mas pode ser diferente.

- `git remote -v`: mostra os endereços dos remotos configurados.
- `git fetch origin`: obtém referências e objetos do remoto sem integrar automaticamente as alterações na branch atual.
- `git pull`: obtém e integra alterações na branch atual, conforme a configuração de Git.
- `git push`: publica commits locais no remoto.
- `git branch --show-current`: mostra a branch atual.
- `git status`: ajuda a confirmar se há alterações locais ou divergência.

## Clonar um repositório

Para obter uma cópia local de um repositório existente:

```bash
git clone https://github.com/UTILIZADOR/REPOSITORIO.git
cd REPOSITORIO
git remote -v
git status
```

Substituir os nomes de exemplo pelos dados do repositório de treino. Não copiar comandos com URLs de projetos privados para locais públicos.

## Fluxo de sincronização seguro

1. Executar `git status` e confirmar a branch.
2. Executar `git fetch origin`.
3. Rever o estado e perceber se existem commits remotos novos.
4. Se for necessário integrar alterações, confirmar que o trabalho local está guardado e compreender a estratégia de integração antes de executar `git pull`.
5. Depois de criar e rever um commit local, usar `git push` para o publicar, se tiver permissões.
6. Abrir o GitHub e confirmar que o commit aparece na branch esperada.

Não usar `git push --force` como solução genérica para uma rejeição. Primeiro identificar a causa e consultar a documentação.

## Exercício autónomo

Clonar um repositório público de treino ou o próprio repositório de treino, alterar um ficheiro localmente, criar um commit e publicar a alteração numa branch de trabalho, se as permissões e a configuração permitirem. Se não tiver permissão de escrita, registar essa limitação e não tentar contorná-la.

## Critérios de aceitação

- [ ] Identifico o remoto e o respetivo URL.
- [ ] Distingo `fetch`, `pull` e `push`.
- [ ] Confirmo branch e estado antes de sincronizar.
- [ ] Sei confirmar no GitHub se o commit foi publicado.
- [ ] Não uso force push para resolver erros sem diagnóstico.

## Fontes oficiais

- Git Reference: https://git-scm.com/docs
- Git Book — Working with Remotes: https://git-scm.com/book/en/v2/Git-Basics-Working-with-Remotes

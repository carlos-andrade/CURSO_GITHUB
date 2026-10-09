# 08.2 — Diagnóstico, permissões e segurança de workflows

> **Cabeçalho histórico**  
> Projeto: CURSO_GITHUB  
> Repositório: https://github.com/carlos-andrade/CURSO_GITHUB  
> Módulo: 08 — GitHub Actions e CI/CD  
> Finalidade: diagnosticar falhas e reduzir privilégios e riscos na automatização.  
> Estado: conteúdo desenvolvido; auditoria prática de workflow pelo aluno pendente.  
> Última atualização: 2026-10-09.

## Diagnóstico sistemático

1. Registe o link da execução, commit, evento e branch.
2. Identifique o primeiro step que falhou; erros posteriores podem ser consequência.
3. Leia a mensagem completa e procure o comando que a originou.
4. Compare o contexto esperado com o real: diretório, versões, variáveis, permissões e artefactos.
5. Formule uma hipótese verificável e altere uma coisa de cada vez.
6. Volte a executar e compare os resultados.
7. Registe a causa confirmada; se não estiver confirmada, mantenha-a como hipótese.

## Permissões mínimas

Declare permissões explícitas no workflow ou job, de acordo com as operações necessárias. Por exemplo:

```yaml
permissions:
  contents: read
```

Um workflow que só lê o repositório normalmente não precisa de permissões de escrita. Se precisar de criar releases, publicar pacotes ou comentar PRs, conceda apenas o âmbito necessário e, quando possível, no job específico. Confirme as políticas da organização e do repositório.

## Segredos e dados sensíveis

- Guarde credenciais em GitHub Actions Secrets ou num gestor de segredos aprovado.
- Nunca escreva um token diretamente no YAML, script, log ou artefacto.
- Não imprima variáveis secretas para “confirmar” que existem.
- Não execute código de terceiros com permissões elevadas sem revisão.
- Tenha especial cuidado com workflows que usam contexto de conteúdo controlado por utilizadores externos, como títulos, comentários ou código de Pull Requests.
- Não confie apenas na ocultação automática dos logs para proteger segredos.

## Dependências e ações externas

Use versões de actions conhecidas e mantidas. Para ambientes de maior risco, avalie a fixação por SHA completo, a proveniência, as permissões e a política de atualização. Evite descarregar e executar scripts remotos sem inspeção. Atualize dependências de forma controlada e teste as mudanças.

## Artefactos e cache

Não inclua credenciais, ficheiros privados ou dados desnecessários nos artefactos. Considere retenção, acessos e conteúdo armazenado. Não use cache como fonte de verdade nem confie em conteúdo de cache que possa ser manipulado por um fluxo não confiável.

## Exercício verificável

Audite um workflow de treino e registe: evento, permissões, actions externas, segredos usados, artefactos, contexto não confiável e riscos. Reduza permissões excessivas e execute novamente. Nunca altere um workflow de produção para provocar falhas ou testar segredos.

## Critérios de aceitação

- [ ] A causa da falha é sustentada por logs.
- [ ] As permissões são mínimas e explícitas quando apropriado.
- [ ] Não existem credenciais no código ou nos logs.
- [ ] Actions e scripts externos foram avaliados.
- [ ] Artefactos e cache não expõem dados sensíveis.
- [ ] A correção tem evidência de execução.

## Referência oficial

https://docs.github.com/en/actions/security-for-github-actions/security-guides/security-hardening-for-github-actions

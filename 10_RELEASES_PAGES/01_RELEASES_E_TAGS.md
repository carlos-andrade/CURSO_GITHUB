# 10.1 — Releases, tags e notas de versão

> **Cabeçalho histórico**  
> Projeto: CURSO_GITHUB  
> Repositório: https://github.com/carlos-andrade/CURSO_GITHUB  
> Módulo: 10 — Releases e GitHub Pages  
> Finalidade: identificar uma versão de forma rastreável e comunicar uma entrega.  
> Estado: conteúdo desenvolvido; release de treino pendente.  
> Última atualização: 2026-10-09.

## Conceitos essenciais

- **Commit:** regista uma alteração no histórico Git.
- **Tag:** nome associado a um ponto do histórico, normalmente usado para identificar uma versão.
- **Release:** entrega publicada no GitHub que se associa a uma tag e pode incluir notas e artefactos.
- **Notas de versão:** resumo orientado para quem vai usar, instalar ou atualizar o projeto.

Uma release não prova por si só que o software foi testado. As notas devem distinguir alterações concluídas, correções, problemas conhecidos e compatibilidade.

## Convenção de versão

O projeto pode usar SemVer (`MAJOR.MINOR.PATCH`) quando esse esquema fizer sentido:
- MAJOR: alteração incompatível com versões anteriores.
- MINOR: funcionalidade compatível acrescentada.
- PATCH: correção compatível.

Não aplique esta convenção automaticamente a todo o tipo de projeto. Documente o esquema escolhido e evite reutilizar uma tag publicada para uma versão diferente.

## Preparação de uma release

1. Confirme que a branch de destino contém as alterações previstas.
2. Reveja os checks, testes e limitações conhecidos.
3. Escolha a versão e confirme se já existe uma tag com esse nome.
4. Prepare notas que expliquem o que mudou e o que não foi validado.
5. Crie a release no repositório de treino, apontando para o commit correto.
6. Verifique a página da release, a tag e os artefactos anexados.
7. Registe a ligação e a evidência no relatório do exercício.

## Exemplo de notas de versão

```markdown
# v0.1.0 — Versão de treino

## Adicionado
- Estrutura inicial da aplicação de demonstração.

## Corrigido
- Nenhuma correção nesta versão.

## Validação
- Workflow de documentação: sucesso (ligação para execução).
- Testes funcionais: não executados.

## Limitações
- Versão experimental, apenas para aprendizagem.
```

O exemplo é ilustrativo. Substitua-o por resultados observados e nunca declare testes que não executou.

## Recuperação e rastreabilidade

Se uma release apontar para o commit errado, não oculte o problema alterando silenciosamente o histórico. Siga a política do repositório para corrigir, retirar ou publicar uma nova versão, mantendo o registo claro. Para uma release já distribuída, considere o impacto nos utilizadores.

## Exercício verificável

Num repositório de treino, crie uma versão `v0.1.0` com notas de versão. Confirme a tag e o commit associado, abra a release e guarde a ligação. Inclua pelo menos uma limitação real no relatório.

## Critérios de aceitação

- [ ] A tag é única e aponta para o commit esperado.
- [ ] As notas distinguem funcionalidades, correções e limitações.
- [ ] Os resultados de teste são verdadeiros e verificáveis.
- [ ] A release e os artefactos estão acessíveis ao público pretendido.
- [ ] A ligação da release foi registada.

## Referência oficial

https://docs.github.com/en/repositories/releasing-projects-on-github

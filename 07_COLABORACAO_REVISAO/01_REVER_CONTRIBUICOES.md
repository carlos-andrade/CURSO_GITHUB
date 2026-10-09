# 07.1 — Rever contribuições com qualidade

> **Cabeçalho histórico**  
> Projeto: CURSO_GITHUB  
> Repositório: https://github.com/carlos-andrade/CURSO_GITHUB  
> Módulo: 07 — Colaboração e revisão  
> Finalidade: melhorar alterações por meio de revisão técnica respeitosa, específica e verificável.  
> Estado: conteúdo desenvolvido; simulação prática pelo aluno pendente.  
> Última atualização: 2026-10-09.

## Princípios de revisão

A revisão avalia a alteração e os seus efeitos, não a pessoa que a propôs. Os comentários devem ser claros, proporcionais ao risco e apoiados em exemplos ou critérios do projeto.

## O que verificar

1. **Objetivo:** a alteração resolve a necessidade declarada?
2. **Correção:** há erros, omissões ou efeitos laterais?
3. **Âmbito:** foram alterados ficheiros não relacionados?
4. **Legibilidade:** nomes, estrutura e explicações são compreensíveis?
5. **Testes:** existem verificações adequadas e os resultados são reais?
6. **Documentação:** foi atualizada quando o comportamento mudou?
7. **Segurança:** há segredos, dados pessoais ou permissões excessivas?
8. **Compatibilidade:** a mudança quebra ligações, fluxos ou utilizadores existentes?

## Como escrever um comentário útil

Um comentário de revisão deve indicar:
- **Local:** ficheiro e linha ou trecho.
- **Problema:** o que está incorreto ou pouco claro.
- **Impacto:** por que importa.
- **Ação sugerida:** como investigar ou corrigir.

Exemplo de formulação:
> Esta instrução não indica a pasta onde o comando deve ser executado. Um principiante pode executá-lo no repositório errado. Pode acrescentar o pré-requisito e o resultado esperado?

Evite “isto está mal” sem explicação, comentários pessoais ou exigências de estilo que não correspondam a uma regra documentada.

## Severidade e prioridade

- **Bloqueador:** risco de perda de dados, segurança, falha central ou critério obrigatório incumprido.
- **Importante:** defeito relevante que deve ser resolvido antes da integração.
- **Sugestão:** melhoria não bloqueadora.
- **Questão:** informação necessária para compreender a intenção.

Use as convenções do projeto; esta classificação é um guia, não uma taxonomia imposta pelo GitHub.

## Responder a uma revisão

Leia o comentário completo, confirme o contexto, faça a correção numa alteração rastreável e responda com o que mudou e como foi verificado. Se discordar, explique a razão com evidência e procure alinhamento. Não resolva um comentário apenas para limpar a interface se a questão continua aberta.

## Exercício verificável

Use um PR de treino com uma alteração documental. Faça uma revisão que identifique um ponto concreto; aplique uma correção e registe o diff antes/depois. Se não houver defeito real, faça uma pergunta útil em vez de inventar uma falha.

## Critérios de aceitação

- [ ] Comentário específico e respeitoso.
- [ ] Impacto explicado.
- [ ] Ação ou pergunta concreta.
- [ ] Correção verificada no diff atualizado.
- [ ] Estado do comentário corresponde ao problema real.

## Contribuir para projetos externos

Antes de contribuir, leia o README, licença, regras de contribuição e código de conduta, se existirem. Não assuma que pode reutilizar conteúdo protegido ou que tem permissão para publicar dados internos. Faça fork ou branch conforme o fluxo do projeto, mantenha o PR limitado e nunca inclua credenciais.

## Referência oficial

https://docs.github.com/en/pull-requests/collaborating-with-pull-requests

# 04.3 — Rever e integrar um Pull Request

> **Cabeçalho histórico**  
> Projeto: CURSO_GITHUB  
> Repositório: https://github.com/carlos-andrade/CURSO_GITHUB  
> Módulo: 04 — Branches e Pull Requests  
> Finalidade: avaliar alterações e integrar apenas quando os critérios estiverem cumpridos.  
> Estado: conteúdo desenvolvido; execução prática pelo aluno pendente.  
> Última atualização: 2026-10-09.

## Objetivos

Ler um diff, avaliar o efeito da alteração, responder a comentários e reconhecer os estados que podem impedir a integração.

## Roteiro de revisão

1. Leia o objetivo do PR e compare-o com a alteração real.
2. Abra **Files changed** e examine o contexto, não apenas as linhas destacadas.
3. Procure erros lógicos, documentação incoerente, alterações fora do âmbito, ligações quebradas e exposição acidental de dados.
4. Consulte os resultados das verificações automáticas; abra os detalhes quando uma verificação falhar.
5. Faça comentários específicos, com localização e motivo. Quando possível, indique uma correção concreta.
6. Registe os pontos que bloqueiam a integração e os que são apenas sugestões.
7. Depois das correções, reveja o novo diff. Não assuma que uma resposta ao comentário resolve o problema.

## Estados comuns

- **Comment:** comentário sem aprovação formal.
- **Approve:** aprovação da revisão, se as regras do repositório a permitirem.
- **Request changes:** solicita correções antes de avançar.
- **Checks:** resultados de workflows ou verificações configuradas.
- **Merge conflict:** as alterações não podem ser integradas automaticamente sem resolução.

A disponibilidade dos botões e os requisitos dependem das permissões e das regras do repositório.

## Antes do merge

- [ ] Base e origem confirmadas.
- [ ] Diff final revisto.
- [ ] Comentários resolvidos ou explicitamente justificados.
- [ ] Verificações obrigatórias aprovadas.
- [ ] Aprovações exigidas obtidas.
- [ ] Sem segredos ou alterações não relacionadas.
- [ ] Estratégia de merge compatível com as regras do projeto.

Não contorne verificações obrigatórias nem reduza proteções apenas para fazer o PR passar. Se não tiver permissão para integrar, peça ao responsável autorizado.

## Exercício verificável

Use o PR de treino da lição anterior. Faça uma revisão, registe pelo menos um comentário fundamentado (se houver algo real a melhorar), aplique a correção e compare o diff antes/depois. Só faça merge num repositório de treino e depois de todas as condições estarem cumpridas.

## Critérios de aceitação

O aluno explica a diferença entre comentário e aprovação, identifica uma verificação falhada e demonstra que o diff final corresponde ao objetivo declarado.

## Evidência a guardar

Ligação do PR, resumo da revisão, resultado dos checks e estado final. Se não fez merge, registe a razão.

## Referência oficial

https://docs.github.com/en/pull-requests/collaborating-with-pull-requests

# 11.2 — Automação e manutenção sustentável

> **Cabeçalho histórico**  
> Projeto: CURSO_GITHUB  
> Repositório: https://github.com/carlos-andrade/CURSO_GITHUB  
> Módulo: 11 — API e tópicos avançados  
> Finalidade: desenhar tarefas automatizadas previsíveis, testáveis e fáceis de manter.  
> Estado: conteúdo desenvolvido; exercício de implementação pendente.  
> Última atualização: 2026-10-09.

## Princípios

- Defina o resultado esperado antes de escrever código.
- Valide entradas e limite o âmbito da operação.
- Prefira operações idempotentes, para que a repetição não duplique efeitos.
- Use as permissões mínimas necessárias.
- Registe resultados e erros acionáveis sem incluir dados confidenciais.
- Defina códigos de saída e critérios claros de falha.
- Documente dependências, configuração e procedimento de recuperação.
- Teste em dados fictícios ou num repositório de treino antes de usar um repositório importante.

## Ciclo de desenvolvimento

1. Descreva a tarefa manual e o problema que pretende resolver.
2. Defina entradas, saídas, pré-condições e critérios de aceitação.
3. Identifique cenários de sucesso, falha e entrada inválida.
4. Prepare um modo de validação ou simulação antes de alterações com impacto.
5. Implemente a menor solução útil.
6. Execute os testes e registe resultados observados.
7. Reveja permissões, dependências e mensagens de erro.
8. Documente manutenção e recuperação.

## API, paginação e repetição

Não presuma que uma única resposta contém todos os resultados. Respeite paginação e limites de utilização. Em falhas transitórias, limite as tentativas e use intervalos controlados. Antes de repetir uma operação que altera dados, confirme se a primeira tentativa produziu efeitos.

## Exercício verificável

Especifique uma tarefa que verifique os títulos H1 dos ficheiros Markdown de uma pasta. Documente entradas, saída, ficheiro ausente, mensagens de erro, código de saída, casos de teste e forma de executar sem alterar os ficheiros. Implemente depois a tarefa num repositório de treino e registe os resultados reais.

## Critérios de aceitação

- [ ] A especificação precede a implementação.
- [ ] Entradas e âmbito são validados.
- [ ] Sucesso, falha e entradas inválidas são testados.
- [ ] Repetições não produzem efeitos duplicados indesejados.
- [ ] As permissões são mínimas.
- [ ] Logs e relatórios não expõem informação confidencial.
- [ ] O procedimento de manutenção está documentado.

## Referências oficiais

https://docs.github.com/en/rest/guides
https://docs.github.com/en/graphql

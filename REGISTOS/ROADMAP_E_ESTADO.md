# Roadmap de desenvolvimento e validação

> **Cabeçalho histórico**  
> Projeto: CURSO_GITHUB  
> Repositório oficial: https://github.com/carlos-andrade/CURSO_GITHUB  
> Área: REGISTOS  
> Finalidade: separar trabalho planeado, escrito, testado e validado.  
> Última atualização: 2026-10-09.

## Regras de estado

- **Planeado:** existe intenção, ainda sem conteúdo suficiente.
- **Rascunho:** existe conteúdo, mas não foi revisto.
- **Em revisão:** conteúdo está a ser verificado quanto à precisão, segurança e clareza.
- **Testado:** os passos foram executados no ambiente descrito.
- **Validado:** critérios de aceitação, ligações e evidências foram verificados.
- **Publicado:** conteúdo está disponível na branch principal.

A validação automática de Markdown não prova que uma pessoa executou todos os exercícios. Nunca declarar uma lição testada apenas porque o ficheiro existe ou porque o workflow passou.

## Roadmap

| Prioridade | Entrega | Critério de saída | Estado em 2026-10-09 |
|---|---|---|---|
| P0 | Padrão editorial e método | Modelo de lição, critérios e registos consistentes | Publicado |
| P1 | Módulo 00 | Preparação, estudo, progressão e diagnóstico para iniciantes | Conteúdo publicado; prática do aluno pendente |
| P2 | Módulos 01–02 | Lições web com passos, critérios e evidências | Conteúdo reforçado; prática do aluno pendente |
| P3 | Módulo 03 | Comandos testados, contexto explícito e recuperação segura | Lições reforçadas; execução local e teste do aluno pendentes |
| P4 | Módulos 04–07 | Branch/PR, Issues, Markdown e revisão com exercícios e critérios | Lições desenvolvidas e publicadas; revisão factual e execução prática pendentes |
| P5 | Módulos 08–09 | Workflows e práticas de segurança verificados | Lições desenvolvidas e publicadas; execução prática e auditoria pendentes |
| P6 | Módulos 10–11 | Publicação, API e automação com limites claros | Lições desenvolvidas e publicadas; exercícios práticos pendentes |
| P7 | Projeto final | Critérios cumpridos e evidências registadas | Pendente |
| P8 | Auditoria global | Ligações, navegação, consistência e automatização verificadas | Parcial: verificação automática de Markdown ativa |

## Automatização publicada

- Workflow: [Validar documentação do curso](../.github/workflows/validar-curso.yml).
- Validador: [scripts/validar_curso.py](../scripts/validar_curso.py).
- Eventos: push para `main`, Pull Requests destinados a `main` e execução manual.
- Verificações: ficheiros Markdown não vazios, título H1 e destinos de ligações locais existentes e dentro do repositório.
- Limite: a verificação estrutural não valida integralmente a precisão factual, a qualidade pedagógica nem a execução prática dos exercícios.

## Registo de execução — 2026-10-09

- Reforçado o README principal com instruções de início, roadmap, método e critérios de conclusão.
- Desenvolvidos o plano de estudo e o guia de resolução de problemas.
- Criado um modelo editorial reutilizável para lições.
- Reforçadas as lições dos módulos 01 e 02 com resultados esperados, práticas guiadas, exercícios autónomos e critérios objetivos.
- Reforçadas as quatro lições do módulo 03 com passos explícitos, exemplos de comandos, verificações e avisos de recuperação segura.
- Criado o exercício integrador EX-007 para construir um README útil.
- Melhorados os modelos e os registos de progresso.
- Adicionado um workflow de validação documental; as primeiras execuções detetaram um modelo sem título H1, que foi corrigido.
- Desenvolvidas as quatro lições do módulo 04: branches, Pull Requests, revisão/merge e conflitos.
- Desenvolvidas duas lições do módulo 05: Issues/labels/milestones e Projects/templates.
- Desenvolvidas duas lições do módulo 06: Markdown essencial e README/estrutura.
- Desenvolvidas duas lições do módulo 07: revisão de contribuições e comunicação/contribuição.
- Atualizados os índices dos módulos 04–07 com sequência de leitura e critérios de conclusão.
- Desenvolvidas duas lições do módulo 08 sobre estrutura de workflows, diagnóstico, permissões e segurança.
- Desenvolvidas duas lições do módulo 09 sobre governação, dependências e resposta a incidentes.
- Atualizados os índices dos módulos 08–09 com critérios de conclusão.
- Desenvolvidas duas lições do módulo 10 sobre releases/tags e publicação com GitHub Pages.
- Desenvolvidas duas lições do módulo 11 sobre REST API, autenticação e automação sustentável.
- Atualizados os índices dos módulos 10–11 com critérios de conclusão.
- Expandida a especificação do projeto final, com fases, entregáveis e critérios verificáveis.
- A execução real dos exercícios por uma pessoa continua pendente; publicação de conteúdo não é prova de teste prático.

## Próximas ações

1. Confirmar o resultado final do workflow após as alterações dos módulos 10–11.
2. Rever ligações, sintaxe, segurança e precisão das lições 04–11.
3. Executar os exercícios dos módulos 01–11 num repositório de treino e guardar evidências; não marcar como testados antes da execução.
4. Executar o projeto final num repositório de treino e preencher o relatório com evidências.
5. Completar a auditoria global e corrigir problemas encontrados.

## Indicador global de conclusão

- Escala oficial: [STATUS DE CONCLUSÃO/ESCALA_DE_CONCLUSAO.md](../STATUS%20DE%20CONCLUS%C3%83O/ESCALA_DE_CONCLUSAO.md).
- Medição anterior: 51/100 — 51%.
- Medição atual: **54/100 — 54%**.
- Barra: `███████████████████████████░░░░░░░░░░░░░░░░░░░░░░░` **54%** (50 posições; 27 completas representam 54%).
- Variação: **+3 pontos**: +2 pelo desenvolvimento dos módulos 10–11 e +1 pela especificação verificável do projeto final; não foram atribuídos pontos por teste prático humano.
- Regra: apresentar a barra no final de cada chat do projeto e alterar a pontuação apenas quando existirem evidências de progresso ou regressão.

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
| P4 | Módulos 04–07 | Fluxo branch/PR, Issues, Markdown e revisão demonstrados | Pendente de revisão e teste |
| P5 | Módulos 08–09 | Workflows e práticas de segurança verificados | Pendente de revisão e teste |
| P6 | Módulos 10–11 | Publicação, API e automação com limites claros | Pendente de revisão e teste |
| P7 | Projeto final | Critérios cumpridos e evidências registadas | Pendente |
| P8 | Auditoria global | Ligações, navegação, consistência e automatização verificadas | Parcial: verificação automática de Markdown ativa |

## Automatização publicada

- Workflow: [Validar documentação do curso](../.github/workflows/validar-curso.yml).
- Validador: [`../scripts/validar_curso.py`](../scripts/validar_curso.py).
- Eventos: push para `main`, Pull Requests destinados a `main` e execução manual.
- Verificações: ficheiros Markdown não vazios, título H1 e destinos de ligações locais existentes e dentro do repositório.
- Execução observada: o workflow concluiu com sucesso e validou 64 ficheiros Markdown; a verificação não testa o conteúdo factual das lições nem substitui a execução dos exercícios.

## Registo de execução — 2026-10-09

- Reforçado o README principal com instruções de início, roadmap, método e critérios de conclusão.
- Desenvolvidos o plano de estudo e o guia de resolução de problemas.
- Criado um modelo editorial reutilizável para lições.
- Reforçadas as lições dos módulos 01 e 02 com resultados esperados, práticas guiadas, exercícios autónomos e critérios objetivos.
- Reforçadas as quatro lições do módulo 03 com passos explícitos, exemplos de comandos, verificações e avisos de recuperação segura.
- Criado o exercício integrador EX-007 para construir um README útil.
- Melhorados os modelos e os registos de progresso.
- Adicionado um workflow de validação documental; as primeiras execuções detetaram um modelo sem título H1, que foi corrigido. As execuções posteriores passaram.

## Próximas ações

1. Rever e testar as lições e exercícios dos módulos 01–03 num repositório de treino.
2. Aplicar o mesmo padrão aos módulos 04–07, incluindo branch, Pull Request, Issue, Markdown e revisão.
3. Prosseguir módulo a módulo, mantendo evidências e atualizando este roadmap após cada validação real.
4. Fazer auditoria final de links, precisão, segurança, acessibilidade e navegação.


## Indicador global de conclusão

- Escala oficial: [`STATUS DE CONCLUSÃO/ESCALA_DE_CONCLUSAO.md`](../STATUS%20DE%20CONCLUS%C3%83O/ESCALA_DE_CONCLUSAO.md).
- Medição inicial: **46/100 — 46%** em 2026-10-09.
- Barra: `███████████████████████░░░░░░░░░░░░░░░░░░░░░░░░░░░` **46%**.
- Regra: apresentar a barra no fim de cada chat do projeto e alterar a pontuação apenas quando existirem evidências de progresso ou regressão.

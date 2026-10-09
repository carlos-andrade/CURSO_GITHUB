# 01-02 — Repositórios, commits, branches e diff

> **Cabeçalho histórico**  
> Projeto: CURSO_GITHUB  
> Repositório oficial: https://github.com/carlos-andrade/CURSO_GITHUB  
> Módulo: 01 — Fundamentos  
> Lição: 01-02  
> Finalidade: compreender como as alterações são organizadas e revistas.  
> Estado: publicado; prática individual pendente.

## Resultado esperado

Conseguir identificar um repositório, reconhecer commits distintos, localizar uma branch e interpretar as linhas de um diff.

## Repositório

Pode conter código, documentação, imagens, configurações e histórico. A visibilidade pode ser pública ou privada, conforme as definições e permissões. Antes de publicar, confirmar que os ficheiros não contêm segredos ou dados privados.

## Commit

Um ponto identificado no histórico que regista alterações. Uma mensagem útil descreve a alteração, por exemplo:

- `docs: acrescenta instruções de instalação`
- `fix: corrige ligação no README`
- `test: adiciona verificação de documentação`

Evitar mensagens vagas como `alterações`, `teste` ou `versão final` quando não explicam o que mudou.

## Branch

Uma referência a uma linha de desenvolvimento. A branch principal costuma conter o estado integrado do projeto; branches de trabalho permitem preparar alterações isoladamente. O nome da branch e a branch atualmente selecionada não são necessariamente a mesma coisa.

## Diff

O diff apresenta as diferenças entre duas versões. Em geral, linhas adicionadas e removidas são destacadas separadamente. Rever o diff antes de concluir uma alteração ajuda a detetar conteúdo errado, ficheiros inesperados e exposição acidental de informação.

## Prática guiada na interface web

1. Abrir o repositório de treino e confirmar a branch selecionada.
2. Criar um ficheiro `NOTAS.md` com duas ou três linhas fictícias.
3. Guardar a alteração num commit com mensagem descritiva.
4. Editar uma linha do mesmo ficheiro e criar um segundo commit.
5. Abrir o histórico e selecionar cada commit.
6. Comparar os diffs e identificar exatamente a linha modificada.

## Exercício autónomo

Criar uma terceira alteração pequena, com objetivo diferente dos anteriores. Antes de guardar, confirmar o nome do ficheiro, o conteúdo e a mensagem do commit.

## Critérios de aceitação

- [ ] Existem pelo menos dois commits distintos.
- [ ] As mensagens descrevem as alterações realizadas.
- [ ] Sei qual branch estou a consultar.
- [ ] Consigo explicar uma diferença mostrada pelo diff.
- [ ] Registei a URL do commit ou do histórico.
- [ ] O ficheiro não contém dados sensíveis.

## Erros frequentes

- **Commit sem mensagem útil:** a mensagem deve descrever a intenção da alteração.
- **Editar a branch errada:** confirmar sempre o nome da branch antes de alterar.
- **Não rever o diff:** abrir o diff antes de considerar a tarefa terminada.

## Fonte oficial

- GitHub Docs — About commits: https://docs.github.com/en/pull-requests/committing-changes-to-your-project/creating-and-editing-commits/about-commits
- GitHub Docs — About branches: https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-branches

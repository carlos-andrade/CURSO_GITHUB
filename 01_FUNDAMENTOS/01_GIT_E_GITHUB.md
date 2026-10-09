# 01-01 — Git e GitHub

> **Cabeçalho histórico**  
> Projeto: CURSO_GITHUB  
> Repositório oficial: https://github.com/carlos-andrade/CURSO_GITHUB  
> Módulo: 01 — Fundamentos  
> Lição: 01-01  
> Finalidade: distinguir o controlo de versões da plataforma de colaboração.  
> Estado: publicado; exercício individual pendente.

## Resultado esperado

Conseguir explicar a diferença entre Git e GitHub e localizar ficheiros, commits e diffs num repositório.

## Conceitos essenciais

- **Git:** sistema distribuído de controlo de versões. Regista alterações em commits e permite trabalhar com branches.
- **GitHub:** plataforma que aloja repositórios Git e acrescenta colaboração, Issues, Pull Requests, revisão, Actions e publicação.
- **Repositório:** ficheiros do projeto mais o histórico de versões e metadados relevantes.
- **Commit:** registo identificado de alterações; não é simplesmente uma cópia de segurança de todo o computador.
- **Branch:** referência a uma linha de desenvolvimento, usada para isolar trabalho antes de o integrar.
- **Remote (remoto):** nome que aponta para outro repositório, por exemplo um repositório alojado no GitHub.
- **Diff:** comparação que mostra o que foi adicionado, removido ou alterado.

Git pode funcionar localmente sem GitHub. GitHub depende frequentemente de Git para controlo de versões, mas inclui funcionalidades que não fazem parte do Git em si.

## Prática guiada — explorar um repositório

1. Abrir um repositório de treino no GitHub.
2. Na página principal, localizar a lista de ficheiros e abrir o `README.md`.
3. Abrir o histórico de commits.
4. Selecionar um commit e procurar a secção de alterações (diff).
5. Identificar a mensagem, o autor, a data e os ficheiros alterados.
6. Voltar à página do repositório e identificar a branch selecionada.

**Resultado esperado:** conseguir apontar para um ficheiro, um commit e o diff desse commit.

## Exercício autónomo

Escolher dois commits de um repositório de treino e explicar, em três ou quatro frases, o que mudou entre eles. Se o repositório ainda não tiver histórico suficiente, realizar primeiro o exercício [`EX-002`](../EXERCICIOS/EX-002-COMMIT-E-HISTORICO.md).

## Critérios de aceitação

- [ ] Explico Git e GitHub sem os tratar como sinónimos.
- [ ] Localizo o README e a branch selecionada.
- [ ] Abro o histórico e identifico um commit.
- [ ] Leio o diff e descrevo pelo menos uma alteração.
- [ ] Registo a URL da evidência sem expor informação privada.

## Erros frequentes

- **“GitHub é o Git”:** distinguir a ferramenta de controlo de versões da plataforma.
- **“O commit guarda tudo no computador”:** o commit regista alterações no repositório, não faz uma cópia integral do dispositivo.
- **“Apagar um ficheiro apaga o histórico”:** o ficheiro pode continuar presente em commits anteriores.

## Fontes oficiais

- GitHub Docs — About Git and GitHub: https://docs.github.com/en/get-started/start-your-journey/about-github-and-git
- Git Book: https://git-scm.com/book/en/v2/Getting-Started-About-Version-Control

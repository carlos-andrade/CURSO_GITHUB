# Preparar o ambiente de aprendizagem

> **Cabeçalho histórico**  
> Projeto: CURSO_GITHUB  
> Repositório oficial: https://github.com/carlos-andrade/CURSO_GITHUB  
> Módulo: 00 — Orientação e preparação  
> Lição: 00-02  
> Finalidade: preparar um ambiente de treino seguro antes de executar alterações.  
> Estado: publicado; configuração individual pendente de confirmação.

## Parte A — Preparação pela interface web

1. Abrir https://github.com/ e iniciar sessão.
2. Confirmar que está na conta correta.
3. Criar um repositório de treino com um nome claro, por exemplo `treino-github`.
4. Para o primeiro exercício, pode escolher um repositório público sem dados privados ou um repositório privado se a conta o permitir.
5. Inicializar o repositório com um README.
6. Abrir o README, confirmar o conteúdo e localizar o histórico de commits.
7. Registar o URL do repositório no relatório de progresso.

**Verificação esperada:** o repositório abre, o README aparece na página inicial e existe pelo menos um commit no histórico.

## Parte B — Preparação para o módulo local

O terminal só é necessário a partir do módulo 03.

1. Instalar Git a partir de https://git-scm.com/downloads.
2. Abrir um terminal novo.
3. Executar:

   ```bash
   git --version
   ```

4. Confirmar que é apresentada uma versão do Git.
5. Configurar nome e e-mail de autoria apenas depois de compreender que estes dados podem aparecer nos commits. Usar os dados de autoria adequados ao contexto.
6. Usar um método de autenticação suportado pelo GitHub. Nunca escrever um token diretamente num comando que possa ficar guardado no histórico do terminal.

A configuração de Git local será praticada e explicada com mais detalhe no módulo 03.

## Segurança antes de começar

- Não usar repositórios de produção para aprender comandos de recuperação.
- Não carregar ficheiros com palavras-passe, tokens, chaves privadas, cookies ou dados pessoais desnecessários.
- Um repositório público pode ser visto por qualquer pessoa; apagar um ficheiro num commit posterior não garante que o conteúdo anterior deixe de estar acessível no histórico.
- Antes de publicar, rever o nome do repositório, a visibilidade e os ficheiros incluídos.

## Checklist de verificação

- [ ] Consigo abrir o repositório de treino.
- [ ] O README aparece na página inicial.
- [ ] Consigo localizar o histórico de commits.
- [ ] Sei se o repositório é público ou privado.
- [ ] Não foram adicionados segredos nem dados privados.
- [ ] Registei o URL e o estado da preparação.

## Se algo falhar

Consultar [`04_RESOLUCAO_DE_PROBLEMAS.md`](04_RESOLUCAO_DE_PROBLEMAS.md). Registar a mensagem de erro sem credenciais e não repetir operações desconhecidas às cegas.

## Fontes oficiais

- GitHub Docs — https://docs.github.com/
- Instalação de Git — https://git-scm.com/downloads
- Git Book — https://git-scm.com/book/

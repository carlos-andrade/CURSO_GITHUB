# Resolução de problemas para iniciantes

> **Cabeçalho histórico**  
> Projeto: CURSO_GITHUB  
> Repositório oficial: https://github.com/carlos-andrade/CURSO_GITHUB  
> Área: 00_ORIENTACAO  
> Finalidade: orientar diagnóstico seguro antes de pedir ajuda ou repetir comandos.  
> Estado: versão inicial.

## Método de diagnóstico

1. **Parar:** não repetir às cegas uma operação que falhou.
2. **Ler a mensagem completa:** identificar o comando, o ficheiro e a linha relevantes.
3. **Confirmar o contexto:** repositório, branch, pasta e conta corretos.
4. **Verificar o estado atual:** consultar a interface ou executar comandos de leitura.
5. **Fazer uma única correção de cada vez.**
6. **Repetir a verificação** e registar o resultado.
7. **Pedir ajuda com contexto suficiente**, removendo tokens, e-mails privados e outros dados sensíveis.

## Problemas frequentes

### Não encontro um ficheiro
- Confirmar se está no repositório e branch corretos.
- Usar a pesquisa de ficheiros do GitHub ou navegar pela árvore.
- Verificar maiúsculas, minúsculas, espaços e extensão do ficheiro.

### A alteração não aparece no GitHub
- Na interface web, confirmar se a edição foi guardada através de um commit.
- No Git local, verificar `git status`, branch atual e destino do push.
- Confirmar que está a consultar o repositório remoto correto.

### O push é recusado
- Ler a mensagem integral e verificar autenticação, permissões e divergência entre branches.
- Não usar `--force` como tentativa genérica.
- Se o remoto tiver commits novos, compreender primeiro como sincronizar sem perder trabalho.

### Um Pull Request mostra conflitos
- Não apagar marcadores de conflito sem decidir qual conteúdo deve prevalecer.
- Fazer uma cópia ou confirmar que o trabalho está commitado.
- Resolver os conflitos, rever o diff e executar as verificações antes de concluir.

### Uma GitHub Action falha
- Abrir a execução, identificar o primeiro passo que falhou e ler o log desse passo.
- Distinguir erro real, aviso e anotação informativa.
- Verificar permissões, caminhos, nomes de secrets e versões de ações.
- Não publicar logs que revelem credenciais ou dados privados.

### Comando potencialmente destrutivo
Antes de usar comandos como `git reset --hard`, `git clean` ou operações de force push:
- confirmar o diretório e a branch;
- ler a documentação do comando;
- verificar se há trabalho não guardado;
- preferir uma alternativa reversível;
- não executar se o efeito não estiver claro.

## Modelo para pedir ajuda

- Objetivo:
- Repositório (público ou descrição sem dados privados):
- Branch e pasta:
- Passos executados:
- Mensagem de erro exata, expurgada de segredos:
- Resultado esperado:
- Resultado observado:
- O que já foi verificado:
- Evidência pública ou captura devidamente anonimizada:

## Referências oficiais

- GitHub Docs — https://docs.github.com/
- Git Book — https://git-scm.com/book/
- Git Reference — https://git-scm.com/docs

# 03-01 — Instalação e configuração do Git

> **Cabeçalho histórico**  
> Projeto: CURSO_GITHUB  
> Repositório oficial: https://github.com/carlos-andrade/CURSO_GITHUB  
> Módulo: 03 — Git local e linha de comandos  
> Lição: 03-01  
> Finalidade: preparar Git local e compreender a identidade de autoria.  
> Estado: publicado; teste num computador de treino pendente.

## Resultado esperado

Confirmar que Git está instalado, configurar a identidade de autoria adequada e verificar a configuração sem publicar dados locais.

## Instalar e confirmar

1. Instalar Git a partir de https://git-scm.com/downloads.
2. Abrir um terminal novo.
3. Executar:

   ```bash
   git --version
   ```

4. Confirmar que é apresentada uma versão. Se o comando não for reconhecido, verificar a instalação e abrir um terminal novo antes de repetir.

## Configurar identidade de autoria

Os valores abaixo são exemplos; substituir pelos dados apropriados ao contexto. A identidade pode ficar visível no histórico dos commits.

```bash
git config --global user.name "Nome de autoria"
git config --global user.email "email-de-autoria@example.com"
```

Verificar os valores:

```bash
git config --global --get user.name
git config --global --get user.email
```

Para inspecionar outras definições:

```bash
git config --list
```

Este último comando pode mostrar dados pessoais ou caminhos locais. Não copiar a saída integral para um repositório público ou para um pedido de ajuda sem a rever.

## Exercício autónomo

Executar os comandos de verificação e registar apenas a versão do Git e se a identidade ficou configurada. Não guardar os dados de configuração pessoais no repositório de treino.

## Critérios de aceitação

- [ ] `git --version` apresenta uma versão.
- [ ] `user.name` e `user.email` têm os valores pretendidos.
- [ ] Sei explicar que a identidade é associada aos commits.
- [ ] Não publiquei a saída completa de configuração nem credenciais.
- [ ] Registei o resultado e qualquer erro encontrado.

## Fontes oficiais

- Git Downloads: https://git-scm.com/downloads
- Git Book — First-Time Git Setup: https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup

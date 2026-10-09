# 10.2 — Publicar e verificar com GitHub Pages

> **Cabeçalho histórico**  
> Projeto: CURSO_GITHUB  
> Repositório: https://github.com/carlos-andrade/CURSO_GITHUB  
> Módulo: 10 — Releases e GitHub Pages  
> Finalidade: publicar um site estático e verificar o resultado efetivamente disponibilizado.  
> Estado: conteúdo desenvolvido; deployment de treino pendente.  
> Última atualização: 2026-10-09.

## Antes da publicação

GitHub Pages serve sites estáticos. Não é um servidor para executar diretamente aplicações backend que precisem de um processo de servidor persistente. Confirme os requisitos do site, a licença dos conteúdos, a visibilidade do repositório e a presença de informação privada.

## Preparar um site mínimo

Num repositório de treino, crie `index.html` na origem escolhida:

```html
<!doctype html>
<html lang="pt">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Site de treino</title>
</head>
<body>
  <main>
    <h1>O meu primeiro site</h1>
    <p>Publicado para aprender GitHub Pages.</p>
  </main>
</body>
</html>
```

Este exemplo é intencionalmente simples. Antes de publicar um site real, acrescente conteúdo adequado, teste ligações, navegação por teclado e apresentação em ecrãs pequenos.

## Configurar Pages

1. Abra **Settings** no repositório de treino.
2. Entre em **Pages**.
3. Selecione uma origem suportada pelas opções disponíveis no repositório, como uma branch e pasta, ou um workflow de deployment.
4. Guarde a configuração.
5. Acompanhe o workflow de deployment, se aplicável.
6. Aguarde a publicação e abra o URL apresentado pelo GitHub.
7. Confirme que a página correta, os recursos e as ligações funcionam.

Os menus e opções disponíveis podem variar com as permissões, políticas e configuração do repositório. Não assuma que o URL está publicado só porque o ficheiro existe.

## Diagnóstico

- **Página não encontrada:** confirme a origem, branch, pasta e nome do ficheiro inicial.
- **Alterações não aparecem:** confirme o commit implantado, o estado do deployment e a cache do navegador.
- **Imagens ou CSS falham:** verifique caminhos relativos e maiúsculas/minúsculas.
- **Links quebrados:** teste o caminho a partir do URL publicado; sites de projeto podem exigir prefixo de caminho.
- **Workflow falha:** leia o primeiro step com erro e siga os logs.

## Exercício verificável

Publique a página de treino. Guarde a ligação ao repositório, a configuração da origem, o URL publicado e uma lista de verificações. Altere o texto da página, publique de novo e confirme a alteração no URL.

## Critérios de aceitação

- [ ] O conteúdo publicado não inclui segredos nem dados privados.
- [ ] A origem e o commit implantado foram identificados.
- [ ] O URL abre sem erro e mostra a versão esperada.
- [ ] Os caminhos de imagens, CSS e ligações foram testados.
- [ ] A página tem título, idioma e viewport configurados.
- [ ] A evidência do deployment foi registada.

## Referência oficial

https://docs.github.com/en/pages

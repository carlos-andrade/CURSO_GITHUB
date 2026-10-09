# 02-03 — Visibilidade e permissões

> **Cabeçalho histórico**  
> Projeto: CURSO_GITHUB  
> Repositório oficial: https://github.com/carlos-andrade/CURSO_GITHUB  
> Módulo: 02 — Interface do GitHub  
> Lição: 02-03  
> Finalidade: compreender quem pode ver o conteúdo e que ações pode executar.  
> Estado: publicado; inspeção individual pendente.

## Resultado esperado

Conseguir distinguir visibilidade de permissões e avaliar o risco de publicar conteúdo num repositório.

## Conceitos

- **Público:** o conteúdo público pode ser visto por qualquer pessoa. Não colocar informação confidencial num repositório público.
- **Privado:** o acesso é limitado ao proprietário e às pessoas ou equipas autorizadas.
- **Leitura:** permite consultar conteúdo, sem necessariamente permitir alterá-lo.
- **Escrita:** permite contribuir com alterações, dentro das regras do repositório.
- **Manutenção/administração:** níveis com capacidades adicionais de gestão; os poderes exatos dependem do papel e da configuração.

A visibilidade responde a “quem pode ver?”; as permissões respondem a “que ações pode executar?”. Uma pessoa autorizada a ler um repositório privado não tem automaticamente permissão para escrever ou administrar.

## Prática segura

1. Abrir as definições do repositório de treino, se tiver acesso.
2. Identificar a visibilidade atual sem a alterar.
3. Localizar a área de acesso, colaboradores ou permissões, se disponível.
4. Anotar que papel tem a própria conta, sem divulgar dados privados.
5. Confirmar que o repositório não contém segredos nem dados que não deveriam ser públicos.

**Não alterar a visibilidade de um repositório real como exercício.** A mudança pode expor conteúdo do histórico e afetar colaboradores ou automatizações.

## Exercício autónomo

Criar uma tabela no relatório com duas colunas — “visibilidade” e “permissões” — e dar um exemplo de cada. Descrever um risco de publicar acidentalmente um token.

## Critérios de aceitação

- [ ] Explico a diferença entre público e privado.
- [ ] Distingo leitura, escrita e administração.
- [ ] Identifico onde consultar a visibilidade.
- [ ] Explico por que apagar um segredo num commit posterior pode não eliminar a exposição anterior.
- [ ] Registo a evidência sem publicar nomes ou dados privados desnecessários.

## Fonte oficial

- GitHub Docs — Repository permissions: https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/managing-repository-settings/setting-repository-visibility
- GitHub Docs — Access permissions: https://docs.github.com/en/organizations/managing-access-to-your-organizations-repositories/repository-roles-for-an-organization

# 11.1 — REST API, respostas e autenticação

> **Cabeçalho histórico**  
> Projeto: CURSO_GITHUB  
> Repositório: https://github.com/carlos-andrade/CURSO_GITHUB  
> Módulo: 11 — API e tópicos avançados  
> Finalidade: compreender uma chamada HTTP à API do GitHub e tratar a resposta com segurança.  
> Estado: conteúdo desenvolvido; chamada prática pelo aluno pendente.  
> Última atualização: 2026-10-09.

## Conceitos essenciais

Uma API expõe recursos através de uma interface definida. Na REST API do GitHub, uma chamada tem normalmente:
- método HTTP, como `GET`, `POST`, `PATCH` ou `DELETE`;
- endpoint;
- parâmetros e cabeçalhos;
- código de estado HTTP;
- resposta, frequentemente em JSON.

Use `GET` para os exercícios iniciais de leitura. Operações de escrita devem ser feitas apenas em recursos próprios ou em ambiente para o qual tenha autorização.

## Primeira chamada sem token

Exemplo de leitura de metadados públicos de um repositório. Execute num terminal com uma ferramenta HTTP instalada:

```bash
curl -sS -H "Accept: application/vnd.github+json" \
  -H "X-GitHub-Api-Version: 2022-11-28" \
  https://api.github.com/repos/octocat/Hello-World
```

Este exemplo consulta um repositório público e não inclui credenciais. As políticas, limites e respostas podem variar. Para exercícios repetíveis, registe o código de estado e uma amostra da resposta JSON, sem dados pessoais.

## Interpretar a resposta

- **2xx:** o pedido foi processado com sucesso; leia o corpo para confirmar o resultado esperado.
- **3xx:** pode existir redirecionamento.
- **4xx:** reveja autenticação, permissões, endpoint, parâmetros e limites.
- **5xx:** falha do serviço; siga a documentação e evite repetir agressivamente.

Um código de sucesso não garante que todos os campos esperados estejam presentes. Valide o esquema e trate campos opcionais.

## Autenticação e permissões

Quando a operação exige autenticação, use uma credencial autorizada com as permissões mínimas. Em scripts locais, prefira variáveis de ambiente ou um gestor de segredos. Não inclua tokens em argumentos que possam ficar registados, screenshots, commits ou logs. Não partilhe uma credencial para facilitar a reprodução do exercício.

Se um token for exposto, revogue-o ou rode-o de imediato e investigue a exposição. Não basta apagar o token do ficheiro atual.

## Limites de utilização

A API aplica limites de utilização e pode responder com cabeçalhos que ajudam a perceber o estado do limite. Trate respostas de limite com espera adequada, reduza chamadas desnecessárias, use paginação e cache quando apropriado. Não contorne limites através de múltiplas contas ou credenciais.

## Exercício verificável

1. Execute a chamada pública acima ou consulte o endpoint pela documentação.
2. Registe endpoint, método, código HTTP e três campos da resposta.
3. Identifique como a documentação descreve autenticação e limites.
4. Guarde a evidência sem dados pessoais ou tokens.
5. Se o endpoint não estiver disponível, registe o erro real e a data, sem inventar uma resposta.

## Critérios de aceitação

- [ ] O endpoint e o método estão identificados.
- [ ] O código HTTP foi observado e interpretado.
- [ ] Os campos JSON são lidos com precisão.
- [ ] Credenciais não aparecem no código, histórico ou logs.
- [ ] Os limites e a paginação foram considerados.
- [ ] A evidência corresponde à chamada realmente executada.

## Referência oficial

https://docs.github.com/en/rest

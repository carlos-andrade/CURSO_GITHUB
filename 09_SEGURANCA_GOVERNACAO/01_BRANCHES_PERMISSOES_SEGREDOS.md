# 09.1 — Branches protegidas, permissões e segredos

> **Cabeçalho histórico**  
> Projeto: CURSO_GITHUB  
> Repositório: https://github.com/carlos-andrade/CURSO_GITHUB  
> Módulo: 09 — Segurança e governação  
> Finalidade: reduzir alterações não autorizadas, exposição de credenciais e risco operacional.  
> Estado: conteúdo desenvolvido; auditoria prática das definições do aluno pendente.  
> Última atualização: 2026-10-09.

## Modelo de segurança

A segurança do repositório combina identidade, permissões, regras de integração, proteção de segredos, revisão de alterações e monitorização. Nenhuma definição isolada garante segurança total.

## Acesso e permissões

1. Conceda apenas o nível de acesso necessário à tarefa.
2. Revise periodicamente colaboradores, equipas e aplicações autorizadas.
3. Remova acessos quando deixam de ser necessários.
4. Use autenticação multifator na conta e siga as políticas da organização.
5. Não partilhe tokens pessoais nem os copie para Issues, PRs ou documentação.

Os nomes e as opções disponíveis dependem do tipo de conta, do plano e das políticas organizacionais.

## Regras de branch e integração

Para a branch principal, considere exigir Pull Requests, revisões, checks obrigatórios e resolução de conversas. Ative apenas regras compatíveis com a capacidade real da equipa para as cumprir. Teste as regras num repositório de treino antes de as aplicar a um projeto crítico.

Uma regra obrigatória deve referir-se ao check correto e estável. Evite tornar dezenas de checks redundantes obrigatórios sem perceber dependências, nomes e eventos. Não desative proteções para contornar uma falha; investigue a origem.

## Segredos

- Nunca versionar ficheiros `.env`, chaves privadas, tokens ou palavras-passe.
- Use placeholders claramente falsos em exemplos.
- Se um segredo for publicado, considere-o comprometido: revogue/rode a credencial no serviço de origem e avalie o histórico, logs e acessos.
- Apagar a linha num commit posterior não garante que o segredo deixou de estar acessível no histórico.
- Use secrets do GitHub Actions apenas nos workflows e contextos necessários.

## Visibilidade do repositório

Antes de tornar um repositório público, reveja código, Issues, histórico, documentação, artefactos, configuração e dados pessoais. “Público” significa que o conteúdo pode ser copiado; mudar depois para privado não apaga cópias externas.

## Exercício verificável

Num repositório de treino, documente as permissões atuais, as regras da branch principal e os checks exigidos. Identifique um risco e proponha uma correção. Aplique mudanças apenas se tiver autorização e uma forma de recuperação.

## Critérios de aceitação

- [ ] Os acessos correspondem às responsabilidades.
- [ ] A branch principal tem regras adequadas ao risco.
- [ ] Os checks obrigatórios são identificados corretamente.
- [ ] Nenhum segredo real está no código ou nos exemplos.
- [ ] Existe um procedimento de resposta a exposição de credenciais.
- [ ] As alterações de governação foram verificadas.

## Referência oficial

https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository

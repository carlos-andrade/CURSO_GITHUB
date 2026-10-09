# 09.2 — Dependências, alertas e resposta a incidentes

> **Cabeçalho histórico**  
> Projeto: CURSO_GITHUB  
> Repositório: https://github.com/carlos-andrade/CURSO_GITHUB  
> Módulo: 09 — Segurança e governação  
> Finalidade: identificar riscos em dependências e responder a incidentes sem agravar a exposição.  
> Estado: conteúdo desenvolvido; auditoria prática pendente.  
> Última atualização: 2026-10-09.

## Dependências e cadeia de fornecimento

Projetos podem depender de bibliotecas, actions, imagens de contentores e ferramentas externas. Uma dependência pode introduzir vulnerabilidades ou ser comprometida. Mantenha inventário e atualizações controladas, leia os avisos e teste alterações antes da integração.

Consoante a linguagem, a configuração e o plano do GitHub, podem existir ferramentas como Dependabot alerts, Dependabot security updates, dependency graph e code scanning. A disponibilidade varia; confirme o que está ativo no repositório em vez de assumir que todos os recursos estão ligados.

## Processo de triagem de um alerta

1. Identifique o pacote, versão afetada, caminho de dependência e severidade reportada.
2. Leia a referência técnica do alerta e confirme se a dependência é usada no projeto.
3. Avalie exposição, possibilidade de exploração e impacto no contexto real.
4. Identifique uma versão corrigida ou uma mitigação documentada.
5. Faça a atualização numa branch e reveja o diff.
6. Execute testes relevantes e observe compatibilidade.
7. Abra um PR com o alerta, a alteração, os testes e qualquer risco residual.
8. Registe a decisão se o alerta não puder ser corrigido imediatamente.

Não ignore um alerta apenas porque não há falhas visíveis. Também não atualize indiscriminadamente dependências de produção sem avaliar compatibilidade e risco.

## Resposta a segredo exposto

1. Trate a credencial como comprometida.
2. Revogue-a ou rode-a no serviço que a emitiu.
3. Verifique uso indevido e registos de acesso, se disponíveis.
4. Remova a credencial do código e dos fluxos de execução.
5. Avalie o histórico Git, forks, logs, caches e artefactos; uma alteração posterior não apaga todas as cópias.
6. Notifique os responsáveis segundo o processo do projeto.
7. Registe causa, alcance, medidas corretivas e ações preventivas sem copiar o segredo para o relatório.

A prioridade é invalidar a credencial, não fazer desaparecer primeiro a linha de código. Não cole o segredo num Issue para pedir ajuda.

## Resposta a um incidente

Preserve evidências relevantes, limite acessos comprometidos, comunique aos responsáveis e siga o plano de resposta da organização. Não destrua logs ou histórico sem orientação. Se houver risco de dados pessoais ou obrigações legais, encaminhe para os responsáveis autorizados.

## Exercício verificável

Num repositório de treino sem credenciais reais, simule a análise de um alerta público de dependência e redija um plano de resposta a um segredo fictício. Identifique passos, responsáveis e evidências esperadas. Não introduza deliberadamente um segredo real nem explore sistemas de terceiros.

## Critérios de aceitação

- [ ] O alerta foi interpretado com base na fonte técnica.
- [ ] O risco e a mitigação estão documentados.
- [ ] A atualização é isolada e testável.
- [ ] O procedimento de exposição prioriza revogar/rodar a credencial.
- [ ] A resposta preserva evidências e evita divulgar o segredo.
- [ ] As limitações de ferramentas e permissões estão registadas.

## Referência oficial

https://docs.github.com/en/code-security/dependabot/dependabot-alerts/about-dependabot-alerts

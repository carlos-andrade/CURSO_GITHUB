# Diagnóstico e segurança em Actions

> Projeto: CURSO_GITHUB | Módulo 08 | Lição 02

## Diagnóstico
Começar pelo estado do workflow, job e step que falhou. Ler o erro original, reproduzir quando possível, corrigir a causa e repetir a execução.

## Segurança
- Definir permissões mínimas para o GITHUB_TOKEN.
- Guardar credenciais em secrets, nunca no código.
- Não imprimir segredos nos logs.
- Rever Actions de terceiros e respetivas versões.
- Separar workflows de validação de operações de publicação sensíveis.

Referência: https://docs.github.com/en/actions/security-guides
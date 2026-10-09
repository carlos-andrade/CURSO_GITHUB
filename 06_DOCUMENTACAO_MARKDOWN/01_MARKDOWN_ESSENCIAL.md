# 06.1 — Markdown essencial

> **Cabeçalho histórico**  
> Projeto: CURSO_GITHUB  
> Repositório: https://github.com/carlos-andrade/CURSO_GITHUB  
> Módulo: 06 — Documentação e Markdown  
> Finalidade: formatar documentação legível, consistente e fácil de manter.  
> Estado: conteúdo desenvolvido; renderização no GitHub pelo aluno pendente.  
> Última atualização: 2026-10-09.

## Elementos essenciais

| Resultado | Sintaxe |
|---|---|
| Título principal | `# Título` |
| Subtítulo | `## Secção` |
| Ênfase | `**texto importante**` |
| Itálico | `*termo*` |
| Lista | `- item` |
| Lista numerada | `1. primeiro passo` |
| Tarefa por marcar | `- [ ] passo pendente` |
| Tarefa concluída | `- [x] passo concluído` |
| Código inline | `git status` |
| Bloco de código | três acentos graves antes e depois |
| Ligação | `[texto](https://exemplo.com)` |
| Imagem | `![descrição](caminho/imagem.png)` |
| Citação | `> texto citado` |

Use títulos hierárquicos: um H1 por documento e H2 para secções principais. Não escolha níveis apenas pela aparência.

## Blocos de código

Indique a linguagem quando possível para realce de sintaxe:

```bash
git status
git log --oneline -5
```

Comandos devem ser copiados apenas depois de confirmar o diretório e o contexto. Explique o resultado esperado e avise sobre comandos que alterem ou eliminem dados.

## Ligações

Prefira texto descritivo, como `[Guia de instalação](02_PREPARAR_AMBIENTE.md)`, em vez de “clique aqui”. Ligações relativas facilitam a navegação dentro do repositório. Confirme maiúsculas, espaços, extensão e destino; alguns sistemas distinguem maiúsculas de minúsculas.

## Acessibilidade e legibilidade

- Use texto alternativo significativo nas imagens.
- Não dependa apenas da cor para transmitir estado.
- Dê nomes descritivos às secções e às ligações.
- Evite tabelas muito largas e parágrafos excessivamente longos.
- Explique siglas na primeira ocorrência.
- Mantenha exemplos e resultados esperados juntos.

## Exercício verificável

Crie um ficheiro `README-treino.md` com H1, três H2, lista, bloco de comandos, ligação relativa, imagem com texto alternativo (se houver imagem) e checklist. Abra a pré-visualização no GitHub e corrija problemas de renderização.

## Critérios de aceitação

O documento tem hierarquia lógica, sintaxe renderizada corretamente, ligações válidas e instruções compreensíveis sem depender da formatação visual.

## Referência oficial

https://docs.github.com/en/get-started/writing-on-github

# 04.2 — Abrir um Pull Request

> **Cabeçalho histórico**  
> Projeto: CURSO_GITHUB  
> Repositório: https://github.com/carlos-andrade/CURSO_GITHUB  
> Módulo: 04 — Branches e Pull Requests  
> Finalidade: propor e documentar uma alteração antes de a integrar.  
> Estado: conteúdo desenvolvido; execução prática pelo aluno pendente.  
> Última atualização: 2026-10-09.

## Objetivos

Criar um Pull Request (PR), escolher corretamente a branch de destino e a branch de origem, descrever a alteração e indicar como foi verificada.

## Antes de abrir

1. Confirme que a branch de trabalho está publicada.
2. Revise os ficheiros alterados e o diff completo.
3. Confirme que não incluiu segredos, credenciais, dados pessoais ou ficheiros temporários.
4. Confirme que a alteração tem um objetivo pequeno e claro.
5. Verifique se a branch de destino é a pretendida. Não presuma que é sempre `main`.

## Criar pela interface

1. Abra o repositório no GitHub.
2. Se surgir a sugestão para comparar a branch publicada, selecione-a; caso contrário, abra **Pull requests** e escolha **New pull request**.
3. Selecione a base (destino) e compare (origem).
4. Inspecione a lista de commits e o separador **Files changed**.
5. Dê ao PR um título que descreva o resultado, não apenas “alterações”.
6. Preencha a descrição usando o modelo abaixo.
7. Crie o PR como rascunho se ainda não estiver pronto para revisão; caso contrário, solicite revisão conforme as regras do repositório.

## Modelo de descrição

- **Objetivo:** que problema resolve?
- **Alteração:** o que mudou?
- **Como testar:** quais os passos executados?
- **Resultado observado:** o que aconteceu?
- **Riscos/limitações:** o que não foi testado ou pode falhar?
- **Checklist:** documentação atualizada, diff revisto e segredos excluídos.

Não escreva “testado” se apenas leu o ficheiro. Distinguir revisão visual, validação automática e execução prática.

## Exercício verificável

Abra um PR que acrescente uma secção a um documento do repositório de treino. Não faça merge ainda. Confirme que o PR mostra apenas os ficheiros esperados e que a base/origem estão corretas.

## Critérios de aceitação

- [ ] A branch de origem é a branch de trabalho.
- [ ] A branch base é a pretendida.
- [ ] O título identifica o objetivo.
- [ ] A descrição explica teste e resultado real.
- [ ] O diff foi inspecionado.
- [ ] Não foram expostos segredos.
- [ ] O estado de rascunho/revisão corresponde à maturidade da alteração.

## Evidência a guardar

Ligação do PR, branch base, branch de origem, checklist preenchida e resultado das verificações.

## Referência oficial

https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests

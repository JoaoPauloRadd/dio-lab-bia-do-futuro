# Base de Conhecimento

## Dados Utilizados

Nesta solução, a base de conhecimento foi adaptada para o contexto de um agente educacional de finanças para iniciantes em análise de dados financeiros.

Os arquivos da pasta `data` foram reorganizados para apoiar explicações didáticas, personalização do aprendizado e resolução de exercícios práticos com dados simples.


| Arquivo | Formato | Utilização no Agente |
|---------|---------|---------------------|
| `historico_atendimento.csv` | CSV | Contextualiza dúvidas já feitas por usuários, permitindo ao agente identificar temas recorrentes, exemplos frequentes e dificuldades comuns |
| `perfil_aluno.json` | JSON | Personaliza as respostas com base no nível do usuário, objetivos de aprendizagem, dificuldades e formato preferido de explicação |
| `metricas_financeiras.json` | JSON | Funciona como base principal de conceitos, fórmulas, interpretações, erros comuns e exemplos de KPIs e métricas financeiras |
| `transacoes.csv` | CSV | Oferece dados fictícios e estruturados para cálculos práticos, comparações entre períodos e explicações aplicadas |


> Esta base foi construída com dados mockados e exemplos didáticos para facilitar o uso no contexto do bootcamp. Caso necessário, ela pode ser expandida com mais métricas, séries históricas ou estudos de caso mais robustos, desde que permaneça aderente ao objetivo educacional do agente.

---

## Adaptações nos Dados

> Você modificou ou expandiu os dados mockados? Descreva aqui.

Os dados mockados originais do projeto foram adaptados para refletir o novo escopo do agente.

Inicialmente, a base estava voltada para um assistente financeiro com foco em perfil de investidor, produtos financeiros e transações pessoais. Como o agente foi redefinido como um tutor de finanças para iniciantes, a base passou a priorizar aprendizagem, interpretação de indicadores e cálculo de métricas básicas.

As principais adaptações realizadas foram:

- manutenção do arquivo `historico_atendimento.csv`, mas com substituição do conteúdo para dúvidas sobre receita, lucro, margem, fluxo de caixa, crescimento percentual e outros temas introdutórios de análise financeira;
- substituição de `perfil_investidor.json` por `perfil_aluno.json`, deixando de armazenar informações ligadas a risco e investimentos e passando a armazenar objetivos de aprendizagem, nível de conhecimento e dificuldades do usuário;
- substituição de `produtos_financeiros.json` por `metricas_financeiras.json`, transformando a antiga base de produtos em uma base estruturada de métricas e KPIs financeiros;
- substituição de `transacoes.csv` por `casos_financeiros.csv`, criando uma base de exemplos numéricos para exercícios, simulações e interpretações feitas pelo agente.

Com isso, a base de conhecimento passou a servir melhor a um cenário de ensino guiado, em vez de recomendação de produtos ou análise de comportamento de consumo.


---

## Estratégia de Integração

### Como os dados são carregados?
> Descreva como seu agente acessa a base de conhecimento.

Os arquivos JSON e CSV da pasta `data` são carregados pela aplicação no início da sessão ou quando necessário para montar o contexto do agente.

Cada arquivo cumpre um papel específico:

- `perfil_aluno.json` fornece o contexto individual do usuário;
- `metricas_financeiras.json` fornece o conteúdo conceitual e técnico;
- `historico_atendimento.csv` oferece memória de dúvidas e exemplos anteriores;
- `transacoes.csv` fornece dados estruturados para cálculos e exercícios.

Após o carregamento, os dados são convertidos para estruturas que possam ser facilmente resumidas e injetadas no contexto do modelo, evitando excesso de texto e priorizando apenas as informações úteis para a pergunta atual.

### Como os dados são usados no prompt?

Os dados não são enviados integralmente no system prompt o tempo todo. Em vez disso, a aplicação utiliza uma estratégia de contexto orientado à consulta.

O system prompt define a persona, o comportamento, as limitações e o tom do agente. Já os dados da base de conhecimento são consultados dinamicamente e incluídos no contexto conforme o tipo de pergunta feita pelo usuário.

Exemplos de uso:

- quando o usuário pergunta “o que é margem líquida?”, o agente consulta `metricas_financeiras.json`;
- quando o usuário pede uma explicação mais simples ou personalizada, o agente usa `perfil_aluno.json` para ajustar profundidade e linguagem;
- quando o usuário pede um cálculo ou um exemplo prático, o agente utiliza `casos_financeiros.csv`;
- quando a pergunta tem relação com dúvidas recorrentes ou continuidade de aprendizado, o agente aproveita `historico_atendimento.csv`.

Essa abordagem reduz ruído, melhora a precisão das respostas e mantém o agente aderente ao seu escopo educacional.

---

## Exemplo de Contexto Montado

Abaixo está um exemplo simplificado de como os dados podem ser organizados antes de serem enviados ao modelo:

```txt
Perfil do Aluno:
- Nome: João Paulo
- Nível: iniciante
- Objetivos: entender receita, lucro, margem e crescimento percentual
- Dificuldades: porcentagem, interpretação de indicadores e diferença entre caixa e lucro
- Preferência: explicações curtas com exemplos simples

Histórico de Dúvidas:
- Receita x lucro
- Margem bruta e líquida
- Fluxo de caixa
- Percentual de crescimento

Métrica Consultada:
- Nome: Margem Líquida
- Fórmula: (lucro líquido / receita líquida) * 100
- Explicação: mostra quanto da receita realmente virou lucro após todos os custos e despesas
- Erro comum: confundir lucro bruto com lucro líquido

Caso Financeiro:
- Empresa: Loja Alfa
- Receita líquida: R$ 20.000
- Lucro líquido: R$ 3.000

Resposta esperada do agente:
“A margem líquida indica qual percentual da receita virou lucro no fim do período. Neste exemplo, o cálculo é (3000 / 20000) * 100, o que resulta em 15%.”

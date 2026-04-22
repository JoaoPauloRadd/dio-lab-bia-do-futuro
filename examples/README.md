# Exemplos de Uso e Boas Práticas de Prompt

Esta pasta reúne exemplos visuais de execução do **Finn Ancer**, o agente educacional do projeto, com foco em **finanças para iniciantes** e **análise de dados financeiros**.

Os prints abaixo foram usados como evidência prática de comportamento do agente em cenários importantes de validação.

## Boas práticas de prompt

Para obter respostas melhores do Finn Ancer, siga estas orientações:

- Faça perguntas **objetivas e diretas**.
- Quando quiser cálculo, informe os **valores numéricos** com clareza.
- Sempre que possível, indique o **contexto** da dúvida, como empresa, período ou métrica.
- Para aprendizado, peça respostas no formato: **conceito + fórmula + exemplo**.
- Evite pedidos fora do escopo do agente, como clima, entretenimento ou consultas pessoais sem relação com finanças.
- Quando quiser validar comportamento, teste também cenários de **segurança**, **escopo** e **ausência de dados**.

## Exemplos disponíveis

### 1. Precisão / Assertividade
Exemplo de resposta do agente para a pergunta sobre diferença entre receita e lucro:

- [precisao.jpeg](./precisao.jpeg)

### 2. Coerência
Exemplo de resposta com cálculo de lucro líquido e margem líquida a partir de valores fornecidos no prompt:

- [coerência.jpeg](./coer%C3%AAncia.jpeg)

### 3. Fora do escopo
Exemplo de recusa adequada para uma pergunta que não pertence ao domínio do agente:

- [escopo.jpeg](./escopo.jpeg)

### 4. Segurança
Exemplo de resposta segura diante de uma solicitação de dados bancários de terceiros:

- [seguranca.jpeg](./seguranca.jpeg)

## Observação

Esses exemplos ajudam a demonstrar que o Finn Ancer foi configurado para responder de forma:

- didática,
- coerente,
- segura,
- aderente ao escopo definido no projeto.

Eles também servem como referência para futuras melhorias no prompt, na base de conhecimento e na avaliação do agente.

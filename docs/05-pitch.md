# Pitch da Solução

## 1. O Problema

A área de dados é uma porta de entrada para muitos profissionais de tecnologia, mas existe uma dificuldade comum quando esses desenvolvedores começam a atuar em contextos financeiros: eles dominam lógica, estrutura de dados e programação, mas nem sempre dominam os conceitos básicos de finanças usados no dia a dia de empresas e análises.

Na prática, isso gera barreiras logo no início da jornada. Termos como receita, lucro, margem, fluxo de caixa, ticket médio e liquidez aparecem o tempo todo em dashboards, relatórios e análises, mas podem causar confusão para quem ainda está migrando para esse universo. E como finanças é uma das áreas mais presentes e requisitadas dentro de negócios, aprender esses fundamentos se torna uma necessidade real para quem quer trabalhar melhor com dados.

O problema, portanto, não é apenas acessar informação, mas transformar conceitos financeiros em aprendizado claro, aplicável e acessível para iniciantes com perfil técnico.

---

## 2. A Solução

A solução desenvolvida foi o **Finn Ancer**, um agente de IA criado para atuar como tutor de análise financeira para iniciantes.

Em vez de funcionar como um recomendador de investimentos, o Finn foi projetado com foco educacional. Ele ensina conceitos, explica métricas financeiras, mostra fórmulas, diferencia termos parecidos e usa exemplos simples para facilitar o entendimento. Seu papel é ajudar o usuário a aprender, não decidir por ele.

A construção da solução foi organizada com uma base de conhecimento simples e objetiva, usando arquivos estruturados em CSV e JSON:

- `historico_atendimento.csv` para registrar dúvidas recorrentes;
- `perfil_aluno.json` para representar o nível e os objetivos de quem está aprendendo;
- `metricas_financeiras.json` para servir como base conceitual de KPIs, fórmulas, interpretações e exemplos;
- `transacoes.csv` para oferecer casos práticos com dados financeiros fictícios.

Além disso, o comportamento do agente foi guiado por um system prompt específico, definindo seu nome, seu papel, seu tom de voz, suas limitações e suas regras de segurança. Assim, o Finn responde com linguagem acessível, evita recomendações financeiras, não fornece dados sensíveis e admite quando uma informação não está disponível.

---

## 3. Demonstração

A demonstração da solução foi feita por meio de testes práticos com perguntas alinhadas ao objetivo do agente.

Em um dos testes, o usuário perguntou **“Qual a diferença entre receita e lucro?”**. O Finn respondeu corretamente, explicando que receita representa o valor total gerado antes dos custos e que lucro é o valor restante após custos e despesas. Além disso, a resposta trouxe exemplo prático, reforço conceitual e linguagem acessível, mostrando boa assertividade didática.

Também foram realizados testes adicionais para validar comportamento em cenários importantes:

- **Segurança:** ao receber um pedido de dados bancários de um cliente, o agente recusou corretamente e reforçou seu papel educacional;
- **Coerência:** ao receber um caso com receita, custos e despesas, calculou corretamente lucro líquido e margem líquida;
- **Fora do escopo:** ao ser perguntado sobre previsão do tempo, informou corretamente que seu foco é análise financeira;
- **Informação inexistente:** ao ser questionado sobre um dado não presente na base, reconheceu a ausência da informação e ofereceu ajuda com o método de cálculo.

Esses testes mostram que o Finn não apenas responde, mas responde de forma coerente com a proposta do projeto: ensinar finanças de forma simples, segura e contextualizada.

---

## 4. Diferencial e Impacto

O principal diferencial do Finn Ancer está no seu foco. Em vez de tentar ser um agente genérico de finanças, ele foi desenhado para resolver um problema muito específico: ajudar iniciantes, especialmente pessoas com base técnica, a entrar no universo da análise financeira com mais clareza e menos fricção.

Isso gera impacto em dois níveis.

No nível individual, o agente reduz a barreira de entrada para quem quer aprender conceitos financeiros e aplicá-los em análise de dados, relatórios e indicadores de negócio. Ele transforma termos que antes pareciam complexos em explicações diretas e utilizáveis.

No nível profissional, a solução ajuda a aproximar duas áreas extremamente conectadas no mercado atual: tecnologia e finanças. Em um cenário onde empresas precisam cada vez mais de profissionais capazes de interpretar dados com visão de negócio, um agente como o Finn funciona como apoio de aprendizagem contínua e acessível.

Por isso, o Finn Ancer se destaca como uma solução simples, viável e útil: ele não promete substituir um especialista, mas cumpre muito bem o papel de ensinar a base necessária para que mais pessoas consigam evoluir com confiança em contextos financeiros orientados por dados.

---

## 5. Possíveis Melhorias

A solução proposta já atende bem ao objetivo educacional do projeto, mas pode evoluir em diferentes frentes.

Uma melhoria importante seria o uso de modelos mais modernos e mais capazes, com melhor raciocínio, maior precisão conceitual e respostas mais naturais. Em ambiente local, isso normalmente exige mais processamento, mais memória e uma máquina mais robusta, o que pode limitar a adoção em computadores pessoais. Como alternativa, também seria possível integrar APIs de modelos mais avançados, como os da OpenAI ou da Anthropic Claude, ampliando a qualidade das respostas e a velocidade de evolução da solução.

Outra evolução possível está na base de conhecimento. Para uso mais individualizado, os arquivos atuais podem ser expandidos ou adaptados com novos contextos, novos perfis de aluno, mais métricas, mais exemplos práticos e bases mais próximas da realidade de cada usuário. Isso permitiria que o agente deixasse de ser apenas um tutor genérico e passasse a oferecer uma experiência ainda mais personalizada de aprendizagem em finanças e análise de dados financeiros.

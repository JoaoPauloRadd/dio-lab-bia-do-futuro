import json
from pathlib import Path

import pandas as pd
import requests
import streamlit as st

# ============ CONFIGURAÇÃO ============
OLLAMA_URL = "http://localhost:11434/api/generate"
MODELO = "qwen3-vl:4b"
BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "../data"


# ============ CARREGAR DADOS ============
@st.cache_data
def carregar_dados():
    with open(DATA_DIR / "perfil_aluno.json", "r", encoding="utf-8") as f:
        perfil_aluno = json.load(f)

    transacoes = pd.read_csv(DATA_DIR / "transacoes.csv")
    historico = pd.read_csv(DATA_DIR / "historico_atendimento.csv")

    with open(DATA_DIR / "metricas_financeiras.json", "r", encoding="utf-8") as f:
        metricas_financeiras = json.load(f)

    return perfil_aluno, transacoes, historico, metricas_financeiras


perfil_aluno, transacoes, historico, metricas_financeiras = carregar_dados()


# ============ HELPERS ============
def lista_para_texto(valor, padrao="Não informado"):
    if isinstance(valor, list):
        return ", ".join(str(item) for item in valor) if valor else padrao
    if valor in (None, "", []):
        return padrao
    return str(valor)


ndef = None

def selecionar_metricas(pergunta, metricas, limite=5):
    termos = set(str(pergunta).lower().replace("?", " ").replace(",", " ").split())
    selecionadas = []

    for metrica in metricas:
        texto_busca = " ".join(
            [
                str(metrica.get("metrica", "")),
                str(metrica.get("categoria", "")),
                str(metrica.get("explicacao_simples", "")),
                str(metrica.get("formula", "")),
                " ".join(metrica.get("palavras_chave", [])) if isinstance(metrica.get("palavras_chave"), list) else str(metrica.get("palavras_chave", "")),
            ]
        ).lower()

        score = sum(1 for termo in termos if termo and termo in texto_busca)
        if score > 0:
            selecionadas.append((score, metrica))

    if selecionadas:
        selecionadas.sort(key=lambda item: item[0], reverse=True)
        return [item[1] for item in selecionadas[:limite]]

    return metricas[:limite]



def resumir_metricas(metricas):
    linhas = []
    for metrica in metricas:
        linhas.append(
            "\n".join(
                [
                    f"- Métrica: {metrica.get('metrica', 'Não informada')}",
                    f"  Categoria: {metrica.get('categoria', 'Não informada')}",
                    f"  Fórmula: {metrica.get('formula', 'Não informada')}",
                    f"  Explicação: {metrica.get('explicacao_simples', 'Não informada')}",
                    f"  Erro comum: {metrica.get('erro_comum', 'Não informado')}",
                    f"  Exemplo: {metrica.get('exemplo', 'Não informado')}",
                ]
            )
        )
    return "\n\n".join(linhas)



def montar_contexto(pergunta):
    perfil_texto = f"""
ALUNO: {perfil_aluno.get('nome', 'Não informado')}
NÍVEL: {perfil_aluno.get('nivel', 'Não informado')}
OBJETIVOS DE APRENDIZADO: {lista_para_texto(perfil_aluno.get('objetivos_aprendizado'))}
DIFICULDADES: {lista_para_texto(perfil_aluno.get('dificuldades'))}
FORMATO PREFERIDO: {perfil_aluno.get('formato_preferido', 'Não informado')}
ÚLTIMO TEMA ESTUDADO: {perfil_aluno.get('ultimo_tema_estudado', 'Não informado')}
CONTEXTO: {perfil_aluno.get('contexto', 'Não informado')}
""".strip()

    historico_texto = historico.tail(8).to_string(index=False)
    transacoes_texto = transacoes.tail(10).to_string(index=False)
    metricas_relevantes = selecionar_metricas(pergunta, metricas_financeiras)
    metricas_texto = resumir_metricas(metricas_relevantes)

    return f"""
PERFIL DO ALUNO:
{perfil_texto}

HISTÓRICO DE DÚVIDAS E ATENDIMENTOS:
{historico_texto}

EXEMPLOS DE DADOS FINANCEIROS:
{transacoes_texto}

MÉTRICAS FINANCEIRAS RELEVANTES:
{metricas_texto}
""".strip()


# ============ SYSTEM PROMPT ============
SYSTEM_PROMPT = """Você é Finn Ancer, um tutor de análise financeira educativo, paciente e direto.

OBJETIVO:
Ajudar pessoas iniciantes a aprender finanças, métricas financeiras e cálculos básicos usados em análise de dados financeiros, sempre com linguagem acessível, exemplos práticos e foco didático.

CONTEXTO DISPONÍVEL:
Você pode receber informações vindas dos arquivos da base de conhecimento do projeto, como:
- historico_atendimento.csv
- transacoes.csv
- perfil_aluno.json
- metricas_financeiras.json

Use esses dados apenas quando forem realmente úteis para responder à pergunta do usuário.

REGRAS:
1. Sempre responda com foco educacional.
2. Explique conceitos de forma simples, como se estivesse ensinando uma pessoa iniciante.
3. Quando possível, use exemplos práticos com os dados fornecidos.
4. Nunca invente números, métricas, resultados ou fatos que não estejam nos dados recebidos.
5. Se a informação não estiver disponível, admita claramente. Exemplo: 'Não tenho esse dado específico, mas posso te explicar como isso funciona.'
6. Nunca faça recomendações de investimento, compra de ativos ou decisões financeiras personalizadas.
7. Nunca forneça dados sensíveis, sigilosos ou informações de terceiros.
8. Se a pergunta estiver fora do escopo de finanças, métricas, cálculos, orçamento ou análise de dados financeiros, lembre educadamente qual é o seu papel.
9. Sempre que explicar uma métrica, priorize esta sequência:
   - o que é
   - fórmula
   - como interpretar
   - exemplo simples
10. Sempre que houver risco de confusão conceitual, destaque diferenças importantes, como:
   - receita x lucro
   - caixa x lucro
   - custo x despesa
   - margem bruta x margem líquida
11. Responda de forma clara e curta, preferencialmente em até 3 parágrafos.
12. Ao final, quando fizer sentido, pergunte se o usuário quer ver outro exemplo ou um cálculo prático.

ESTILO DE RESPOSTA:
- Tom formal, acessível, prático e direto
- Sem jargão desnecessário
- Sem julgamentos sobre o nível de conhecimento do usuário
- Didático e objetivo"""


# ============ CHAMAR OLLAMA ============
def perguntar(msg):
    contexto = montar_contexto(msg)
    prompt = f"""
{SYSTEM_PROMPT}

CONTEXTO DO ALUNO:
{contexto}

PERGUNTA DO USUÁRIO:
{msg}
"""

    try:
        resposta = requests.post(
            OLLAMA_URL,
            json={"model": MODELO, "prompt": prompt, "stream": False},
            timeout=1200,
        )
        resposta.raise_for_status()
        dados = resposta.json()
        return dados.get("response", "Não consegui gerar uma resposta no momento.")
    except requests.RequestException as e:
        return f"Erro ao consultar o modelo local: {e}"
    except ValueError:
        return "Erro ao interpretar a resposta do modelo."


# ============ INTERFACE ============
st.set_page_config(page_title="Finn Ancer", page_icon="📊")
st.title("📊 Finn Ancer, Tutor de Análise Financeira")
st.caption("Tire dúvidas sobre métricas, conceitos e cálculos financeiros para iniciantes.")

if pergunta_usuario := st.chat_input("Digite sua dúvida sobre finanças e análise de dados financeiros..."):
    st.chat_message("user").write(pergunta_usuario)
    with st.spinner("Pensando..."):
        resposta = perguntar(pergunta_usuario)
    st.chat_message("assistant").write(resposta)

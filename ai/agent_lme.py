import os

from openai import OpenAI
import streamlit as st


def chatGPT(pergunta,ultima, variacao_30, media_3m, df):
    palavras_lme = [
    "alumínio",
    "aluminio",
    "lme",
    "cotação",
    "cotacao",
    "preço",
    "preco",
    "mercado",
    "metal",
    "tendência",
    "tendencia",
    "media",
    "média",
    "histórico",
    "historico",
    "subiu",
    "caiu",
    "aumentou",
    "reduziu",
    "queda",
    "alta"
    ]


    pergunta_lower = pergunta.lower()


    if not any(
        palavra in pergunta_lower
        for palavra in palavras_lme
    ):

        st.warning(
            """
            Sou um analista especializado em commodities LME (aluminio).

            Pergunte sobre:
            - cotação
            - histórico
            - tendência
            - médias
            - preços de metais
            """
        )


    else:
        client = OpenAI(
            api_key=os.getenv("OPENAI_API_KEY")
        )


        contexto = f"""

        Você é um analista especializado no mercado London Metal Exchange (LME).

        Analise somente usando os dados fornecidos.

        Dados atuais:

        Produto:
        Alumínio LME

        Última cotação:
        {ultima.valor:.2f} USD

        Data da última cotação:
        {ultima.data_referencia.strftime("%d/%m/%Y")}

        Variação aproximada últimos 30 dias:
        {variacao_30:.2f}%

        Média últimos 3 meses:
        {media_3m:.2f} USD

        Máxima histórica:
        {df.valor.max():.2f} USD

        Mínima histórica:
        {df.valor.min():.2f} USD


        Regras:

        - Responda somente sobre LME e metais.
        - Explique os indicadores.
        - Não invente dados que não estão disponíveis.
        - Seja objetivo.
        """

        try:
            response = client.responses.create(
                model="gpt-4o-mini",
                input=f"""
            {contexto}

            Pergunta do usuário:
            {pergunta}
            """
                )
        except:
            return "Desculpe, parece que este serviço está fora de ar no momento. Contacte o administrador do sistema."


        return response.output_text
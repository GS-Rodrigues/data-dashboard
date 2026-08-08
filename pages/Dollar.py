import os
import pandas as pd
import plotly.express as px
import streamlit as st
from database.queries import get_dollar
from ai.agent import chatGPT_Dollar

# ==========================
# Configuração da página
# ==========================

st.set_page_config(
    page_title="BRL | Cotação Cambio Dolar-Real",
    page_icon="💵",
    layout="wide"
)

st.title("💵 BRL | Cotação Cambio Dolar-Real")


# ==========================
# Carrega dados
# ==========================

df = get_dollar()

df["data_referencia"] = pd.to_datetime(df["data_referencia"])

df = df.sort_values("data_referencia")


# ==========================
# Cards principais
# ==========================

ultima = df.iloc[-1]

maior = df["valor_compra"].max()
menor = df["valor_compra"].min()



# Variação 12 meses
data_inicio_12m = (
    df["data_referencia"].max()
    - pd.DateOffset(months=12)
)

df36_temp = df[
    df["data_referencia"] >= data_inicio_12m
]

variacao_12m = (
    (df36_temp.iloc[-1]["valor_compra"] - df36_temp.iloc[0]["valor_compra"])
    /
    df36_temp.iloc[0]["valor_compra"]
) * 100


col1, col2, col3, col4 = st.columns(4)


col1.metric(
    "Última cotação",
    f"{ultima.valor_compra:.2f} BRL"
)


col2.metric(
    "Variação 12 meses",
    f"{variacao_12m:.2f}%"
)


col3.metric(
    "Máxima histórica",
    f"{maior:.2f} BRL"
)


col4.metric(
    "Mínima histórica",
    f"{menor:.2f} BRL"
)

# ==========================
# Dados
# ==========================


df["data_referencia"] = pd.to_datetime(
    df["data_referencia"]
)

df = df.sort_values(
    "data_referencia"
)

# ==========================
# Carrega dados Dollar
# ==========================

df["data_referencia"] = (
    df["data_referencia"]
    .astype("datetime64[ns]")
)

df = df.sort_values(
    "data_referencia"
)


ultima = df.iloc[-1]


# Variação aproximada 30 dias úteis

if len(df) >= 22:

    valor_30_dias = df.iloc[-22]["valor_compra"]

    variacao_30 = (
        (ultima.valor_compra - valor_30_dias)
        /
        valor_30_dias
    ) * 100

else:

    variacao_30 = 0


# Média últimos 3 meses

data_3_meses = (
    ultima.data_referencia
    -
    pd.DateOffset(months=3)
)

df_3m = df[
    df.data_referencia >= data_3_meses
]


media_3m = df_3m.valor_compra.mean()

# ==========================
# Agente
# ==========================

st.divider()

st.subheader(
    "🤖 Agente Online - Guilherme"
)


pergunta = st.text_input(
    "Olá, como posso lhe ajudar hoje?",
    placeholder="Ex: Como está a tendência do dolar?",
    max_chars=150
)


enviar = st.button(
    "Consultar"
)

if enviar and pergunta:

    resposta = chatGPT_Dollar(
        pergunta,
        ultima,
        variacao_30,
        media_3m,
        df
    )

    st.success(f"Análise: {resposta}")

# ==========================
# Últimos 12 meses
# ==========================

st.subheader("📈 Histórico dos últimos 3 anos")

data_limite = (
    df["data_referencia"].max()
    - pd.DateOffset(months=36)
)

df36 = df[df["data_referencia"] >= data_limite]

fig = px.line(
    df36,
    x="data_referencia",
    y="valor_compra",
    markers=True
)

fig.update_layout(
    hovermode="x unified",
    xaxis_title="Data",
    yaxis_title="BRL",
    xaxis=dict(
        rangeselector=dict(
            buttons=[
                dict(count=1, label="1M", step="month", stepmode="backward"),
                dict(count=3, label="3M", step="month", stepmode="backward"),
                dict(count=6, label="6M", step="month", stepmode="backward"),
                dict(count=1, label="1A", step="year", stepmode="backward"),
                dict(step="all", label="Tudo"),
            ]
        ),
        rangeslider=dict(
            visible=True
        ),
        type="date"
    )
)

st.plotly_chart(
    fig,
    use_container_width=True
)


# ==========================
# Média trimestral
# ==========================

st.subheader("📊 Média trimestral")


def definir_trimestre(data):

    mes = data.month

    if mes in [1, 2, 3]:
        return 1

    elif mes in [4, 5, 6]:
        return 2

    elif mes in [7, 8, 9]:
        return 3

    else:
        return 4


nome_trimestre = {
    1: "Jan-Mar",
    2: "Abr-Jun",
    3: "Jul-Set",
    4: "Out-Dez"
}


# Cria ano e trimestre
df["ano"] = df["data_referencia"].dt.year
df["trimestre"] = df["data_referencia"].apply(definir_trimestre)


# Calcula média
media_tri = (
    df
    .groupby(["ano", "trimestre"], as_index=False)["valor_compra"]
    .mean()
)


# Nome amigável
media_tri["Periodo"] = (
    media_tri["ano"].astype(str)
    + " - "
    + media_tri["trimestre"].map(nome_trimestre)
)


# Ordenação correta
media_tri = media_tri.sort_values(
    ["ano", "trimestre"]
)


fig2 = px.bar(
    media_tri,
    x="Periodo",
    y="valor_compra",
    text_auto=".1f"
)

fig2.update_layout(
    xaxis_title="Período",
    yaxis_title="Média BRL",
    xaxis_tickangle=-45,

    xaxis=dict(
        rangeselector=dict(
            buttons=[
                dict(count=4, label="4 Trim.", step="all"),
                dict(count=8, label="8 Trim.", step="all"),
                dict(step="all", label="Tudo")
            ]
        ),
        rangeslider=dict(
            visible=True
        )
    )
)

st.plotly_chart(
    fig2,
    use_container_width=True
)


# Mostrar tabela da média trimestral
with st.expander("📋 Ver médias trimestrais"):

    st.dataframe(
        media_tri[
            ["Periodo", "valor_compra"]
        ],
        use_container_width=True
    )


# ==========================
# Tendência
# ==========================

st.subheader("📉 Tendência do mercado")

if len(df) >= 22:

    ultimo = df.iloc[-1]["valor_compra"]

    anterior = df.iloc[-22]["valor_compra"]

    variacao = variacao_30

    st.metric(
        label="Variação aproximada dos últimos 30 dias",
        value=f"{ultimo:.2f} BRL",
        delta=f"{variacao:.2f}%"
    )

    if variacao > 5:

        st.success(
            "📈 Tendência de alta nos últimos 30 dias."
        )

    elif variacao < -5:

        st.error(
            "📉 Tendência de queda nos últimos 30 dias."
        )

    else:

        st.info(
            "➡️ Mercado relativamente estável nos últimos 30 dias."
        )

else:

    st.warning(
        "Ainda não existem dados suficientes para análise."
    )


# ==========================
# Tendência com médias móveis
# ==========================



df_tendencia = df.copy()

df_tendencia["MM30"] = (
    df_tendencia["valor_compra"]
    .rolling(30)
    .mean()
)

df_tendencia["MM90"] = (
    df_tendencia["valor_compra"]
    .rolling(90)
    .mean()
)


fig_mm = px.line(
    df_tendencia,
    x="data_referencia",
    y=[
        "valor_compra",
        "MM30",
        "MM90"
    ],
    title="Preço e médias móveis"
)


fig_mm.update_layout(
    hovermode="x unified",
    xaxis_title="Data",
    yaxis_title="BRL",

    xaxis=dict(
        type="date",

        rangeselector=dict(
            buttons=[
                dict(
                    count=3,
                    label="3M",
                    step="month",
                    stepmode="backward"
                ),
                dict(
                    count=6,
                    label="6M",
                    step="month",
                    stepmode="backward"
                ),
                dict(
                    count=1,
                    label="1A",
                    step="year",
                    stepmode="backward"
                ),
                dict(
                    count=3,
                    label="3A",
                    step="year",
                    stepmode="backward"
                ),
                dict(
                    step="all",
                    label="Tudo"
                )
            ]
        ),

        rangeslider=dict(
            visible=True,
            thickness=0.08
        )
    )
)


st.plotly_chart(
    fig_mm,
    use_container_width=True
)

# ==========================
# Dados completos
# ==========================

with st.expander("📋 Visualizar tabela completa"):

    st.dataframe(
        df,
        use_container_width=True
    )
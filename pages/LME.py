import streamlit as st

from database.queries import get_lme

df = get_lme()

st.title("📈 London Metal Exchange")

ultima = df.iloc[-1]

st.metric(
    label="Último valor",
    value=f"{ultima.valor:.2f} USD"
)

st.line_chart(
    df,
    x="data_referencia",
    y="valor"
)

st.dataframe(df)
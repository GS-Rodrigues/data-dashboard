import streamlit as st

st.set_page_config(
    page_title="Data Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Data Dashboard")

st.write("""
Bem-vindo ao meu dashboard de projetos de Engenharia de Dados.

Cada página apresenta um pipeline diferente,
com coleta automática, tratamento dos dados
e armazenamento em PostgreSQL.
""")

st.divider()

col1, col2 = st.columns(2)

with col1:
    st.info("📈 LME")

with col2:
    st.info("💱 Novos projetos em breve")
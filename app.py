import streamlit as st


# =========================
# CONFIGURAÇÃO
# =========================

st.set_page_config(
    page_title="Data Dashboard | Guilherme Rodrigues",
    page_icon="📊",
    layout="wide"
)


# =========================
# CSS
# =========================

st.markdown("""
<style>
.block-container {
    padding-top: 3rem;
    padding-bottom: 2rem;
    max-width: 1200px;
}

.hero-title {
    font-size: 3rem;
    font-weight: 700;
    margin-bottom: 0.3rem;
}

.hero-subtitle {
    font-size: 1.2rem;
    color: #8b949e;
    margin-bottom: 1rem;
}

.hero-description {
    color: #c9d1d9;
    font-size: 1rem;
    max-width: 750px;
    line-height: 1.6;
}

.section-title {
    font-size: 1.5rem;
    font-weight: 600;
    margin-top: 1rem;
    margin-bottom: 1rem;
}

</style>
""", unsafe_allow_html=True)


# =========================
# HERO
# =========================

st.markdown(
    '<div class="hero-title">📊 Data Dashboard</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="hero-subtitle">'
    'Engenharia de Dados • Web Scraping • ETL • Analytics'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="hero-description">'
    'Projetos desenvolvidos para coletar, processar, armazenar '
    'e visualizar dados de mercado de forma automatizada.'
    '</div>',
    unsafe_allow_html=True
)


st.divider()


# =========================
# PROJETOS
# =========================

st.markdown(
    '<div class="section-title">🚀 Projetos</div>',
    unsafe_allow_html=True
)


col1, col2 = st.columns(2)


# ---------- LME ----------

with col1:

    with st.container(border=True):

        st.subheader("🏭 LME")

        st.caption("Aluminum Market Monitor")

        st.write(
            "Pipeline para coleta, tratamento e análise de dados "
            "do mercado europeu de alumínio (LME)."
        )

        st.markdown(
            "**Tecnologias:** "
            "`Python` `Web Scraping` `PostgreSQL` `ETL`"
        )

        st.write("")

        if st.button(
            "📈 Acessar Dashboard",
            width="stretch",
            key="lme"
        ):
            st.switch_page("pages/LME.py")


# ---------- CÂMBIO ----------

with col2:

    with st.container(border=True):

        st.subheader("💱 Câmbio")

        st.caption("Currency Monitor")

        st.write(
            "Pipeline para coleta e processamento de dados "
            "de câmbio, com armazenamento estruturado."
        )

        st.markdown(
            "**Tecnologias:** "
            "`Python` `Web Scraping` `SQL` `Automation`"
        )

        st.write("")

        if st.button(
            "💵 Acessar Dashboard",
            width="stretch",
            key="dollar"
        ):
            st.switch_page("pages/Dollar.py")


# =========================
# STACK
# =========================

st.markdown(
    '<div class="section-title">🛠️ Stack</div>',
    unsafe_allow_html=True
)


col1, col2, col3, col4 = st.columns(4)


with col1:
    st.metric("🐍 Python", "Pipelines")


with col2:
    st.metric("🗄️ PostgreSQL", "Database")


with col3:
    st.metric("⚙️ GitHub Actions", "Automation")


with col4:
    st.metric("📊 Streamlit", "Dashboard")


# =========================
# FLUXO
# =========================

st.markdown(
    '<div class="section-title">🔄 Data Pipeline</div>',
    unsafe_allow_html=True
)

st.code(
    """Fonte
  ↓
Web Scraping
  ↓
Tratamento
  ↓
PostgreSQL
  ↓
Dashboard""",
    language="text"
)


# =========================
# FOOTER
# =========================

st.divider()

st.caption(
    "Desenvolvido por Guilherme Rodrigues • "
    "Ciência da Computação — UNICAMP"
)
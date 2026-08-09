import streamlit as st


# Configuração
st.set_page_config(
    page_title="Data Dashboard | Guilherme Rodrigues",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)


# CSS
st.markdown("""
<style>

    /* Remove espaçamento superior padrão */
    .block-container {
        padding-top: 3rem;
        padding-bottom: 3rem;
    }

    /* Título principal */
    .hero-title {
        font-size: 3.2rem;
        font-weight: 700;
        margin-bottom: 0.3rem;
    }

    .hero-subtitle {
        font-size: 1.25rem;
        color: #8b949e;
        margin-bottom: 2rem;
    }

    /* Cards */
    .project-card {
        padding: 1.5rem;
        border: 1px solid #30363d;
        border-radius: 12px;
        background-color: #161b22;
        min-height: 190px;
        transition: 0.2s;
    }

    .project-card:hover {
        border-color: #58a6ff;
        transform: translateY(-2px);
    }

    .project-title {
        font-size: 1.4rem;
        font-weight: 600;
        margin-bottom: 0.7rem;
    }

    .project-description {
        color: #8b949e;
        font-size: 0.95rem;
        line-height: 1.5;
    }

    /* Tags */
    .tag {
        display: inline-block;
        padding: 0.3rem 0.65rem;
        margin: 0.2rem 0.2rem 0 0;
        border-radius: 20px;
        background-color: #21262d;
        color: #c9d1d9;
        font-size: 0.8rem;
    }

    /* Seções */
    .section-title {
        font-size: 1.5rem;
        font-weight: 600;
        margin-top: 2rem;
        margin-bottom: 1rem;
    }

    /* Footer */
    .footer {
        text-align: center;
        color: #8b949e;
        margin-top: 4rem;
        font-size: 0.85rem;
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
    'Projetos de Engenharia de Dados • Web Scraping • ETL • Analytics'
    '</div>',
    unsafe_allow_html=True
)

st.write(
    "Um conjunto de projetos voltados à coleta, tratamento, "
    "armazenamento e visualização de dados de mercado."
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


with col1:

    st.markdown("""
    <div class="project-card">

        <div class="project-title">
            🏭 LME — Aluminum Market
        </div>

        <div class="project-description">
            Pipeline para coleta, tratamento e armazenamento
            de dados do mercado europeu de alumínio (LME).
        </div>

        <br>

        <span class="tag">Python</span>
        <span class="tag">Web Scraping</span>
        <span class="tag">PostgreSQL</span>
        <span class="tag">ETL</span>

    </div>
    """, unsafe_allow_html=True)

    st.write("")

    if st.button("📈 Acessar Dashboard LME", use_container_width=True):
        st.switch_page("pages/lme.py")


with col2:

    st.markdown("""
    <div class="project-card">

        <div class="project-title">
            💱 Currency Monitor
        </div>

        <div class="project-description">
            Pipeline para coleta e processamento de dados
            de câmbio, integrado ao sistema de armazenamento.
        </div>

        <br>

        <span class="tag">Python</span>
        <span class="tag">Web Scraping</span>
        <span class="tag">SQL</span>
        <span class="tag">Automation</span>

    </div>
    """, unsafe_allow_html=True)


# =========================
# TECNOLOGIAS
# =========================

st.markdown(
    '<div class="section-title">🛠️ Tecnologias</div>',
    unsafe_allow_html=True
)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("🐍 Python", "Data")

with col2:
    st.metric("🗄️ PostgreSQL", "Database")

with col3:
    st.metric("⚙️ ETL", "Pipelines")

with col4:
    st.metric("📊 Streamlit", "Dashboard")


# =========================
# ARQUITETURA
# =========================

st.markdown(
    '<div class="section-title">🔄 Pipeline</div>',
    unsafe_allow_html=True
)

st.code(
"""
Fonte
  ↓
Web Scraping
  ↓
Tratamento
  ↓
PostgreSQL
  ↓
Dashboard
""",
language="text"
)


# =========================
# FOOTER
# =========================

st.markdown(
    """
    <div class="footer">
        Desenvolvido por <b>Guilherme Rodrigues</b> ·
        Ciência da Computação — UNICAMP
    </div>
    """,
    unsafe_allow_html=True
)
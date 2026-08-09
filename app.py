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

    .hero {
        padding: 1rem 0 2rem 0;
    }

    .hero-title {
        font-size: 3.2rem;
        font-weight: 700;
        line-height: 1.1;
        margin-bottom: 0.5rem;
    }

    .hero-subtitle {
        font-size: 1.2rem;
        color: #8b949e;
        margin-bottom: 1rem;
    }

    .hero-description {
        font-size: 1rem;
        color: #c9d1d9;
        max-width: 750px;
        line-height: 1.6;
    }

    .section-title {
        font-size: 1.5rem;
        font-weight: 600;
        margin: 1.5rem 0 1rem 0;
    }

    .project-card {
        padding: 1.6rem;
        border: 1px solid #30363d;
        border-radius: 14px;
        background: #161b22;
        min-height: 220px;
    }

    .project-icon {
        font-size: 2rem;
        margin-bottom: 0.5rem;
    }

    .project-title {
        font-size: 1.35rem;
        font-weight: 600;
        margin-bottom: 0.2rem;
    }

    .project-subtitle {
        color: #8b949e;
        font-size: 0.9rem;
        margin-bottom: 1rem;
    }

    .project-description {
        color: #c9d1d9;
        font-size: 0.95rem;
        line-height: 1.5;
    }

    .tag {
        display: inline-block;
        padding: 0.25rem 0.6rem;
        margin: 0.25rem 0.2rem 0 0;
        border-radius: 20px;
        background: #21262d;
        color: #c9d1d9;
        font-size: 0.75rem;
    }

    .stack-card {
        text-align: center;
        padding: 1rem;
        border: 1px solid #30363d;
        border-radius: 10px;
        background: #161b22;
    }

    .stack-icon {
        font-size: 1.5rem;
    }

    .stack-name {
        font-weight: 600;
        margin-top: 0.3rem;
    }

    .stack-description {
        color: #8b949e;
        font-size: 0.75rem;
    }

    .footer {
        text-align: center;
        color: #8b949e;
        padding-top: 2.5rem;
        font-size: 0.85rem;
    }

</style>
""", unsafe_allow_html=True)


# =========================
# HERO
# =========================

st.markdown("""
<div class="hero">

    <div class="hero-title">📊 Data Dashboard</div>

    <div class="hero-subtitle">
        Engenharia de Dados • Web Scraping • ETL • Analytics
    </div>

    <div class="hero-description">
        Projetos desenvolvidos para coletar, processar, armazenar
        e visualizar dados de mercado de forma automatizada.
    </div>

</div>
""", unsafe_allow_html=True)


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

        <div class="project-icon">🏭</div>

        <div class="project-title">
            LME
        </div>

        <div class="project-subtitle">
            Aluminum Market Monitor
        </div>

        <div class="project-description">
            Pipeline para coleta, tratamento e análise de dados
            do mercado europeu de alumínio (LME).
        </div>

        <br>

        <span class="tag">Python</span>
        <span class="tag">Web Scraping</span>
        <span class="tag">PostgreSQL</span>
        <span class="tag">ETL</span>

    </div>
    """, unsafe_allow_html=True)

    st.write("")

    if st.button(
        "📈 Acessar Dashboard LME",
        use_container_width=True
    ):
        st.switch_page("pages/lme.py")


with col2:

    st.markdown("""
    <div class="project-card">

        <div class="project-icon">💱</div>

        <div class="project-title">
            Câmbio
        </div>

        <div class="project-subtitle">
            Currency Monitor
        </div>

        <div class="project-description">
            Pipeline para coleta e processamento de dados
            de câmbio, com armazenamento estruturado.
        </div>

        <br>

        <span class="tag">Python</span>
        <span class="tag">Web Scraping</span>
        <span class="tag">SQL</span>
        <span class="tag">Automation</span>

    </div>
    """, unsafe_allow_html=True)

    st.write("")

    st.button(
        "🚧 Em desenvolvimento",
        use_container_width=True,
        disabled=True
    )


# =========================
# STACK
# =========================

st.markdown(
    '<div class="section-title">🛠️ Stack</div>',
    unsafe_allow_html=True
)

col1, col2, col3, col4 = st.columns(4)


with col1:
    st.markdown("""
    <div class="stack-card">
        <div class="stack-icon">🐍</div>
        <div class="stack-name">Python</div>
        <div class="stack-description">Pipelines & ETL</div>
    </div>
    """, unsafe_allow_html=True)


with col2:
    st.markdown("""
    <div class="stack-card">
        <div class="stack-icon">🗄️</div>
        <div class="stack-name">PostgreSQL</div>
        <div class="stack-description">Data Storage</div>
    </div>
    """, unsafe_allow_html=True)


with col3:
    st.markdown("""
    <div class="stack-card">
        <div class="stack-icon">⚙️</div>
        <div class="stack-name">GitHub Actions</div>
        <div class="stack-description">Automation</div>
    </div>
    """, unsafe_allow_html=True)


with col4:
    st.markdown("""
    <div class="stack-card">
        <div class="stack-icon">📊</div>
        <div class="stack-name">Streamlit</div>
        <div class="stack-description">Data Visualization</div>
    </div>
    """, unsafe_allow_html=True)


# =========================
# FLUXO
# =========================

st.markdown(
    '<div class="section-title">🔄 Pipeline</div>',
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

st.markdown("""
<div class="footer">
    Desenvolvido por <b>Guilherme Rodrigues</b><br>
    Ciência da Computação — UNICAMP
</div>
""", unsafe_allow_html=True)
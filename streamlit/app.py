"""
Data Analysis Bootcamp — Interactive Learning Platform
======================================================
Main entry point for the Streamlit multi-page application.
"""

import streamlit as st
import sys, os

# ── Make utils importable from any page ──
sys.path.insert(0, os.path.dirname(__file__))

from utils.styles import inject_custom_css, hero

# ── Page config ──
st.set_page_config(
    page_title="Data Analysis Bootcamp",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

inject_custom_css()

# ── Sidebar branding ──
with st.sidebar:
    st.markdown("## 📊 DA Bootcamp")
    st.caption("Master Data Science Skills")
    st.divider()
    st.markdown(
        "**Modules**\n"
        "- 🔢 NumPy Basics\n"
        "- 🐼 Pandas Essentials\n"
        "- 📈 Data Visualization\n"
        "- 🤖 Scikit-Learn\n"
        "- 🚀 Projects\n"
    )
    st.divider()
    st.caption("Use the sidebar pages ↑ to navigate.")

# ── Hero section ──
hero(
    "📊 Data Analysis Bootcamp",
    "Master NumPy · Pandas · Visualization · Scikit-Learn — step by step, interactively.",
)

# ── Overview metrics ──
st.markdown("""
<div class="metric-row">
    <div class="metric-mini"><div class="value">4</div><div class="label">Modules</div></div>
    <div class="metric-mini"><div class="value">15</div><div class="label">Notebooks</div></div>
    <div class="metric-mini"><div class="value">50+</div><div class="label">Concepts</div></div>
    <div class="metric-mini"><div class="value">∞</div><div class="label">Practice</div></div>
</div>
""", unsafe_allow_html=True)

# ── Module cards ──
st.markdown("### 🗺️ Learning Roadmap")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="module-card">
        <h3>🔢 NumPy Basics</h3>
        <p>Arrays, indexing, slicing, math operations, aggregations, and set operations — the foundation of numerical Python.</p>
        <span class="badge">3 Notebooks · 5 Steps</span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="module-card">
        <h3>📈 Data Visualization</h3>
        <p>Matplotlib plots, time-series resampling, correlation heatmaps, and interactive Plotly charts.</p>
        <span class="badge">3 Notebooks · 3 Steps</span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="module-card">
        <h3>🚀 Projects</h3>
        <p>Apply your skills — data melting, wide-to-long transforms, and real-world plotting challenges.</p>
        <span class="badge">2 Notebooks · 2 Projects</span>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="module-card">
        <h3>🐼 Pandas Essentials</h3>
        <p>DataFrames, missing data, sorting, merging, concatenation, cut/qcut, rolling windows, and pivot tables.</p>
        <span class="badge">7 Notebooks · 6 Steps</span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="module-card">
        <h3>🤖 Scikit-Learn</h3>
        <p>ML pipelines — imputation, encoding, scaling, and logistic regression in one clean workflow.</p>
        <span class="badge">1 Notebook · 3 Steps</span>
    </div>
    """, unsafe_allow_html=True)

# ── Footer ──
st.divider()
st.markdown(
    "<center style='color:#64748b; font-size:0.85rem;'>"
    "Built with ❤️ using Streamlit · Data Analysis Bootcamp"
    "</center>",
    unsafe_allow_html=True,
)

"""Shared CSS styles for the Data Analysis Bootcamp Streamlit app."""

import streamlit as st


def inject_custom_css():
    """Inject global custom CSS for premium look & feel."""
    st.markdown("""
    <style>
    /* ── Import Google Font ── */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    /* ── Hero gradient header ── */
    .hero-container {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2.5rem 2rem;
        border-radius: 16px;
        margin-bottom: 2rem;
        color: white;
        text-align: center;
    }
    .hero-container h1 {
        font-size: 2.4rem;
        font-weight: 800;
        margin-bottom: 0.5rem;
        letter-spacing: -0.5px;
    }
    .hero-container p {
        font-size: 1.1rem;
        opacity: 0.9;
        font-weight: 300;
    }

    /* ── Module cards ── */
    .module-card {
        background: linear-gradient(145deg, #1e1e2e, #2a2a3d);
        border: 1px solid rgba(255,255,255,0.08);
        border-radius: 14px;
        padding: 1.5rem;
        margin-bottom: 1rem;
        transition: transform 0.2s, box-shadow 0.2s;
    }
    .module-card:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 24px rgba(102,126,234,0.25);
    }
    .module-card h3 {
        color: #a78bfa;
        margin-bottom: 0.5rem;
        font-weight: 700;
    }
    .module-card p {
        color: #94a3b8;
        font-size: 0.9rem;
        line-height: 1.5;
    }
    .module-card .badge {
        display: inline-block;
        background: rgba(167,139,250,0.15);
        color: #a78bfa;
        padding: 3px 10px;
        border-radius: 20px;
        font-size: 0.75rem;
        font-weight: 600;
        margin-top: 0.5rem;
    }

    /* ── Step header ── */
    .step-header {
        background: linear-gradient(90deg, rgba(102,126,234,0.12), transparent);
        border-left: 4px solid #667eea;
        padding: 0.8rem 1.2rem;
        border-radius: 0 10px 10px 0;
        margin: 1.5rem 0 1rem 0;
    }
    .step-header h3 {
        margin: 0;
        color: #c4b5fd;
        font-weight: 600;
    }

    /* ── Info cards ── */
    .info-card {
        background: rgba(30,30,46,0.7);
        border: 1px solid rgba(255,255,255,0.06);
        border-radius: 12px;
        padding: 1rem 1.2rem;
        margin: 0.5rem 0;
    }
    .info-card code {
        color: #7dd3fc;
        background: rgba(125,211,252,0.1);
        padding: 2px 6px;
        border-radius: 4px;
    }

    /* ── Data upload banner ── */
    .upload-banner {
        background: linear-gradient(90deg, rgba(34,197,94,0.1), rgba(34,197,94,0.03));
        border: 1px dashed rgba(34,197,94,0.3);
        border-radius: 12px;
        padding: 1rem 1.2rem;
        margin: 1rem 0;
        text-align: center;
    }
    .upload-banner p {
        color: #86efac;
        margin: 0;
        font-size: 0.9rem;
    }

    /* ── Metric mini-cards ── */
    .metric-row {
        display: flex;
        gap: 1rem;
        margin: 1rem 0;
    }
    .metric-mini {
        flex: 1;
        background: rgba(30,30,46,0.8);
        border: 1px solid rgba(255,255,255,0.06);
        border-radius: 12px;
        padding: 1rem;
        text-align: center;
    }
    .metric-mini .value {
        font-size: 1.8rem;
        font-weight: 700;
        color: #a78bfa;
    }
    .metric-mini .label {
        font-size: 0.8rem;
        color: #94a3b8;
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    /* ── Smooth scrollbar ── */
    ::-webkit-scrollbar { width: 6px; }
    ::-webkit-scrollbar-track { background: transparent; }
    ::-webkit-scrollbar-thumb { background: #4a4a6a; border-radius: 3px; }
    </style>
    """, unsafe_allow_html=True)


def step_header(step_num: int, title: str) -> None:
    """Render a styled step header."""
    st.markdown(
        f'<div class="step-header"><h3>Step {step_num} — {title}</h3></div>',
        unsafe_allow_html=True,
    )


def hero(title: str, subtitle: str) -> None:
    """Render a gradient hero banner."""
    st.markdown(
        f'<div class="hero-container"><h1>{title}</h1><p>{subtitle}</p></div>',
        unsafe_allow_html=True,
    )

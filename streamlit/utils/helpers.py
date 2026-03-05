"""Shared helper utilities for the Data Analysis Bootcamp Streamlit app."""

import streamlit as st
import pandas as pd
import io


def show_code(code: str, language: str = "python") -> None:
    """Display a code block with syntax highlighting."""
    st.code(code, language=language)


def show_explanation(text: str) -> None:
    """Render an explanation inside a styled info card."""
    st.markdown(
        f'<div class="info-card">{text}</div>',
        unsafe_allow_html=True,
    )


def data_uploader(
    key: str,
    default_df: pd.DataFrame,
    help_text: str = "Upload a CSV or Excel file to use your own data, or use the built-in default dataset.",
    accepted_types: list | None = None,
) -> pd.DataFrame:
    """
    Show a file uploader with a default dataset fallback.

    Returns the user-uploaded DataFrame if provided, otherwise the default.
    """
    if accepted_types is None:
        accepted_types = ["csv", "xlsx", "xls"]

    st.markdown(
        '<div class="upload-banner">'
        "<p>📂 <strong>Bring Your Own Data</strong> — Upload a CSV / Excel file below, "
        "or continue with the built-in default dataset.</p></div>",
        unsafe_allow_html=True,
    )

    format_hints = {
        "csv": "Comma-separated, UTF-8 encoded",
        "xlsx": "Excel workbook (.xlsx)",
        "xls": "Legacy Excel (.xls)",
    }
    format_str = " · ".join(f"**{k.upper()}**: {v}" for k, v in format_hints.items() if k in accepted_types)

    with st.expander("ℹ️ Supported formats & tips", expanded=False):
        st.markdown(format_str)
        st.markdown(
            "- First row should be **column headers**\n"
            "- Numeric columns work best for math / stats operations\n"
            "- Date columns should be parseable (e.g. `2024-01-15`)"
        )

    uploaded = st.file_uploader(
        help_text,
        type=accepted_types,
        key=key,
        label_visibility="collapsed",
    )

    if uploaded is not None:
        try:
            if uploaded.name.endswith(".csv"):
                df = pd.read_csv(uploaded)
            else:
                df = pd.read_excel(uploaded)
            st.success(f"✅ Loaded **{uploaded.name}** — {len(df)} rows × {len(df.columns)} columns")
            return df
        except Exception as e:
            st.error(f"❌ Failed to parse file: {e}")
            st.info("Falling back to the default dataset.")
            return default_df
    else:
        return default_df


def create_metric_cards(metrics: list[tuple[str, str]]) -> None:
    """
    Render a row of mini metric cards.

    metrics: list of (value, label) tuples.
    """
    cards_html = "".join(
        f'<div class="metric-mini"><div class="value">{val}</div><div class="label">{lbl}</div></div>'
        for val, lbl in metrics
    )
    st.markdown(f'<div class="metric-row">{cards_html}</div>', unsafe_allow_html=True)

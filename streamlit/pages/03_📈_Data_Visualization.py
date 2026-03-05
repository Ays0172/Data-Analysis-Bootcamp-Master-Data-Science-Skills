"""
Module 3 — Data Visualization
===============================
Interactive charts with Matplotlib and Plotly — line, bar, scatter, heatmaps, and time-series.
"""

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("Agg")
import plotly.express as px
import sys, os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from utils.styles import inject_custom_css, hero, step_header
from utils.helpers import show_code, data_uploader

st.set_page_config(page_title="Data Visualization", page_icon="📈", layout="wide")
inject_custom_css()
hero("📈 Data Visualization", "Matplotlib, Plotly heatmaps, time-series resampling & more")


# ═══════════════════════════════════════════════════════
# STEP 1 — Matplotlib Basics
# ═══════════════════════════════════════════════════════
step_header(1, "Matplotlib Chart Gallery")

np.random.seed(42)
default_viz = pd.DataFrame({
    "Month": pd.date_range("2024-01-01", periods=12, freq="MS").strftime("%b"),
    "Revenue": np.random.randint(10000, 50000, 12),
    "Expenses": np.random.randint(8000, 35000, 12),
    "Profit": np.random.randint(2000, 15000, 12),
})

df_viz = data_uploader("viz_upload", default_viz)
st.dataframe(df_viz, use_container_width=True)

num_cols = df_viz.select_dtypes(include=[np.number]).columns.tolist()
all_cols = df_viz.columns.tolist()

c1, c2, c3 = st.columns(3)
chart_type = c1.selectbox("Chart type:", ["Line", "Bar", "Scatter", "Histogram", "Area"], key="chart_type")
x_col = c2.selectbox("X axis:", all_cols, index=0, key="x_col")
y_col = c3.selectbox("Y axis:", num_cols, index=0, key="y_col") if num_cols else None

style = st.selectbox("Matplotlib style:", plt.style.available[:15], index=0, key="mpl_style")

if y_col:
    fig, ax = plt.subplots(figsize=(10, 5))
    with plt.style.context(style):
        fig, ax = plt.subplots(figsize=(10, 5))
        if chart_type == "Line":
            ax.plot(df_viz[x_col], df_viz[y_col], marker="o", linewidth=2, color="#667eea")
            ax.fill_between(range(len(df_viz)), df_viz[y_col], alpha=0.1, color="#667eea")
        elif chart_type == "Bar":
            colors = plt.cm.viridis(np.linspace(0.3, 0.9, len(df_viz)))
            ax.bar(df_viz[x_col], df_viz[y_col], color=colors, edgecolor="white", linewidth=0.5)
        elif chart_type == "Scatter":
            ax.scatter(df_viz[x_col], df_viz[y_col], s=100, c="#764ba2", alpha=0.7, edgecolors="white")
        elif chart_type == "Histogram":
            ax.hist(df_viz[y_col], bins=st.slider("Bins:", 3, 30, 10, key="hist_bins"), color="#667eea", edgecolor="white", alpha=0.8)
        elif chart_type == "Area":
            ax.fill_between(range(len(df_viz)), df_viz[y_col], alpha=0.5, color="#667eea")
            ax.plot(df_viz[y_col].values, color="#764ba2", linewidth=2)

        ax.set_title(f"{chart_type} Chart — {y_col}", fontweight="bold", fontsize=14)
        ax.set_xlabel(x_col)
        ax.set_ylabel(y_col)
        plt.xticks(rotation=45)
        plt.tight_layout()
    st.pyplot(fig)
    plt.close(fig)

    show_code(f"plt.{chart_type.lower()}(df['{x_col}'], df['{y_col}'])\nplt.title('{chart_type} Chart')\nplt.show()")


# ═══════════════════════════════════════════════════════
# STEP 2 — Time Series Resampling
# ═══════════════════════════════════════════════════════
step_header(2, "Time Series Resampling")

np.random.seed(45)
dates = pd.date_range(start="2024-01-01", periods=365)
default_ts = pd.DataFrame({"Date": dates, "Sale": np.random.randint(99, 300, size=365)})

df_ts = data_uploader("ts_upload", default_ts)
if "Date" in df_ts.columns:
    df_ts["Date"] = pd.to_datetime(df_ts["Date"], errors="coerce")
    df_ts = df_ts.dropna(subset=["Date"])
    df_ts.set_index("Date", inplace=True)

ts_num_cols = df_ts.select_dtypes(include=[np.number]).columns.tolist()
if ts_num_cols:
    ts_col = st.selectbox("Column:", ts_num_cols, key="ts_col")

    freq_map = {"Daily (D)": "D", "Weekly (W)": "W", "Monthly (MS)": "MS", "Quarterly (QS)": "QS"}
    freq_label = st.selectbox("Resample frequency:", list(freq_map.keys()), index=2, key="ts_freq")
    freq = freq_map[freq_label]

    agg = st.selectbox("Aggregation:", ["mean", "sum", "max", "min"], key="ts_agg")

    resampled = df_ts[[ts_col]].resample(freq).agg(agg)

    show_code(f"df['{ts_col}'].resample('{freq}').{agg}()")

    fig2 = px.line(resampled, y=ts_col, title=f"{ts_col} — Resampled ({freq_label}, {agg})",
                   template="plotly_dark", color_discrete_sequence=["#a78bfa"])
    fig2.update_layout(font_family="Inter", plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)")
    st.plotly_chart(fig2, use_container_width=True)
else:
    st.warning("No numeric columns found for resampling.")


# ═══════════════════════════════════════════════════════
# STEP 3 — Correlation Heatmap
# ═══════════════════════════════════════════════════════
step_header(3, "Correlation Heatmap")

np.random.seed(42)
default_corr = pd.DataFrame({
    "Math": np.random.randint(40, 100, 50),
    "Science": np.random.randint(40, 100, 50),
    "English": np.random.randint(40, 100, 50),
    "History": np.random.randint(40, 100, 50),
    "Art": np.random.randint(40, 100, 50),
})

df_corr = data_uploader("corr_upload", default_corr)

numeric_df = df_corr.select_dtypes(include=[np.number])
if len(numeric_df.columns) >= 2:
    corr = numeric_df.corr().round(3)

    show_code("df.corr()  # Pearson correlation matrix")

    fig3 = px.imshow(
        corr,
        text_auto=True,
        color_continuous_scale="Viridis",
        title="Correlation Heatmap",
        template="plotly_dark",
    )
    fig3.update_layout(font_family="Inter", plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)")
    st.plotly_chart(fig3, use_container_width=True)
else:
    st.warning("Need at least 2 numeric columns for a correlation heatmap.")

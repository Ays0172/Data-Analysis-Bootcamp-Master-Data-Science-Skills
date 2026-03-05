"""
Module 5 — Projects
=====================
Apply your skills — data melting and interactive plotting.
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

st.set_page_config(page_title="Projects", page_icon="🚀", layout="wide")
inject_custom_css()
hero("🚀 Projects", "Apply what you've learned — real-world data transformations & visualizations")


# ═══════════════════════════════════════════════════════
# PROJECT 1 — Data Melt (Wide → Long)
# ═══════════════════════════════════════════════════════
step_header(1, "Project 1 — Data Melt (Wide → Long Format)")

st.markdown("""
**pd.melt()** unpivots a DataFrame from **wide** format to **long** format.
This is essential for tidy data and plotting libraries that expect long-form data.
""")

default_melt = pd.DataFrame({
    "Product": ["A", "B", "C", "D", "E"],
    "Q1_Sales": [100, 150, 200, 250, 300],
    "Q2_Sales": [110, 160, 210, 260, 310],
    "Q3_Sales": [120, 170, 220, 270, 320],
    "Q4_Sales": [130, 180, 230, 280, 330],
})

df_melt = data_uploader("melt_upload", default_melt)

st.markdown("**Original Data (Wide Format):**")
st.dataframe(df_melt, use_container_width=True)

all_cols = df_melt.columns.tolist()
id_vars = st.multiselect("ID variables (kept as-is):", all_cols, default=[all_cols[0]] if all_cols else [], key="melt_id")
value_vars = st.multiselect("Value variables (melted):", [c for c in all_cols if c not in id_vars],
                            default=[c for c in all_cols if c not in id_vars], key="melt_vals")

var_name = st.text_input("Variable name:", "Quarter", key="melt_var")
value_name = st.text_input("Value name:", "Sales", key="melt_val")

if id_vars and value_vars:
    show_code(f"""pd.melt(df,
    id_vars={id_vars},
    value_vars={value_vars},
    var_name='{var_name}',
    value_name='{value_name}')""")

    melted = pd.melt(df_melt, id_vars=id_vars, value_vars=value_vars, var_name=var_name, value_name=value_name)

    st.markdown("**Melted Data (Long Format):**")
    st.dataframe(melted, use_container_width=True)

    # Bonus: Plot the melted data
    st.markdown("**📊 Visualization of melted data:**")
    if len(id_vars) >= 1:
        fig = px.bar(
            melted,
            x=var_name,
            y=value_name,
            color=id_vars[0],
            barmode="group",
            template="plotly_dark",
            color_discrete_sequence=px.colors.qualitative.Pastel,
            title=f"{value_name} by {var_name}",
        )
        fig.update_layout(font_family="Inter", plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)")
        st.plotly_chart(fig, use_container_width=True)
else:
    st.info("Select at least one ID variable and one value variable.")


# ═══════════════════════════════════════════════════════
# PROJECT 2 — Interactive Plotting Challenge
# ═══════════════════════════════════════════════════════
step_header(2, "Project 2 — Interactive Plotting Challenge")

st.markdown("""
Build your own charts from scratch! Upload data or use the default dataset,
pick columns, and create publication-quality plots.
""")

np.random.seed(10)
default_plot = pd.DataFrame({
    "City": np.random.choice(["New York", "London", "Tokyo", "Berlin", "Sydney"], 100),
    "Temperature": np.random.normal(22, 8, 100).round(1),
    "Humidity": np.random.randint(30, 90, 100),
    "Rainfall_mm": np.random.exponential(20, 100).round(1),
    "Wind_Speed": np.random.uniform(5, 40, 100).round(1),
})

df_plot = data_uploader("plot_upload", default_plot)
st.dataframe(df_plot.head(10), use_container_width=True)

num_cols = df_plot.select_dtypes(include=[np.number]).columns.tolist()
cat_cols = df_plot.select_dtypes(include=["object", "category"]).columns.tolist()

chart_type = st.selectbox(
    "Chart type:",
    ["Scatter Plot", "Box Plot", "Violin Plot", "Histogram", "Strip Plot", "Sunburst"],
    key="proj_chart_type",
)

c1, c2, c3 = st.columns(3)

if chart_type == "Scatter Plot" and len(num_cols) >= 2:
    x = c1.selectbox("X:", num_cols, index=0, key="sc_x")
    y = c2.selectbox("Y:", num_cols, index=1, key="sc_y")
    color = c3.selectbox("Color:", ["None"] + cat_cols + num_cols, key="sc_c")
    color_val = None if color == "None" else color
    fig = px.scatter(df_plot, x=x, y=y, color=color_val, template="plotly_dark",
                     title=f"{y} vs {x}", color_discrete_sequence=px.colors.qualitative.Pastel)

elif chart_type == "Box Plot" and num_cols:
    y = c1.selectbox("Numeric:", num_cols, key="box_y")
    x = c2.selectbox("Group by:", ["None"] + cat_cols, key="box_x")
    x_val = None if x == "None" else x
    fig = px.box(df_plot, x=x_val, y=y, template="plotly_dark", title=f"Box Plot — {y}",
                 color=x_val, color_discrete_sequence=px.colors.qualitative.Pastel)

elif chart_type == "Violin Plot" and num_cols:
    y = c1.selectbox("Numeric:", num_cols, key="vio_y")
    x = c2.selectbox("Group by:", ["None"] + cat_cols, key="vio_x")
    x_val = None if x == "None" else x
    fig = px.violin(df_plot, x=x_val, y=y, template="plotly_dark", title=f"Violin — {y}",
                    color=x_val, box=True, color_discrete_sequence=px.colors.qualitative.Pastel)

elif chart_type == "Histogram" and num_cols:
    col = c1.selectbox("Column:", num_cols, key="hist_col")
    bins = c2.slider("Bins:", 5, 50, 20, key="hist_b")
    fig = px.histogram(df_plot, x=col, nbins=bins, template="plotly_dark",
                       title=f"Histogram — {col}", color_discrete_sequence=["#a78bfa"])

elif chart_type == "Strip Plot" and num_cols:
    y = c1.selectbox("Numeric:", num_cols, key="strip_y")
    x = c2.selectbox("Group by:", ["None"] + cat_cols, key="strip_x")
    x_val = None if x == "None" else x
    fig = px.strip(df_plot, x=x_val, y=y, template="plotly_dark", title=f"Strip — {y}",
                   color=x_val, color_discrete_sequence=px.colors.qualitative.Pastel)

elif chart_type == "Sunburst" and cat_cols and num_cols:
    path_cols = st.multiselect("Hierarchy:", cat_cols, default=cat_cols[:1], key="sun_path")
    val_col = c1.selectbox("Value:", num_cols, key="sun_val")
    if path_cols:
        fig = px.sunburst(df_plot, path=path_cols, values=val_col, template="plotly_dark",
                          title="Sunburst Chart", color_discrete_sequence=px.colors.qualitative.Pastel)
    else:
        fig = None
        st.info("Select at least one hierarchy column.")
else:
    fig = None
    st.warning("Not enough columns for this chart type. Try uploading data with more columns.")

if fig is not None:
    fig.update_layout(font_family="Inter", plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)")
    st.plotly_chart(fig, use_container_width=True)

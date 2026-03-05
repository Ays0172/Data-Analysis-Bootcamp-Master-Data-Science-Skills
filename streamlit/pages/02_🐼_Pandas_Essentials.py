"""
Module 2 — Pandas Essentials
==============================
Interactive exploration of Pandas DataFrames, missing data, sorting, merging, and more.
"""

import streamlit as st
import pandas as pd
import numpy as np
import sys, os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from utils.styles import inject_custom_css, hero, step_header
from utils.helpers import show_code, data_uploader

st.set_page_config(page_title="Pandas Essentials", page_icon="🐼", layout="wide")
inject_custom_css()
hero("🐼 Pandas Essentials", "DataFrames, missing data, sorting, merging, pivoting & more")


# ═══════════════════════════════════════════════════════
# STEP 1 — Handling Missing Data (Dropna)
# ═══════════════════════════════════════════════════════
step_header(1, "Handling Missing Data (dropna)")

default_na = pd.DataFrame({
    "A": [1, 2, 6, 4, 5],
    "B": [np.nan, 2, 3, 4, 5],
    "C": [np.nan, 2, 3, 4, np.nan],
})

df_na = data_uploader("dropna_upload", default_na)

st.markdown("**Original DataFrame:**")
st.dataframe(df_na, use_container_width=True)

c1, c2 = st.columns(2)
axis_opt = c1.radio("Drop along:", ["Rows (axis=0)", "Columns (axis=1)"], key="drop_axis", horizontal=True)
how_opt = c2.radio("How:", ["any", "all"], key="drop_how", horizontal=True)

axis_val = 0 if "0" in axis_opt else 1
subset_cols = None

if axis_val == 0 and len(df_na.columns) > 1:
    subset_cols = st.multiselect(
        "Subset (optional — only check these columns for NaN):",
        df_na.columns.tolist(),
        key="drop_subset",
    )

code_str = f"df.dropna(axis={axis_val}, how='{how_opt}'"
if subset_cols:
    code_str += f", subset={subset_cols}"
code_str += ")"
show_code(code_str)

try:
    if subset_cols:
        result_na = df_na.dropna(axis=axis_val, how=how_opt, subset=subset_cols)
    else:
        result_na = df_na.dropna(axis=axis_val, how=how_opt)
    st.markdown("**Result:**")
    st.dataframe(result_na, use_container_width=True)
    st.info(f"Dropped {len(df_na) - len(result_na)} rows" if axis_val == 0 else f"Dropped {len(df_na.columns) - len(result_na.columns)} columns")
except Exception as e:
    st.error(f"Error: {e}")


# ═══════════════════════════════════════════════════════
# STEP 2 — Sorting Data
# ═══════════════════════════════════════════════════════
step_header(2, "Sorting Data (sort_values)")

default_sort = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Grace", "Hannah", "Ian", "Jack"],
    "Age": np.random.randint(20, 40, size=10),
    "Score": np.random.randint(35, 100, size=10),
    "Country": np.random.choice(["USA", "Canada", "UK", "Germany", "France"], size=10),
    "Salary": np.random.randint(40000, 120000, size=10),
})

df_sort = data_uploader("sort_upload", default_sort)
st.dataframe(df_sort, use_container_width=True)

sort_cols = st.multiselect("Sort by columns:", df_sort.columns.tolist(), default=[df_sort.columns[0]], key="sort_cols")

if sort_cols:
    asc_toggles = []
    cols_asc = st.columns(len(sort_cols))
    for i, col_name in enumerate(sort_cols):
        asc_toggles.append(cols_asc[i].checkbox(f"Ascending ({col_name})", value=True, key=f"asc_{col_name}"))

    sorted_df = df_sort.sort_values(by=sort_cols, ascending=asc_toggles)
    show_code(f"df.sort_values(by={sort_cols}, ascending={asc_toggles})")
    st.dataframe(sorted_df, use_container_width=True)


# ═══════════════════════════════════════════════════════
# STEP 3 — Merge & Concat
# ═══════════════════════════════════════════════════════
step_header(3, "Merge & Concat")

tab_merge, tab_concat = st.tabs(["pd.merge", "pd.concat"])

with tab_merge:
    st.markdown("**Merge two DataFrames on a common key:**")

    df_id = pd.DataFrame({"ID": [1, 2, 3, 4, 5], "Name": ["Alice", "Bob", "Charlie", "David", "Eva"]})
    df_orders = pd.DataFrame({"ID": [1, 2, 3, 4, 5], "Amount": [250, 150, 200, 300, 400], "Order_ID": [101, 102, 103, 104, 105]})

    c1, c2 = st.columns(2)
    c1.markdown("**DataFrame 1:**")
    c1.dataframe(df_id)
    c2.markdown("**DataFrame 2:**")
    c2.dataframe(df_orders)

    merge_how = st.selectbox("Join type:", ["inner", "outer", "left", "right"], key="merge_how")
    show_code(f"pd.merge(df_id, df_orders, on='ID', how='{merge_how}')")
    merged = pd.merge(df_id, df_orders, on="ID", how=merge_how)
    st.dataframe(merged, use_container_width=True)

with tab_concat:
    st.markdown("**Concatenate DataFrames vertically:**")

    df_mar = pd.DataFrame({"Date": ["2024-03-01", "2024-03-02", "2024-03-03"], "Sale": [150, 200, 250]})
    df_apr = pd.DataFrame({"Date": ["2024-04-01", "2024-04-02", "2024-04-03"], "Sale": [180, 220, 270]})

    c1, c2 = st.columns(2)
    c1.markdown("**March Sales:**")
    c1.dataframe(df_mar)
    c2.markdown("**April Sales:**")
    c2.dataframe(df_apr)

    ignore_idx = st.checkbox("Reset index (ignore_index=True)", value=True, key="concat_idx")
    show_code(f"pd.concat([df_mar, df_apr], ignore_index={ignore_idx})")
    concatenated = pd.concat([df_mar, df_apr], ignore_index=ignore_idx)
    st.dataframe(concatenated, use_container_width=True)


# ═══════════════════════════════════════════════════════
# STEP 4 — Cut & Qcut (Customer Segmentation)
# ═══════════════════════════════════════════════════════
step_header(4, "Cut & Qcut — Customer Segmentation")

st.markdown("Segment customers by **age group** (pd.cut) and **spending quartile** (pd.qcut).")

np.random.seed(0)
n = st.slider("Number of customers:", 100, 2000, 500, 100, key="cust_n")
default_seg = pd.DataFrame({
    "Customer": range(1, n + 1),
    "Age": np.random.randint(20, 60, n),
    "Annual_Spend": np.random.uniform(600, 20000, n).round(2),
    "Purchase_Frequency": np.random.poisson(2, n),
})

df_seg = data_uploader("seg_upload", default_seg)

num_age_bins = st.slider("Number of age bins:", 2, 6, 3, key="age_bins")
num_spend_q = st.slider("Number of spending quartiles:", 2, 6, 4, key="spend_q")

age_min, age_max = int(df_seg["Age"].min()) if "Age" in df_seg.columns else 20, int(df_seg["Age"].max()) if "Age" in df_seg.columns else 60
age_bins = np.linspace(age_min, age_max, num_age_bins + 1).astype(int).tolist()
age_labels = [f"Group {i+1}" for i in range(num_age_bins)]

try:
    df_seg["Age_Group"] = pd.cut(df_seg["Age"], bins=age_bins, labels=age_labels, include_lowest=True)
    spend_labels = [f"Q{i+1}" for i in range(num_spend_q)]
    df_seg["Spend_Segment"] = pd.qcut(df_seg["Annual_Spend"], q=num_spend_q, labels=spend_labels)

    show_code(f"pd.cut(df['Age'], bins={age_bins}, labels={age_labels})\npd.qcut(df['Annual_Spend'], q={num_spend_q}, labels={spend_labels})")

    segment_analysis = df_seg.groupby(["Age_Group", "Spend_Segment"], observed=True).agg(
        Count=("Customer", "count"),
        Avg_Spend=("Annual_Spend", "mean"),
        Avg_Frequency=("Purchase_Frequency", "mean"),
    ).reset_index()

    st.dataframe(segment_analysis, use_container_width=True)
except Exception as e:
    st.error(f"Segmentation error: {e}. Make sure your data has 'Age' and 'Annual_Spend' columns.")


# ═══════════════════════════════════════════════════════
# STEP 5 — Rolling Windows
# ═══════════════════════════════════════════════════════
step_header(5, "Rolling Windows — Moving Average & Std")

np.random.seed(45)
dates = pd.date_range(start="2024-01-01", periods=90)
default_roll = pd.DataFrame({"Date": dates, "Sale": np.random.randint(99, 198, size=90)})
default_roll.set_index("Date", inplace=True)

df_roll = data_uploader("roll_upload", default_roll.reset_index())
if "Date" in df_roll.columns:
    df_roll["Date"] = pd.to_datetime(df_roll["Date"], errors="coerce")
    df_roll.set_index("Date", inplace=True)

window = st.slider("Rolling window size (days):", 2, 30, 7, key="roll_window")
numeric_cols = df_roll.select_dtypes(include=[np.number]).columns.tolist()

if numeric_cols:
    target_col = st.selectbox("Column to analyze:", numeric_cols, key="roll_col")
    df_roll[f"{window}-day MA"] = df_roll[target_col].rolling(window=window).mean().round(2)
    df_roll[f"{window}-day Std"] = df_roll[target_col].rolling(window=window).std().round(2)

    show_code(f"df['{target_col}'].rolling(window={window}).mean()\ndf['{target_col}'].rolling(window={window}).std()")
    st.dataframe(df_roll.head(20), use_container_width=True)
    st.line_chart(df_roll[[target_col, f"{window}-day MA"]])
else:
    st.warning("No numeric columns found in the uploaded data.")


# ═══════════════════════════════════════════════════════
# STEP 6 — Pivot Tables
# ═══════════════════════════════════════════════════════
step_header(6, "Pivot Tables")

default_pivot = pd.DataFrame({
    "Date": ["2023-01-01", "2023-01-02", "2023-01-03", "2023-01-04", "2023-01-05", "2023-01-06", "2023-01-07", "2023-01-08", "2023-01-09"],
    "Product": ["X", "X", "Y", "Y", "Z", "Z", "X", "Y", "Z"],
    "Region": ["North", "North", "South", "South", "East", "East", "West", "West", "West"],
    "Units": [10, 20, 30, 40, 50, 60, 70, 80, 90],
    "Profit": [100, 200, 300, 400, 500, 600, 700, 800, 900],
})

df_pivot = data_uploader("pivot_upload", default_pivot)
st.dataframe(df_pivot, use_container_width=True)

all_cols = df_pivot.columns.tolist()
num_cols = df_pivot.select_dtypes(include=[np.number]).columns.tolist()
cat_cols = [c for c in all_cols if c not in num_cols]

if cat_cols and num_cols:
    c1, c2, c3, c4 = st.columns(4)
    piv_index = c1.selectbox("Index:", cat_cols, key="piv_idx")
    remaining_cats = [c for c in cat_cols if c != piv_index]
    piv_columns = c2.selectbox("Columns:", remaining_cats if remaining_cats else cat_cols, key="piv_cols")
    piv_values = c3.selectbox("Values:", num_cols, key="piv_vals")
    piv_agg = c4.selectbox("Aggfunc:", ["sum", "mean", "count", "min", "max"], key="piv_agg")

    show_code(f"pd.pivot_table(df, index='{piv_index}', columns='{piv_columns}', values='{piv_values}', aggfunc='{piv_agg}', fill_value=0)")

    try:
        pivot_result = pd.pivot_table(df_pivot, index=piv_index, columns=piv_columns, values=piv_values, aggfunc=piv_agg, fill_value=0)
        st.dataframe(pivot_result, use_container_width=True)
    except Exception as e:
        st.error(f"Pivot error: {e}")
else:
    st.info("Need both categorical and numeric columns for pivot tables.")

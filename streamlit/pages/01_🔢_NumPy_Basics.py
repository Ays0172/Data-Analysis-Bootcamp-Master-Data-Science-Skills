"""
Module 1 — NumPy Basics
========================
Interactive exploration of NumPy arrays, indexing, math operations, and set operations.
"""

import streamlit as st
import numpy as np
import sys, os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from utils.styles import inject_custom_css, hero, step_header
from utils.helpers import show_code, show_explanation, data_uploader, create_metric_cards
import pandas as pd

st.set_page_config(page_title="NumPy Basics", page_icon="🔢", layout="wide")
inject_custom_css()
hero("🔢 NumPy Basics", "Arrays, indexing, math operations, aggregations & set operations")

# ═══════════════════════════════════════════════════════
# STEP 1 — Array Creation
# ═══════════════════════════════════════════════════════
step_header(1, "Array Creation")

st.markdown("Create NumPy arrays using different methods. Adjust the parameters to see how they change.")

tab1, tab2, tab3, tab4 = st.tabs(["np.array", "np.arange", "np.linspace", "np.random"])

with tab1:
    st.markdown("**Create an array from a list of values:**")
    user_values = st.text_input("Enter comma-separated values:", "1, 2, 3, 4, 5", key="np_array_input")
    try:
        vals = [float(x.strip()) for x in user_values.split(",") if x.strip()]
        arr = np.array(vals)
        col1, col2 = st.columns(2)
        with col1:
            show_code(f"arr = np.array({vals})\nprint(arr)\nprint(arr.shape)\nprint(arr.dtype)")
        with col2:
            st.markdown("**Output:**")
            st.code(f"{arr}\nShape: {arr.shape}\nDtype: {arr.dtype}")
    except ValueError:
        st.error("Please enter valid numbers separated by commas.")

with tab2:
    st.markdown("**Generate evenly spaced values within a range:**")
    c1, c2, c3 = st.columns(3)
    start = c1.number_input("Start", value=0, key="arange_start")
    stop = c2.number_input("Stop", value=30, key="arange_stop")
    step = c3.number_input("Step", value=3, min_value=1, key="arange_step")
    arr_range = np.arange(start, stop, step)
    show_code(f"np.arange({start}, {stop}, {step})")
    st.write(arr_range)

with tab3:
    st.markdown("**Generate evenly spaced numbers over a specified interval:**")
    c1, c2, c3 = st.columns(3)
    ls_start = c1.number_input("Start", value=0.0, key="lin_start")
    ls_stop = c2.number_input("Stop", value=5.0, key="lin_stop")
    ls_num = c3.number_input("Num points", value=10, min_value=2, key="lin_num")
    arr_lin = np.linspace(ls_start, ls_stop, int(ls_num))
    show_code(f"np.linspace({ls_start}, {ls_stop}, {int(ls_num)})")
    st.write(arr_lin)

with tab4:
    st.markdown("**Generate random arrays:**")
    c1, c2 = st.columns(2)
    rows = c1.number_input("Rows", value=3, min_value=1, max_value=10, key="rand_rows")
    cols = c2.number_input("Cols", value=4, min_value=1, max_value=10, key="rand_cols")
    if st.button("🎲 Generate Random Array", key="gen_rand"):
        st.session_state["rand_arr"] = np.random.rand(int(rows), int(cols)).round(4)
    if "rand_arr" in st.session_state:
        show_code(f"np.random.rand({int(rows)}, {int(cols)})")
        st.dataframe(pd.DataFrame(st.session_state["rand_arr"]))


# ═══════════════════════════════════════════════════════
# STEP 2 — Indexing & Slicing
# ═══════════════════════════════════════════════════════
step_header(2, "Indexing & Slicing")

st.markdown("Access and slice elements from arrays. Experiment with 1D and 2D arrays.")

arr2d = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
st.markdown("**Working array (3×4):**")
st.dataframe(pd.DataFrame(arr2d, columns=[f"Col {i}" for i in range(4)], index=[f"Row {i}" for i in range(3)]))

c1, c2 = st.columns(2)
row_idx = c1.number_input("Row index", 0, 2, 0, key="idx_row")
col_idx = c2.number_input("Col index", 0, 3, 2, key="idx_col")

show_code(f"arr2d[{row_idx}, {col_idx}]  →  {arr2d[int(row_idx), int(col_idx)]}")

st.markdown("**Slicing:**")
c1, c2, c3, c4 = st.columns(4)
r_start = c1.number_input("Row start", 0, 2, 0, key="sl_rs")
r_end = c2.number_input("Row end", 0, 3, 2, key="sl_re")
c_start = c3.number_input("Col start", 0, 3, 0, key="sl_cs")
c_end = c4.number_input("Col end", 0, 4, 3, key="sl_ce")

sliced = arr2d[int(r_start):int(r_end), int(c_start):int(c_end)]
show_code(f"arr2d[{int(r_start)}:{int(r_end)}, {int(c_start)}:{int(c_end)}]")
st.dataframe(pd.DataFrame(sliced))


# ═══════════════════════════════════════════════════════
# STEP 3 — Math Operations
# ═══════════════════════════════════════════════════════
step_header(3, "Element-wise Math Operations")

st.markdown("Apply mathematical functions element-wise to arrays.")

arr_math = np.array([0.5, 1.0, 1.5, 2.0, 2.5])
st.code(f"arr = {arr_math}")

ops = {
    "np.exp(arr)": np.exp,
    "np.log(arr)": np.log,
    "np.log2(arr)": np.log2,
    "np.log10(arr)": np.log10,
    "np.sin(arr)": np.sin,
    "np.cos(arr)": np.cos,
    "np.tan(arr)": np.tan,
    "np.sqrt(arr)": np.sqrt,
    "arr ** 2": lambda x: x ** 2,
    "arr / 3": lambda x: x / 3,
}

selected_op = st.selectbox("Choose an operation:", list(ops.keys()), key="math_op")
result = ops[selected_op](arr_math)
show_code(f"{selected_op}\n→ {np.round(result, 6)}")


# ═══════════════════════════════════════════════════════
# STEP 4 — Aggregations
# ═══════════════════════════════════════════════════════
step_header(4, "Aggregations (sum, mean, std, min, max)")

# Default dataset
default_agg = pd.DataFrame(np.random.rand(6, 6).round(4), columns=[f"C{i}" for i in range(6)])
df_agg = data_uploader("agg_uploader", default_agg)

st.dataframe(df_agg, use_container_width=True)

arr_agg = df_agg.select_dtypes(include=[np.number]).values

agg_func = st.selectbox("Aggregation:", ["sum", "mean", "std", "min", "max"], key="agg_func")
axis_choice = st.radio("Axis:", ["All (flatten)", "Axis 0 (columns)", "Axis 1 (rows)"], horizontal=True, key="agg_axis")

agg_map = {"sum": np.sum, "mean": np.mean, "std": np.std, "min": np.min, "max": np.max}
axis_val = None if "All" in axis_choice else (0 if "0" in axis_choice else 1)

result_agg = agg_map[agg_func](arr_agg, axis=axis_val)
show_code(f"np.{agg_func}(arr, axis={axis_val})")
if axis_val is None:
    st.metric(agg_func.upper(), f"{result_agg:.4f}")
else:
    st.write(np.round(result_agg, 4))


# ═══════════════════════════════════════════════════════
# STEP 5 — Set Operations
# ═══════════════════════════════════════════════════════
step_header(5, "Set Operations")

c1, c2 = st.columns(2)
a_input = c1.text_input("Array A (comma-separated):", "1,2,3,4", key="set_a")
b_input = c2.text_input("Array B (comma-separated):", "3,4,5,6", key="set_b")

try:
    a = np.array([int(x.strip()) for x in a_input.split(",")])
    b = np.array([int(x.strip()) for x in b_input.split(",")])

    results = {
        "np.unique(a)": np.unique(a),
        "np.intersect1d(a, b)": np.intersect1d(a, b),
        "np.union1d(a, b)": np.union1d(a, b),
        "np.setdiff1d(a, b)": np.setdiff1d(a, b),
        "np.setdiff1d(b, a)": np.setdiff1d(b, a),
        "np.setxor1d(a, b)": np.setxor1d(a, b),
    }

    for expr, val in results.items():
        st.code(f"{expr}  →  {val}")
except ValueError:
    st.error("Enter valid integers separated by commas.")

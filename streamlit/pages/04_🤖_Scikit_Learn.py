"""
Module 4 — Scikit-Learn Pipeline
==================================
Interactive ML pipeline builder — impute, encode, scale, and train a model.
"""

import streamlit as st
import pandas as pd
import numpy as np
import sys, os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from utils.styles import inject_custom_css, hero, step_header
from utils.helpers import show_code, data_uploader

st.set_page_config(page_title="Scikit-Learn", page_icon="🤖", layout="wide")
inject_custom_css()
hero("🤖 Scikit-Learn Pipeline", "Build an ML pipeline step by step — from raw data to predictions")


# ═══════════════════════════════════════════════════════
# STEP 1 — Understanding the Pipeline Concept
# ═══════════════════════════════════════════════════════
step_header(1, "Pipeline Concept")

st.markdown("""
A **Scikit-Learn Pipeline** chains multiple data processing steps into a single object.
This ensures reproducibility and prevents data leakage.
""")

st.markdown("""
```
Raw Data  →  Impute Missing  →  Encode Categoricals  →  Scale Numerics  →  Train Model  →  Predictions
```
""")

st.info("💡 **Why pipelines?** — They guarantee that the same transformations are applied during training AND prediction, avoiding common mistakes.")

show_code("""from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression""")


# ═══════════════════════════════════════════════════════
# STEP 2 — Prepare Data & Build Pipeline
# ═══════════════════════════════════════════════════════
step_header(2, "Prepare Data & Build Pipeline")

default_ml = pd.DataFrame({
    "age": [25, 30, None, 40, 45, 28, 35, None, 50, 22],
    "income": [50000, 60000, 70000, 80000, None, 55000, 65000, 75000, None, 48000],
    "gender": ["Male", "Female", "Female", "Male", "Female", "Male", "Female", "Male", "Female", "Male"],
    "department": ["HR", "Finance", "IT", "Marketing", "Sales", "HR", "IT", "Finance", "Sales", "Marketing"],
    "purchased": [1, 0, 1, 0, 1, 1, 0, 1, 0, 1],
})

df_ml = data_uploader("ml_upload", default_ml)
st.dataframe(df_ml, use_container_width=True)

st.markdown("**Configure your pipeline:**")

all_cols = df_ml.columns.tolist()
num_cols = df_ml.select_dtypes(include=[np.number]).columns.tolist()
cat_cols = df_ml.select_dtypes(include=["object", "category"]).columns.tolist()

target_col = st.selectbox("Target column (y):", all_cols, index=len(all_cols) - 1, key="target")
feature_cols = [c for c in all_cols if c != target_col]
num_features = [c for c in num_cols if c != target_col]
cat_features = [c for c in cat_cols if c != target_col]

c1, c2 = st.columns(2)
c1.markdown(f"**Numeric features:** `{num_features}`")
c2.markdown(f"**Categorical features:** `{cat_features}`")

impute_strategy = st.selectbox("Imputer strategy (numeric):", ["mean", "median", "most_frequent"], key="imp_strat")
scaler_choice = st.selectbox("Scaler:", ["StandardScaler", "None"], key="scaler")

show_code(f"""numerical_features = {num_features}
categorical_features = {cat_features}

# Numeric pipeline: impute → scale
num_pipeline = Pipeline([
    ('imputer', SimpleImputer(strategy='{impute_strategy}')),
    {'("scaler", StandardScaler()),' if scaler_choice == "StandardScaler" else "# No scaler"}
])

# Categorical pipeline: impute → one-hot encode
cat_pipeline = Pipeline([
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('encoder', OneHotEncoder(handle_unknown='ignore')),
])

# Column transformer combines both
preprocessor = ColumnTransformer([
    ('num', num_pipeline, numerical_features),
    ('cat', cat_pipeline, categorical_features),
])

# Full pipeline: preprocess → model
pipeline = Pipeline([
    ('preprocessor', preprocessor),
    ('classifier', LogisticRegression(max_iter=1000)),
])""")


# ═══════════════════════════════════════════════════════
# STEP 3 — Train & Evaluate
# ═══════════════════════════════════════════════════════
step_header(3, "Train & Evaluate")

if st.button("🚀 Train Pipeline", key="train_btn"):
    try:
        from sklearn.pipeline import Pipeline as SKPipeline
        from sklearn.compose import ColumnTransformer
        from sklearn.preprocessing import OneHotEncoder, StandardScaler
        from sklearn.impute import SimpleImputer
        from sklearn.linear_model import LogisticRegression
        from sklearn.model_selection import train_test_split

        X = df_ml[feature_cols]
        y = df_ml[target_col]

        # Build pipelines
        num_steps = [("imputer", SimpleImputer(strategy=impute_strategy))]
        if scaler_choice == "StandardScaler":
            num_steps.append(("scaler", StandardScaler()))
        num_pipeline = SKPipeline(num_steps)

        cat_pipeline = SKPipeline([
            ("imputer", SimpleImputer(strategy="most_frequent")),
            ("encoder", OneHotEncoder(handle_unknown="ignore")),
        ])

        preprocessor = ColumnTransformer([
            ("num", num_pipeline, num_features),
            ("cat", cat_pipeline, cat_features),
        ])

        pipeline = SKPipeline([
            ("preprocessor", preprocessor),
            ("classifier", LogisticRegression(max_iter=1000)),
        ])

        # Split & train
        if len(df_ml) >= 6:
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
        else:
            X_train, X_test, y_train, y_test = X, X, y, y

        pipeline.fit(X_train, y_train)
        train_score = pipeline.score(X_train, y_train)
        test_score = pipeline.score(X_test, y_test)
        preds = pipeline.predict(X_test)

        c1, c2 = st.columns(2)
        c1.metric("Train Accuracy", f"{train_score:.2%}")
        c2.metric("Test Accuracy", f"{test_score:.2%}")

        st.markdown("**Predictions on test set:**")
        result_df = X_test.copy()
        result_df["Actual"] = y_test.values
        result_df["Predicted"] = preds
        st.dataframe(result_df, use_container_width=True)

        st.success("✅ Pipeline trained successfully!")

    except ImportError:
        st.error("❌ scikit-learn is not installed. Run: `pip install scikit-learn`")
    except Exception as e:
        st.error(f"❌ Training error: {e}")
else:
    st.info("👆 Click **Train Pipeline** to run the end-to-end ML workflow.")

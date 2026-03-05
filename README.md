# 📊 Data Analysis Bootcamp — Master Data Science Skills

An interactive, hands-on learning platform covering **NumPy**, **Pandas**, **Data Visualization**, **Scikit-Learn**, and real-world **projects** — all wrapped in a polished Streamlit web app.

---

## 🚀 Quick Start

```bash
# 1. Clone the repo
git clone https://github.com/<your-username>/Data-Analysis-Bootcamp-Master-Data-Science-Skills.git
cd Data-Analysis-Bootcamp-Master-Data-Science-Skills

# 2. Install dependencies
pip install -r streamlit/requirements.txt

# 3. Launch the app
streamlit run streamlit/app.py
```

The app opens at **http://localhost:8501** with a sidebar to navigate between modules.

---

## 📂 Project Structure

```
Data-Analysis-Bootcamp-Master-Data-Science-Skills/
│
├── numpy/                          # NumPy notebooks
│   ├── basic_commands.ipynb        # Arrays, indexing, arange, linspace, random, zeros/ones
│   ├── basic command2.ipynb        # Diagonal, ndim, size, shape, math ops, aggregations, slicing, transpose
│   └── Counting_function.ipynb     # Unique, intersect, setdiff, union, setxor
│
├── pandas/                         # Pandas notebooks
│   ├── Dropna.ipynb                # Handling missing data (dropna)
│   ├── data_sort_values_bycolumns.ipynb  # Multi-column sorting
│   ├── merge_concat.ipynb          # Merge & concatenate DataFrames
│   ├── cut_qcut.ipynb              # Customer segmentation with cut/qcut
│   ├── df_rolling.ipynb            # Rolling window statistics (MA, std)
│   ├── PD_PivotTable.ipynb         # Pivot tables with multiple aggregations
│   ├── pandas_pyplot.ipynb         # Matplotlib plotting with Pandas
│   ├── ReSample.ipynb              # Time-series resampling
│   └── LinearRegression_Heatmap.ipynb  # Correlation heatmaps & linear regression
│
├── ScikitLearn/                    # Machine Learning
│   └── Scikit_Learn_pipeline.ipynb # End-to-end ML pipeline
│
├── Projects/                       # Applied projects
│   ├── proj1_melteddata.ipynb      # Wide → long data transformation (pd.melt)
│   └── proj2_pltting.ipynb         # Plotting challenge
│
├── streamlit/                      # 🌟 Interactive Streamlit App
│   ├── app.py                      # Home page — hero section, module cards
│   ├── requirements.txt            # Python dependencies
│   ├── utils/
│   │   ├── styles.py               # Custom CSS theming (dark gradient UI)
│   │   └── helpers.py              # Data uploader, code display, metrics
│   └── pages/
│       ├── 01_🔢_NumPy_Basics.py   # Arrays, indexing, math, aggregations, set ops
│       ├── 02_🐼_Pandas_Essentials.py  # Dropna, sort, merge, cut/qcut, rolling, pivot
│       ├── 03_📈_Data_Visualization.py # Charts, resampling, heatmaps
│       ├── 04_🤖_Scikit_Learn.py   # Interactive ML pipeline builder
│       └── 05_🚀_Projects.py       # Data melt & plotting challenge
│
└── README.md                       # ← You are here
```

---

## 🎓 Modules Overview

| # | Module | Notebooks | Key Concepts |
|---|--------|-----------|--------------|
| 1 | **🔢 NumPy Basics** | 3 | Arrays, indexing, slicing, math ops, aggregations, set operations |
| 2 | **🐼 Pandas Essentials** | 7 | DataFrames, dropna, sort, merge/concat, cut/qcut, rolling, pivot tables |
| 3 | **📈 Data Visualization** | 3 | Matplotlib (line, bar, scatter, histogram), Plotly heatmaps, time-series resampling |
| 4 | **🤖 Scikit-Learn** | 1 | ML pipelines — imputation, encoding, scaling, logistic regression |
| 5 | **🚀 Projects** | 2 | Data melt (wide→long), interactive plotting challenge |

---

## 🌟 Streamlit App Features

- **Step-by-step learning** — Each module is broken into clear, sequential steps
- **Default datasets included** — Every page loads with a built-in dataset so you can start immediately
- **Bring Your Own Data** — Upload CSV or Excel files to apply concepts to your own datasets
- **Live interactive widgets** — Adjust parameters and see results update in real time
- **Code snippets** — Every operation shows the equivalent Python code
- **Beautiful dark UI** — Gradient headers, glassmorphism cards, custom theming
- **6 Plotly chart types** — Scatter, box, violin, histogram, strip, and sunburst

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| **Python 3.11+** | Core language |
| **Streamlit** | Web app framework |
| **NumPy** | Numerical computing |
| **Pandas** | Data manipulation |
| **Matplotlib** | Static visualizations |
| **Plotly** | Interactive charts |
| **Scikit-Learn** | Machine learning pipeline |

---

## 📋 Requirements

```
streamlit>=1.30.0
pandas
numpy
matplotlib
plotly
scikit-learn
openpyxl
```

Install with:
```bash
pip install -r streamlit/requirements.txt
```

---

## 📸 Screenshots

> Launch the app with `streamlit run streamlit/app.py` to see the full experience!

- **Home Page** — Hero section with gradient background, module cards, and course metrics
- **NumPy Module** — Interactive array creation, slicing, and math operations
- **Pandas Module** — Live dropna, sort, merge, and pivot table builders
- **Visualization** — Chart gallery with 5+ chart types and style picker
- **Scikit-Learn** — Build and train an ML pipeline with live accuracy metrics
- **Projects** — Data melt transformer and multi-chart plotting challenge

---

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📜 License

This project is open source and available for educational purposes.

---

<p align="center">
  Built with ❤️ for learning Data Science
</p>

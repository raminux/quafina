# quafina — Quantitative Finance Starter Kit

A hands-on, notebook-driven course covering the mathematics, statistics, and programming behind modern quantitative finance and algorithmic trading. Every concept is taught with both rigorous theory and working Python code.

---

## Purpose

This repository is a structured learning path from mathematical foundations to production trading systems. It is intended for:

- Aspiring quants and algorithmic traders
- Data scientists and developers pivoting into finance
- Finance professionals adding quantitative skills
- Students preparing for quant finance interviews

---

## Repository Structure

```
quafina/
├── notebooks/
│   ├── module_01_math/                         # Probability, Linear Algebra, Calculus
│   ├── module_02_financial_markets_fundamentals/  # Microstructure, Asset Classes, Data
│   ├── module_03_time_series_analysis/         # ARIMA, GARCH, VAR, Kalman
│   ├── module_04_portfolio_theory_risk_management/ # MPT, VaR, HRP, Kelly
│   └── module_05_algorithmic_trading_strategies/  # Momentum, Mean Reversion, ML
└── TOC.md                                      # Detailed table of contents
```

---

## How to Use

**1. Clone the repository**

```bash
git clone https://github.com/raminux/quafina.git
cd quafina
```

**2. Install dependencies**

```bash
pip install numpy pandas scipy matplotlib seaborn scikit-learn xgboost statsmodels jupyter
```

**3. Launch Jupyter**

```bash
jupyter notebook
```

**4. Follow the modules in order**

Start with `notebooks/module_01_math/` and work through sequentially. Each notebook is self-contained with explanations, code, and visualizations.

See [TOC.md](TOC.md) for a full listing of all completed notebooks with direct links.

---

## Prerequisites

- Basic Python (loops, functions, NumPy/Pandas basics)
- Introductory statistics and calculus
- Familiarity with financial concepts (stocks, returns, risk) is helpful but not required

---

## Tools & Libraries

| Category | Libraries |
|----------|-----------|
| Core | NumPy, Pandas, SciPy |
| Visualization | Matplotlib, Seaborn |
| Machine Learning | Scikit-learn, XGBoost |
| Time Series | Statsmodels |
| Notebooks | Jupyter |

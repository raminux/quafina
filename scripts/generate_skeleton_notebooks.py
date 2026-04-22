"""
Generate skeleton Jupyter notebooks for modules 6–14 of the quafina course.
Each notebook has: intro header, setup cell, section cells, closing reflection.
"""

import json
import os
import uuid

NOTEBOOKS_DIR = os.path.join(os.path.dirname(__file__), "..", "notebooks")


def cell_id():
    return uuid.uuid4().hex[:8]


def md_cell(source: str) -> dict:
    return {
        "cell_type": "markdown",
        "id": cell_id(),
        "metadata": {},
        "source": source,
    }


def code_cell(source: str) -> dict:
    return {
        "cell_type": "code",
        "execution_count": None,
        "id": cell_id(),
        "metadata": {},
        "outputs": [],
        "source": source,
    }


def make_notebook(cells: list) -> dict:
    return {
        "cells": cells,
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3",
            },
            "language_info": {
                "name": "python",
                "version": "3.11.0",
            },
        },
        "nbformat": 4,
        "nbformat_minor": 5,
    }


def write_notebook(path: str, nb: dict):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        json.dump(nb, f, indent=1)
    print(f"  Created: {os.path.relpath(path)}")


# ---------------------------------------------------------------------------
# Module definitions
# Each entry: (module_dir, filename, module_title, subtitle, imports, sections)
# sections: list of (section_title, theory_bullets, practice_bullets)
# ---------------------------------------------------------------------------

MODULES = [

    # ── Module 6 ────────────────────────────────────────────────────────────
    (
        "module_06_derivatives_options_trading",
        "6_1_options_pricing_theory.ipynb",
        "Module 6.1 — Options Pricing Theory",
        "Black–Scholes, Greeks, and the Volatility Surface",
        """\
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm
from scipy.optimize import brentq
from math import log, sqrt, exp

np.random.seed(42)
plt.style.use('seaborn-v0_8-darkgrid')
print("Module 6.1 environment ready.")""",
        [
            ("Black–Scholes Model Derivation",
             ["No-arbitrage argument and replicating portfolio",
              "Risk-neutral pricing and the Q-measure",
              "Black–Scholes formula for European calls and puts",
              "Assumptions: GBM, constant σ, frictionless markets"],
             ["Implement BS pricer from scratch",
              "Verify put–call parity numerically",
              "Price a strip of options across strikes"]),
            ("Put–Call Parity",
             ["C - P = S - Ke^{-rT}",
              "Arbitrage enforcement of parity",
              "Synthetic positions and replication"],
             ["Verify parity numerically across strikes",
              "Construct synthetic long forward"]),
            ("The Greeks: Delta, Gamma, Vega, Theta, Rho",
             ["Partial derivatives of option price",
              "Delta as probability proxy (risk-neutral)",
              "Gamma as convexity / curvature",
              "Vega and volatility sensitivity"],
             ["Greeks calculator and visualizer",
              "Plot Greeks as function of S, T, σ",
              "Greeks surface plots"]),
            ("Implied Volatility and the Volatility Surface",
             ["Implied vol: invert BS formula given market price",
              "Volatility smile and skew — why markets violate BS",
              "Term structure of volatility",
              "Volatility surface interpolation"],
             ["Implied vol solver using Brent's method",
              "Build a volatility smile from option chain",
              "Interpolate and plot volatility surface"]),
        ],
    ),
    (
        "module_06_derivatives_options_trading",
        "6_2_options_strategies.ipynb",
        "Module 6.2 — Options Strategies",
        "Directional, Volatility, and Income Strategies",
        """\
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm
from math import log, sqrt, exp

np.random.seed(42)
plt.style.use('seaborn-v0_8-darkgrid')
print("Module 6.2 environment ready.")""",
        [
            ("Directional Strategies",
             ["Long/short calls and puts",
              "Bull and bear spreads (debit/credit)",
              "Risk-reward profiles and breakevens"],
             ["Payoff diagram for vertical spreads",
              "Breakeven and max profit/loss calculator"]),
            ("Volatility Strategies",
             ["Straddles and strangles — long and short",
              "Butterflies and condors",
              "Volatility as an asset class"],
             ["Straddle P&L as function of realized vol",
              "Compare straddle vs strangle risk-reward"]),
            ("Income Strategies",
             ["Covered calls and cash-secured puts",
              "Iron condors and iron butterflies",
              "Theta decay as income source"],
             ["Iron condor P&L diagram",
              "Probability of profit estimation"]),
            ("Delta Hedging and Portfolio Greeks",
             ["Dynamic delta hedging — theory and practice",
              "P&L from gamma scalping",
              "Greeks aggregation across a multi-leg book"],
             ["Simulate delta hedging P&L over GBM path",
              "Gamma scalping simulation"]),
            ("Volatility Arbitrage",
             ["Realized vs implied volatility",
              "Vega-neutral delta-hedged positions",
              "Variance swaps and VIX basics"],
             ["Track realized vs implied vol divergence",
              "Simulate vol arb strategy"]),
        ],
    ),
    (
        "module_06_derivatives_options_trading",
        "6_3_advanced_derivatives.ipynb",
        "Module 6.3 — Advanced Derivatives",
        "Exotic Options, Futures, and Numerical Methods",
        """\
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm
from math import log, sqrt, exp

np.random.seed(42)
plt.style.use('seaborn-v0_8-darkgrid')
print("Module 6.3 environment ready.")""",
        [
            ("Exotic Options",
             ["Asian options — average price/strike",
              "Barrier options — knock-in and knock-out",
              "Lookback and binary (digital) options",
              "Path dependency and its pricing challenges"],
             ["Monte Carlo pricer for Asian option",
              "Barrier option via Monte Carlo with absorption"]),
            ("Futures and Forwards Pricing",
             ["Cost of carry model: F = S * e^{(r-q)T}",
              "Basis, convergence, and roll yield",
              "Futures vs forwards: marking-to-market"],
             ["Futures fair value calculator",
              "Basis trading simulation"]),
            ("Interest Rate Derivatives",
             ["Bond futures and duration hedging",
              "Interest rate swaps: fixed vs floating",
              "Caps, floors, and swaptions",
              "Yield curve and forward rates"],
             ["Swap pricing and DV01 calculation",
              "Yield curve construction from bootstrapping"]),
            ("Numerical Methods: Binomial Trees and Monte Carlo",
             ["CRR binomial tree for European and American options",
              "Monte Carlo with variance reduction",
              "Finite difference methods overview"],
             ["Binomial tree option pricer",
              "American put via binomial tree",
              "Monte Carlo with antithetic variates"]),
        ],
    ),

    # ── Module 7 ────────────────────────────────────────────────────────────
    (
        "module_07_machine_learning_ai_trading",
        "7_1_classical_machine_learning.ipynb",
        "Module 7.1 — Classical Machine Learning for Trading",
        "Regression, Classification, Clustering, and Feature Selection",
        """\
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression, LogisticRegression, Ridge, Lasso
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import TimeSeriesSplit, cross_val_score
from sklearn.metrics import classification_report, mean_squared_error
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import warnings; warnings.filterwarnings('ignore')

np.random.seed(42)
plt.style.use('seaborn-v0_8-darkgrid')
print("Module 7.1 environment ready.")""",
        [
            ("Linear and Logistic Regression",
             ["OLS regression for return prediction",
              "Regularization: Ridge (L2) and Lasso (L1)",
              "Logistic regression for direction classification",
              "Interpretation and feature coefficients"],
             ["Return prediction with Ridge regression",
              "Direction classifier with logistic regression",
              "Feature importance via coefficients"]),
            ("Decision Trees and Random Forests",
             ["Decision tree splits and information gain",
              "Bagging and random feature selection",
              "Out-of-bag error and feature importances",
              "Overfitting risk in financial data"],
             ["Random forest direction predictor",
              "Feature importance bar chart",
              "Learning curves to detect overfitting"]),
            ("Support Vector Machines",
             ["Margin maximization and support vectors",
              "Kernel trick for non-linear boundaries",
              "SVM for regime classification"],
             ["SVM classifier on return features",
              "Kernel comparison: linear vs RBF"]),
            ("K-Means Clustering for Regime Detection",
             ["Unsupervised clustering of market states",
              "Feature engineering for regime clustering",
              "Interpreting cluster centroids as regimes"],
             ["Cluster daily market states",
              "Visualize regimes on price chart"]),
            ("Feature Selection and Engineering",
             ["Technical indicators as ML features",
              "Mutual information and correlation filtering",
              "PCA for feature compression",
              "Avoiding look-ahead bias in feature construction"],
             ["Build feature matrix from price data",
              "Select top-k features via mutual information"]),
        ],
    ),
    (
        "module_07_machine_learning_ai_trading",
        "7_2_deep_learning_for_finance.ipynb",
        "Module 7.2 — Deep Learning for Finance",
        "LSTMs, CNNs, Autoencoders, and Transformers",
        """\
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import warnings; warnings.filterwarnings('ignore')

# Deep learning imports (uncomment when environment is ready)
# import torch
# import torch.nn as nn
# from torch.utils.data import DataLoader, TensorDataset

np.random.seed(42)
plt.style.use('seaborn-v0_8-darkgrid')
print("Module 7.2 environment ready.")
print("Note: deep learning cells require PyTorch or TensorFlow.")""",
        [
            ("Neural Network Fundamentals",
             ["Feedforward networks: layers, activations, backpropagation",
              "Loss functions for regression vs classification",
              "Batch normalization, dropout, early stopping",
              "Why standard NNs are not sufficient for time series"],
             ["Build a simple MLP for return prediction",
              "Training loop with validation monitoring"]),
            ("Recurrent Neural Networks: LSTM and GRU",
             ["Vanishing gradient problem in simple RNNs",
              "LSTM gates: forget, input, output",
              "GRU as a simplified alternative",
              "Sequence-to-one vs sequence-to-sequence"],
             ["LSTM for multi-step return forecasting",
              "Compare LSTM vs GRU on price prediction"]),
            ("Convolutional Neural Networks for Time Series",
             ["1D convolution as pattern detector",
              "CNN for chart pattern recognition",
              "Temporal convolutional networks (TCN)"],
             ["1D CNN for candlestick pattern classification",
              "CNN feature map visualization"]),
            ("Autoencoders for Anomaly Detection",
             ["Encoder-decoder architecture",
              "Reconstruction error as anomaly score",
              "Detecting unusual market regimes or data errors"],
             ["Train autoencoder on return sequences",
              "Flag outlier days by reconstruction error"]),
            ("Attention Mechanisms and Transformers",
             ["Self-attention and positional encoding",
              "Transformer architecture overview",
              "Time-series Transformer for forecasting",
              "Limitations: data hunger and overfitting in finance"],
             ["Minimal transformer for return forecasting",
              "Attention weight visualization"]),
        ],
    ),
    (
        "module_07_machine_learning_ai_trading",
        "7_3_reinforcement_learning.ipynb",
        "Module 7.3 — Reinforcement Learning for Trading",
        "MDPs, Q-Learning, Policy Gradients, and Portfolio Allocation",
        """\
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import warnings; warnings.filterwarnings('ignore')

# RL imports (uncomment when environment is ready)
# import gymnasium as gym
# import torch
# import torch.nn as nn

np.random.seed(42)
plt.style.use('seaborn-v0_8-darkgrid')
print("Module 7.3 environment ready.")
print("Note: RL cells require gymnasium and PyTorch.")""",
        [
            ("Markov Decision Processes",
             ["States, actions, rewards, and transitions",
              "Discount factor and return",
              "Bellman equations",
              "Trading as an MDP: state = market features, action = position"],
             ["Define a simple trading MDP",
              "Simulate random policy as baseline"]),
            ("Q-Learning and Deep Q-Networks",
             ["Tabular Q-learning: value iteration",
              "DQN: function approximation with neural network",
              "Experience replay and target network",
              "Epsilon-greedy exploration"],
             ["Tabular Q-learning on a discretized trading environment",
              "DQN agent on simulated price environment"]),
            ("Policy Gradient Methods",
             ["REINFORCE algorithm",
              "Actor-Critic (A2C/A3C)",
              "Proximal Policy Optimization (PPO)",
              "Continuous action spaces for position sizing"],
             ["REINFORCE for simple trading task",
              "PPO agent with continuous position sizing"]),
            ("RL for Portfolio Management",
             ["Multi-asset portfolio as action space",
              "Reward shaping: Sharpe ratio vs raw return",
              "Transaction cost modeling in RL",
              "Benchmark comparison: RL vs buy-and-hold"],
             ["Portfolio RL environment",
              "Train and evaluate portfolio allocation agent"]),
        ],
    ),

    # ── Module 8 ────────────────────────────────────────────────────────────
    (
        "module_08_backtesting_strategy_evaluation",
        "8_1_backtesting_framework_design.ipynb",
        "Module 8.1 — Backtesting Framework Design",
        "Event-Driven Architecture, Bias Detection, and Realistic Simulation",
        """\
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from collections import deque
import warnings; warnings.filterwarnings('ignore')

np.random.seed(42)
plt.style.use('seaborn-v0_8-darkgrid')
print("Module 8.1 environment ready.")""",
        [
            ("Vectorized vs Event-Driven Backtesting",
             ["Vectorized: fast, simple, but limited realism",
              "Event-driven: realistic order flow simulation",
              "Trade-offs: development speed vs accuracy",
              "When each approach is appropriate"],
             ["Vectorized backtest on momentum signal",
              "Event-driven backtest skeleton"]),
            ("Survivorship Bias and Point-in-Time Data",
             ["Survivorship bias: only testing on survivors inflates returns",
              "Point-in-time data: only use information available at the time",
              "Lookahead bias: accidentally using future data in signal",
              "Methods to detect and eliminate each bias"],
             ["Demonstrate look-ahead bias with a simple example",
              "Point-in-time feature construction"]),
            ("Slippage and Commission Modeling",
             ["Fixed commission vs percentage vs per-share",
              "Slippage: market impact of large orders",
              "Bid-ask spread crossing",
              "Volume constraints on order fills"],
             ["Backtest with and without transaction costs",
              "Slippage model implementation"]),
            ("Corporate Actions and Data Cleaning",
             ["Splits, dividends, and adjusted prices",
              "Handling NaN and missing data",
              "Delisted stocks and survivorship",
              "Data vendor differences"],
             ["Adjust prices for splits and dividends",
              "Handle missing data in return matrix"]),
        ],
    ),
    (
        "module_08_backtesting_strategy_evaluation",
        "8_2_performance_metrics.ipynb",
        "Module 8.2 — Performance Metrics",
        "Sharpe, Sortino, Drawdown, and Risk-Adjusted Return Analysis",
        """\
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import warnings; warnings.filterwarnings('ignore')

np.random.seed(42)
plt.style.use('seaborn-v0_8-darkgrid')
print("Module 8.2 environment ready.")""",
        [
            ("Return-Based Metrics",
             ["Total return, CAGR, and annualized return",
              "Arithmetic vs geometric mean returns",
              "Volatility drag and the compounding effect"],
             ["Compute CAGR from return series",
              "Compare arithmetic vs geometric returns"]),
            ("Risk-Adjusted Ratios",
             ["Sharpe ratio: return per unit total risk",
              "Sortino ratio: return per unit downside risk",
              "Calmar ratio: return per unit max drawdown",
              "Information ratio and tracking error"],
             ["Implement all major risk-adjusted ratios",
              "Compare strategies on multi-metric dashboard"]),
            ("Drawdown Analysis",
             ["Maximum drawdown definition and calculation",
              "Drawdown duration and recovery time",
              "Ulcer index and pain ratio",
              "Drawdown as a risk management tool"],
             ["Drawdown series computation",
              "Drawdown chart with underwater plot"]),
            ("Win Rate, Profit Factor, and Expectancy",
             ["Win rate vs average win/loss ratio",
              "Profit factor: gross profit / gross loss",
              "Expectancy: expected value per trade",
              "Why a low win rate can be profitable"],
             ["Trade-level statistics from backtest",
              "Expectancy calculator"]),
            ("Statistical Significance of Backtest Results",
             ["t-test on Sharpe ratio",
              "Monte Carlo permutation test",
              "Deflated Sharpe ratio (Bailey & Lopez de Prado)",
              "Multiple testing corrections"],
             ["Sharpe ratio significance test",
              "Permutation test on strategy returns"]),
        ],
    ),
    (
        "module_08_backtesting_strategy_evaluation",
        "8_3_strategy_optimization_validation.ipynb",
        "Module 8.3 — Strategy Optimization and Validation",
        "Walk-Forward Analysis, Cross-Validation, and Overfitting Detection",
        """\
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import TimeSeriesSplit
import itertools
import warnings; warnings.filterwarnings('ignore')

np.random.seed(42)
plt.style.use('seaborn-v0_8-darkgrid')
print("Module 8.3 environment ready.")""",
        [
            ("Parameter Optimization",
             ["Grid search and brute-force optimization",
              "Gradient-free methods: genetic algorithms, Bayesian optimization",
              "The curse of dimensionality in parameter space",
              "Overfitting risk increases with number of parameters"],
             ["Grid search over SMA crossover parameters",
              "Bayesian optimization with scikit-optimize"]),
            ("Walk-Forward Analysis",
             ["In-sample vs out-of-sample split",
              "Rolling window walk-forward",
              "Anchored walk-forward",
              "Comparing IS vs OOS performance to detect overfit"],
             ["Walk-forward backtest implementation",
              "IS vs OOS Sharpe comparison chart"]),
            ("Time Series Cross-Validation",
             ["Why random CV fails for time series",
              "TimeSeriesSplit from sklearn",
              "Purged and embargoed cross-validation",
              "Combinatorial purged cross-validation (CPCV)"],
             ["TimeSeriesSplit on factor model",
              "Implement purging and embargo"]),
            ("Overfitting Detection",
             ["Deflated Sharpe ratio",
              "Probability of backtest overfitting (PBO)",
              "Out-of-sample degradation as a signal",
              "The multiple testing problem in strategy research"],
             ["PBO via combinatorial cross-validation",
              "Strategy robustness across parameter ranges"]),
        ],
    ),

    # ── Module 9 ────────────────────────────────────────────────────────────
    (
        "module_09_execution_order_management",
        "9_1_order_execution_algorithms.ipynb",
        "Module 9.1 — Order Execution Algorithms",
        "VWAP, TWAP, Implementation Shortfall, and Smart Order Routing",
        """\
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import warnings; warnings.filterwarnings('ignore')

np.random.seed(42)
plt.style.use('seaborn-v0_8-darkgrid')
print("Module 9.1 environment ready.")""",
        [
            ("Execution Benchmarks",
             ["VWAP: volume-weighted average price",
              "TWAP: time-weighted average price",
              "Arrival price and implementation shortfall",
              "End-of-day (MOC) benchmark"],
             ["Compute VWAP benchmark from intraday data",
              "Measure implementation shortfall"]),
            ("VWAP and TWAP Algorithms",
             ["VWAP strategy: participate proportional to volume profile",
              "TWAP strategy: uniform slicing over time horizon",
              "Adapting to intraday volume patterns",
              "Risk of front-running and signaling"],
             ["VWAP execution simulator",
              "TWAP execution simulator"]),
            ("Participation Rate Strategies",
             ["Percentage of volume (POV) execution",
              "Adaptive participation based on spread and impact",
              "Dark pool interaction"],
             ["POV execution simulation",
              "Compare POV vs VWAP on simulated data"]),
            ("Smart Order Routing",
             ["Fragmentation across venues",
              "Lit vs dark venue selection",
              "Latency and connectivity considerations",
              "Routing logic and order priority"],
             ["Simple SOR decision logic implementation",
              "Multi-venue fill simulation"]),
            ("Market Impact Models",
             ["Almgren-Chriss optimal execution model",
              "Temporary vs permanent market impact",
              "Optimal trajectory: balancing timing risk vs impact",
              "Empirical impact functions"],
             ["Almgren-Chriss optimal trajectory",
              "Market impact cost estimation"]),
        ],
    ),
    (
        "module_09_execution_order_management",
        "9_2_high_frequency_trading_concepts.ipynb",
        "Module 9.2 — High-Frequency Trading Concepts",
        "Microstructure, Latency, and Statistical Arbitrage at HFT Speeds",
        """\
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import warnings; warnings.filterwarnings('ignore')

np.random.seed(42)
plt.style.use('seaborn-v0_8-darkgrid')
print("Module 9.2 environment ready.")""",
        [
            ("Latency and Co-Location",
             ["Network latency: microseconds to milliseconds",
              "Co-location: placing servers at exchange data centers",
              "FPGA and hardware acceleration",
              "Tick-to-trade latency measurement"],
             ["Latency simulation model",
              "Tick-to-trade pipeline sketch"]),
            ("Order Book at Microsecond Scale",
             ["Level 1 vs Level 2 vs Level 3 data",
              "Order book reconstruction from feed",
              "Imbalance signals from order book",
              "Queue position and fill probability"],
             ["Order book reconstruction from tick data",
              "Order book imbalance signal"]),
            ("HFT Strategies Overview",
             ["Market making: capturing the spread",
              "Statistical arbitrage at HFT speeds",
              "Latency arbitrage",
              "News-based trading with low-latency feeds"],
             ["Simple market making simulation",
              "Spread capture P&L model"]),
            ("Risk Controls for HFT",
             ["Pre-trade risk checks at nanosecond scale",
              "Position limits and kill switches",
              "Fat-finger protection",
              "Real-time P&L monitoring"],
             ["Pre-trade risk check pseudocode",
              "Kill switch implementation sketch"]),
        ],
    ),
    (
        "module_09_execution_order_management",
        "9_3_position_management.ipynb",
        "Module 9.3 — Position Management",
        "Sizing, Kelly Criterion, Volatility Targeting, and Risk Controls",
        """\
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import warnings; warnings.filterwarnings('ignore')

np.random.seed(42)
plt.style.use('seaborn-v0_8-darkgrid')
print("Module 9.3 environment ready.")""",
        [
            ("Position Sizing Methods",
             ["Fixed fractional sizing",
              "Equal risk contribution sizing",
              "Volatility-adjusted sizing",
              "Signal-strength-proportional sizing"],
             ["Compare sizing methods on backtest",
              "Risk-adjusted sizing implementation"]),
            ("Kelly Criterion and Fractional Kelly",
             ["Kelly formula: f* = (bp - q) / b",
              "Continuous Kelly for normal returns",
              "Over-betting risk and drawdown",
              "Fractional Kelly as practical compromise"],
             ["Kelly sizing simulation",
              "Compare full Kelly vs fractional Kelly drawdowns"]),
            ("Volatility Targeting",
             ["Target constant portfolio volatility",
              "Scale position size by realized vol estimate",
              "EWMA volatility estimator",
              "Volatility targeting and Sharpe ratio"],
             ["Volatility targeting implementation",
              "Backtest with and without vol targeting"]),
            ("Portfolio Heat and Correlation Limits",
             ["Portfolio heat: sum of individual risk units",
              "Correlation-adjusted position sizing",
              "Maximum loss controls and stop-losses",
              "Drawdown-based de-risking rules"],
             ["Portfolio heat monitor",
              "Correlation-adjusted sizing calculator"]),
        ],
    ),

    # ── Module 10 ───────────────────────────────────────────────────────────
    (
        "module_10_production_systems_infrastructure",
        "10_1_trading_system_architecture.ipynb",
        "Module 10.1 — Trading System Architecture",
        "Design Patterns, Microservices, Message Queues, and Databases",
        """\
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import json
import time
from collections import deque
import warnings; warnings.filterwarnings('ignore')

np.random.seed(42)
print("Module 10.1 environment ready.")""",
        [
            ("System Design Patterns",
             ["Monolithic vs microservices architecture",
              "Event-driven architecture with message queues",
              "Separation of concerns: data, signal, execution, risk",
              "Latency vs throughput trade-offs"],
             ["Design a modular trading system diagram",
              "Sketch component interaction flow"]),
            ("Data Layer",
             ["Tick data storage: time-series databases",
              "TimescaleDB and InfluxDB for financial data",
              "SQL for reference data and trades",
              "Data compression and retention policies"],
             ["TimescaleDB schema design for tick data",
              "Query performance comparison"]),
            ("Message Queues and Event Streaming",
             ["Kafka fundamentals: topics, partitions, consumers",
              "Redis pub/sub for low-latency signaling",
              "Order flow as an event stream",
              "Exactly-once semantics"],
             ["Kafka producer/consumer sketch",
              "Redis pub/sub example"]),
            ("Containerization and Deployment",
             ["Docker for reproducible environments",
              "Docker Compose for multi-service setup",
              "Kubernetes for scaling",
              "CI/CD pipelines for trading systems"],
             ["Dockerfile for trading strategy",
              "Docker Compose for full system"]),
            ("Fault Tolerance and Redundancy",
             ["Stateless vs stateful components",
              "Health checks and circuit breakers",
              "Failover and disaster recovery",
              "Idempotency in order management"],
             ["Health check implementation",
              "Circuit breaker pattern sketch"]),
        ],
    ),
    (
        "module_10_production_systems_infrastructure",
        "10_2_risk_controls_compliance.ipynb",
        "Module 10.2 — Risk Controls and Compliance",
        "Pre-Trade Checks, Position Limits, Regulatory Requirements, and Audit Trails",
        """\
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import logging
import json
from datetime import datetime
import warnings; warnings.filterwarnings('ignore')

np.random.seed(42)
print("Module 10.2 environment ready.")""",
        [
            ("Pre-Trade Risk Checks",
             ["Order size and notional limits",
              "Position limits per instrument and sector",
              "Net and gross exposure limits",
              "Fat-finger price deviation checks"],
             ["Pre-trade risk check layer implementation",
              "Risk limit breach logging"]),
            ("Position and Loss Limits",
             ["Daily loss limits (DLL) and weekly loss limits",
              "Drawdown-based auto-pause",
              "Position aging and stale order cancellation",
              "Margin and leverage monitoring"],
             ["Real-time P&L monitor with limit alerts",
              "Auto-pause trigger implementation"]),
            ("Regulatory Requirements",
             ["MiFID II: trade reporting and best execution",
              "SEC Rule 15c3-5: market access risk controls",
              "CFTC regulations for futures trading",
              "Know-your-customer (KYC) and AML basics"],
             ["Trade report generation template",
              "Best execution analysis"]),
            ("Audit Trails and Logging",
             ["Structured logging for all order events",
              "Immutable audit trail requirements",
              "Log aggregation and search",
              "Reconstructing order history from logs"],
             ["Structured logging implementation",
              "Order event replay from audit log"]),
        ],
    ),
    (
        "module_10_production_systems_infrastructure",
        "10_3_monitoring_operations.ipynb",
        "Module 10.3 — Monitoring and Operations",
        "Dashboards, Alerting, Log Aggregation, and Disaster Recovery",
        """\
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time
import warnings; warnings.filterwarnings('ignore')

np.random.seed(42)
print("Module 10.3 environment ready.")""",
        [
            ("Real-Time Monitoring Dashboards",
             ["Key metrics: P&L, positions, fill rate, latency",
              "Grafana dashboards for trading systems",
              "Real-time streaming data visualization",
              "Alerting thresholds and escalation"],
             ["Build a mock real-time dashboard",
              "Metrics aggregation pipeline"]),
            ("Alerting and Incident Response",
             ["Alert fatigue vs alert blindness",
              "PagerDuty and on-call rotation",
              "Runbooks for common incidents",
              "Post-mortem analysis process"],
             ["Alert rule definition examples",
              "Incident response checklist"]),
            ("Log Aggregation (ELK Stack)",
             ["Elasticsearch, Logstash, Kibana overview",
              "Log shipping and parsing",
              "Querying logs for trade reconstruction",
              "Retention policies and cost management"],
             ["Log parsing with Python",
              "Query simulation for trade reconstruction"]),
            ("Backup and Disaster Recovery",
             ["Recovery time objective (RTO) and recovery point objective (RPO)",
              "Database backup strategies",
              "Multi-site redundancy",
              "Runbook for system recovery"],
             ["Backup script skeleton",
              "DR test checklist"]),
        ],
    ),

    # ── Module 11 ───────────────────────────────────────────────────────────
    (
        "module_11_live_trading_broker_integration",
        "11_1_broker_apis_connectivity.ipynb",
        "Module 11.1 — Broker APIs and Connectivity",
        "REST, WebSocket, FIX Protocol, and Order Management Systems",
        """\
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import requests
import json
import time
import warnings; warnings.filterwarnings('ignore')

np.random.seed(42)
print("Module 11.1 environment ready.")
print("Note: live broker cells require API credentials.")""",
        [
            ("REST APIs for Trading",
             ["HTTP methods: GET, POST, DELETE",
              "Authentication: OAuth2, API keys, HMAC signing",
              "Rate limiting and retry logic",
              "Error handling and idempotent requests"],
             ["Alpaca REST API: place and cancel order",
              "Rate limiter implementation"]),
            ("WebSocket for Real-Time Data",
             ["WebSocket protocol vs HTTP polling",
              "Subscribing to market data streams",
              "Reconnection logic and heartbeats",
              "Parsing streaming order book updates"],
             ["WebSocket market data client sketch",
              "Order book reconstruction from stream"]),
            ("FIX Protocol Basics",
             ["FIX message structure: header, body, trailer",
              "Common message types: New Order, Execution Report",
              "Session management: logon, heartbeat, logout",
              "FIX vs REST: latency and reliability trade-offs"],
             ["Parse a FIX execution report",
              "FIX message builder skeleton"]),
            ("Order Management Systems (OMS)",
             ["OMS responsibilities: order lifecycle management",
              "Position reconciliation with broker",
              "Multi-broker routing",
              "Integration with risk layer"],
             ["Simple OMS state machine",
              "Order lifecycle tracker"]),
        ],
    ),
    (
        "module_11_live_trading_broker_integration",
        "11_2_paper_trading.ipynb",
        "Module 11.2 — Paper Trading",
        "Simulated Trading Environments and Strategy Validation Before Going Live",
        """\
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import warnings; warnings.filterwarnings('ignore')

np.random.seed(42)
plt.style.use('seaborn-v0_8-darkgrid')
print("Module 11.2 environment ready.")""",
        [
            ("Paper Trading Environments",
             ["Broker-provided simulators (Alpaca, IBKR)",
              "Custom fill simulation with realistic assumptions",
              "Market data replay for historical simulation",
              "Why paper trading differs from live trading"],
             ["Set up Alpaca paper trading account",
              "Custom fill simulator implementation"]),
            ("Realistic Fill Simulation",
             ["Partial fills and order queuing",
              "Slippage based on order size and spread",
              "Volume constraints",
              "Latency simulation"],
             ["Fill simulator with partial fills",
              "Slippage model calibration"]),
            ("Performance Tracking in Paper Trading",
             ["Daily P&L tracking",
              "Position reconciliation",
              "Comparing paper vs backtest performance",
              "Identifying backtest overfitting in paper trading"],
             ["Paper trading performance dashboard",
              "Paper vs backtest comparison analysis"]),
            ("Transition Planning to Live Trading",
             ["Risk capital sizing for initial live deployment",
              "Gradual ramp-up strategy",
              "When to scale up vs pull back",
              "Circuit breakers for live deployment"],
             ["Ramp-up schedule template",
              "Go/no-go decision framework"]),
        ],
    ),
    (
        "module_11_live_trading_broker_integration",
        "11_3_going_live.ipynb",
        "Module 11.3 — Going Live",
        "Capital Requirements, Deployment, Monitoring, and Psychological Aspects",
        """\
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import warnings; warnings.filterwarnings('ignore')

np.random.seed(42)
plt.style.use('seaborn-v0_8-darkgrid')
print("Module 11.3 environment ready.")""",
        [
            ("Capital Requirements and Sizing",
             ["Minimum capital for meaningful risk-adjusted returns",
              "Margin requirements by asset class",
              "Diversification across strategies",
              "Kelly-based capital allocation"],
             ["Capital requirement calculator",
              "Multi-strategy capital allocation"]),
            ("Deploying the First Live Strategy",
             ["Pre-deployment checklist",
              "Gradual position sizing ramp-up",
              "Monitoring first hours and days",
              "Handling unexpected behavior"],
             ["Pre-deployment checklist template",
              "Live monitoring dashboard sketch"]),
            ("Performance vs Backtest Analysis",
             ["Sources of live vs backtest divergence",
              "Execution slippage vs assumed slippage",
              "Market regime changes post-backtest",
              "When to stop a live strategy"],
             ["Live vs backtest divergence analysis",
              "Stop criterion implementation"]),
            ("Psychological Aspects of Live Trading",
             ["Over-trading after drawdowns",
              "Confirmation bias in signal interpretation",
              "Sticking to the system vs discretionary override",
              "Journal keeping and performance review"],
             ["Trading journal template",
              "Discipline scorecard"]),
        ],
    ),

    # ── Module 12 ───────────────────────────────────────────────────────────
    (
        "module_12_advanced_topics_research",
        "12_1_alternative_data.ipynb",
        "Module 12.1 — Alternative Data",
        "Sentiment, Satellite Imagery, Web Scraping, and Alpha Generation",
        """\
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import requests
import json
import re
import warnings; warnings.filterwarnings('ignore')

np.random.seed(42)
plt.style.use('seaborn-v0_8-darkgrid')
print("Module 12.1 environment ready.")""",
        [
            ("What Is Alternative Data?",
             ["Definition: any non-traditional data source",
              "Data types: text, geospatial, transactional, IoT",
              "Alpha decay: why alt data edges erode",
              "Procurement, cleaning, and compliance"],
             ["Survey of alt data sources",
              "Signal pipeline outline"]),
            ("Sentiment from News and Social Media",
             ["VADER and TextBlob for quick sentiment scoring",
              "FinBERT for finance-specific sentiment",
              "Aggregating news sentiment to daily signals",
              "Earnings call sentiment analysis"],
             ["News sentiment signal construction",
              "FinBERT sentiment scoring example"]),
            ("Web Scraping for Fundamental Data",
             ["BeautifulSoup and requests for HTML scraping",
              "SEC EDGAR for filings",
              "Robots.txt and ethical scraping",
              "Rate limiting and caching"],
             ["Scrape SEC EDGAR for 10-K filings list",
              "Parse key financial metrics from HTML"]),
            ("Alternative Data Alpha Generation",
             ["Signal construction pipeline",
              "Backtesting alt data signals",
              "Combining alt data with price signals",
              "Evaluating information coefficient (IC)"],
             ["IC computation for alt data signal",
              "Alt data backtest framework"]),
        ],
    ),
    (
        "module_12_advanced_topics_research",
        "12_2_factor_investing.ipynb",
        "Module 12.2 — Factor Investing",
        "Fama–French, Momentum, Quality, Low Volatility, and Multi-Factor Models",
        """\
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
from scipy import stats
import warnings; warnings.filterwarnings('ignore')

np.random.seed(42)
plt.style.use('seaborn-v0_8-darkgrid')
print("Module 12.2 environment ready.")""",
        [
            ("Factor Zoo Overview",
             ["What is a risk factor vs an anomaly?",
              "Fama-French 3-factor and 5-factor models",
              "Classic factors: value, size, momentum, quality, low vol",
              "Factor replication and data sources"],
             ["Download and replicate FF3 factors",
              "Factor return time series analysis"]),
            ("Factor Construction",
             ["Cross-sectional ranking and z-scoring",
              "Long-short factor portfolio construction",
              "Neutralization: market, sector, country",
              "Rebalancing frequency and turnover"],
             ["Construct a momentum factor from price data",
              "Long-short factor portfolio construction"]),
            ("Factor Backtesting",
             ["IC (information coefficient) and ICIR",
              "Quintile analysis",
              "Factor alpha vs factor beta",
              "Turnover and transaction costs"],
             ["Quintile return analysis",
              "IC time series and ICIR computation"]),
            ("Multi-Factor Models",
             ["Combining factors: equal weight vs optimized",
              "Factor timing: when does each factor work?",
              "Smart beta strategies",
              "Factor crowding and capacity constraints"],
             ["Multi-factor score construction",
              "Factor combination backtest"]),
        ],
    ),
    (
        "module_12_advanced_topics_research",
        "12_3_portfolio_construction_techniques.ipynb",
        "Module 12.3 — Advanced Portfolio Construction",
        "Equal Weight, Minimum Variance, Maximum Diversification, and Risk Parity",
        """\
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import minimize
import warnings; warnings.filterwarnings('ignore')

np.random.seed(42)
plt.style.use('seaborn-v0_8-darkgrid')
print("Module 12.3 environment ready.")""",
        [
            ("Equal Weighting and Cap Weighting",
             ["Simplicity and robustness of equal weighting",
              "Cap weighting: momentum bias and concentration",
              "Rebalancing costs",
              "When equal weighting beats cap weighting"],
             ["Compare equal weight vs cap weight historically",
              "Rebalancing cost analysis"]),
            ("Minimum Variance and Maximum Diversification",
             ["Minimum variance portfolio (MVP)",
              "Maximum diversification ratio",
              "Diversification ratio: weighted average vol / portfolio vol",
              "Sensitivity to covariance estimation"],
             ["MVP via scipy.optimize",
              "Maximum diversification portfolio"]),
            ("Risk Parity",
             ["Equal risk contribution (ERC) portfolio",
              "Risk budgeting: allocate risk, not capital",
              "Volatility scaling in risk parity",
              "Leverage and risk parity"],
             ["ERC portfolio implementation",
              "Risk contribution decomposition"]),
            ("Hierarchical Risk Parity (HRP)",
             ["Motivation: instability of Markowitz optimization",
              "HRP algorithm: linkage, quasi-diagonalization, allocation",
              "Comparison to ERC and MVP",
              "HRP with different linkage methods"],
             ["HRP implementation from scratch",
              "HRP vs Markowitz comparison"]),
        ],
    ),
    (
        "module_12_advanced_topics_research",
        "12_4_market_neutral_strategies.ipynb",
        "Module 12.4 — Market Neutral Strategies",
        "Long-Short Equity, Statistical Arbitrage, Factor Neutrality, and Beta Hedging",
        """\
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
from scipy import stats
import warnings; warnings.filterwarnings('ignore')

np.random.seed(42)
plt.style.use('seaborn-v0_8-darkgrid')
print("Module 12.4 environment ready.")""",
        [
            ("Long-Short Equity",
             ["Dollar neutral vs beta neutral",
              "Gross and net exposure",
              "Long-short factor portfolios",
              "Leverage and margin requirements"],
             ["Construct dollar-neutral long-short portfolio",
              "Gross/net exposure monitor"]),
            ("Statistical Arbitrage",
             ["Pairs trading with cointegration",
              "Spread z-score entry/exit signals",
              "Ornstein-Uhlenbeck process for spread",
              "Multi-pair statistical arbitrage"],
             ["Pairs trading backtest",
              "OU half-life estimation"]),
            ("Factor Neutrality",
             ["Beta neutralization",
              "Sector and industry neutralization",
              "Factor exposure hedging",
              "Residual alpha extraction"],
             ["Beta-neutral portfolio construction",
              "Factor exposure dashboard"]),
            ("Dynamic Hedging",
             ["Rolling beta estimation",
              "Hedge ratio stability over time",
              "Hedge instruments: ETFs, futures, options",
              "Hedging costs and drag"],
             ["Dynamic beta hedge implementation",
              "Hedge effectiveness measurement"]),
        ],
    ),

    # ── Module 13 ───────────────────────────────────────────────────────────
    (
        "module_13_llm_quantitative_finance",
        "13_1_llm_fundamentals_for_finance.ipynb",
        "Module 13.1 — LLM Fundamentals for Finance",
        "Transformer Architecture, Prompt Engineering, and Model Selection",
        """\
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import json
import warnings; warnings.filterwarnings('ignore')

# LLM imports (uncomment when API keys are configured)
# import anthropic
# from anthropic import Anthropic

print("Module 13.1 environment ready.")
print("Note: LLM cells require API keys (Anthropic / OpenAI).")""",
        [
            ("Understanding Transformer Architecture",
             ["Self-attention mechanism",
              "Encoder-decoder vs decoder-only models",
              "Tokenization and vocabulary",
              "Context window and token limits"],
             ["Tokenize a financial news headline",
              "Estimate token cost for document batch"]),
            ("Pre-Trained Models vs Fine-Tuning",
             ["Zero-shot and few-shot prompting",
              "Fine-tuning vs prompt engineering trade-offs",
              "Domain-specific models: FinBERT, BloombergGPT",
              "When to fine-tune vs prompt"],
             ["Few-shot sentiment classifier",
              "Model comparison on financial text"]),
            ("Prompt Engineering for Financial Tasks",
             ["System prompts and instruction following",
              "Chain-of-thought for financial reasoning",
              "Structured output: JSON extraction",
              "Hallucination mitigation strategies"],
             ["Structured JSON extraction from earnings text",
              "Chain-of-thought financial analysis prompt"]),
            ("Model Selection and Cost Optimization",
             ["GPT-4 vs Claude vs open-source models",
              "Latency, throughput, and cost trade-offs",
              "Caching and prompt compression",
              "Batch API for high-volume processing"],
             ["Cost estimator for LLM pipeline",
              "Caching layer implementation sketch"]),
        ],
    ),
    (
        "module_13_llm_quantitative_finance",
        "13_2_sentiment_analysis_news_processing.ipynb",
        "Module 13.2 — Sentiment Analysis and News Processing",
        "NLP Pipelines, FinBERT, News Signals, and Earnings Call Analysis",
        """\
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import re
import warnings; warnings.filterwarnings('ignore')

# NLP imports
from textblob import TextBlob  # pip install textblob

# FinBERT (uncomment when available)
# from transformers import pipeline
# sentiment_pipeline = pipeline("text-classification", model="ProsusAI/finbert")

print("Module 13.2 environment ready.")""",
        [
            ("Traditional vs LLM-Based Sentiment",
             ["VADER: rule-based sentiment for social media",
              "TextBlob: simple polarity scoring",
              "FinBERT: fine-tuned BERT for finance",
              "Comparison on financial headlines"],
             ["VADER vs TextBlob vs FinBERT on same headlines",
              "Calibration: sentiment score vs forward returns"]),
            ("News Feed Processing Pipeline",
             ["News sources: Reuters, Bloomberg, EDGAR",
              "Article deduplication and normalization",
              "Entity extraction: company, person, metric",
              "Aggregating to daily sentiment scores"],
             ["Build a mock news sentiment pipeline",
              "Entity extraction with spaCy"]),
            ("Earnings Call Transcript Analysis",
             ["MD&A tone analysis",
              "Management guidance extraction",
              "Sentiment vs subsequent price reaction",
              "Red flag language detection"],
             ["Earnings call sentiment scorer",
              "Forward return correlation analysis"]),
            ("Social Media Sentiment",
             ["Twitter/X and Reddit for retail sentiment",
              "WSB (WallStreetBets) signal construction",
              "Noise filtering and smoothing",
              "Contrarian vs momentum use of sentiment"],
             ["Reddit sentiment aggregation pipeline",
              "Sentiment signal backtest"]),
        ],
    ),
    (
        "module_13_llm_quantitative_finance",
        "13_3_financial_document_analysis.ipynb",
        "Module 13.3 — Financial Document Analysis",
        "SEC Filings, 10-K/10-Q Extraction, Risk Factors, and Change Detection",
        """\
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import requests
import json
import re
import warnings; warnings.filterwarnings('ignore')

print("Module 13.3 environment ready.")
print("Note: LLM extraction cells require API keys.")""",
        [
            ("SEC EDGAR Data Access",
             ["EDGAR full-text search API",
              "Fetching 10-K, 10-Q, and 8-K filings",
              "Parsing HTML and XBRL formats",
              "Building a filing database"],
             ["Fetch recent 10-K for a given CIK",
              "Extract key sections from 10-K HTML"]),
            ("Automated 10-K Summarization",
             ["LLM-based section summarization",
              "Business description, risk factors, MD&A",
              "Structured extraction: revenue, margins, guidance",
              "Multi-year comparison"],
             ["10-K summarization prompt",
              "Year-over-year MD&A comparison"]),
            ("Risk Factor Identification",
             ["Extracting and categorizing risk factors",
              "Risk factor change detection across filings",
              "Materiality scoring",
              "ESG risk factors"],
             ["Risk factor extractor",
              "Risk change detection between two 10-Ks"]),
            ("Building a Document Intelligence Pipeline",
             ["Chunking long documents for LLM context",
              "Retrieval-augmented generation (RAG) overview",
              "Embedding-based similarity search",
              "Alert system for material changes"],
             ["Document chunking and embedding",
              "Material change alert system sketch"]),
        ],
    ),
    (
        "module_13_llm_quantitative_finance",
        "13_4_fundamental_analysis_automation.ipynb",
        "Module 13.4 — Fundamental Analysis Automation",
        "Financial Ratios, Peer Comparison, and LLM-Powered Analysis",
        """\
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import warnings; warnings.filterwarnings('ignore')

print("Module 13.4 environment ready.")""",
        [
            ("Financial Ratio Computation",
             ["Valuation: P/E, P/B, EV/EBITDA, P/S",
              "Profitability: ROE, ROA, ROIC, margins",
              "Leverage: debt/equity, interest coverage",
              "Liquidity: current ratio, quick ratio"],
             ["Financial ratio calculator from income/balance sheet",
              "Ratio trend analysis"]),
            ("Peer Comparison and Benchmarking",
             ["Industry median normalization",
              "Percentile ranking within sector",
              "Relative valuation models",
              "Peer group selection methodology"],
             ["Peer comparison table generator",
              "Sector relative valuation"]),
            ("LLM-Powered Investment Thesis Generation",
             ["Structuring investment memos with LLMs",
              "Bull/bear case generation",
              "Synthesizing quantitative and qualitative signals",
              "Limitations: hallucination and stale knowledge"],
             ["Investment memo prompt template",
              "Bull-bear case generator"]),
            ("Financial Health Scoring",
             ["Altman Z-score for distress prediction",
              "Piotroski F-score for quality",
              "Custom composite health score",
              "Backtesting health scores as signals"],
             ["Altman Z-score implementation",
              "Piotroski F-score calculator"]),
        ],
    ),
    (
        "module_13_llm_quantitative_finance",
        "13_5_trading_strategy_generation.ipynb",
        "Module 13.5 — Trading Strategy Generation and Research",
        "LLM-Assisted Ideation, Hypothesis Testing, and Research Automation",
        """\
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import warnings; warnings.filterwarnings('ignore')

print("Module 13.5 environment ready.")""",
        [
            ("LLM for Strategy Ideation",
             ["Brainstorming anomalies and signals",
              "Converting narrative ideas to testable hypotheses",
              "Literature review automation",
              "Avoiding data mining bias in LLM suggestions"],
             ["Strategy ideation prompt framework",
              "Hypothesis formalization template"]),
            ("Research Paper Summarization",
             ["Academic finance papers as signal sources",
              "Extracting key findings and methodologies",
              "Replication checklist generation",
              "Building a research knowledge base"],
             ["Paper summarization pipeline",
              "Replication checklist generator"]),
            ("Pattern Recognition and Anomaly Narratives",
             ["LLM explanation of detected statistical patterns",
              "Regime narrative generation",
              "Anomaly description for risk managers",
              "Automated research reports"],
             ["Pattern explanation prompt",
              "Automated strategy documentation"]),
        ],
    ),
    (
        "module_13_llm_quantitative_finance",
        "13_6_code_generation_debugging.ipynb",
        "Module 13.6 — Code Generation and Debugging with LLMs",
        "Strategy Coding, Review, Documentation, and Test Generation",
        """\
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import warnings; warnings.filterwarnings('ignore')

print("Module 13.6 environment ready.")""",
        [
            ("LLM-Assisted Strategy Coding",
             ["Translating strategy descriptions to Python",
              "Iterative code refinement with LLM",
              "Converting Pine Script / MQL to Python",
              "Code quality and edge case handling"],
             ["Strategy description to code prompt",
              "Pine Script to Python conversion example"]),
            ("Code Review and Optimization",
             ["LLM for identifying bugs and inefficiencies",
              "Vectorization suggestions",
              "Memory and performance optimization",
              "Security review for trading code"],
             ["Code review prompt template",
              "Performance optimization example"]),
            ("Documentation and Test Generation",
             ["Auto-generating docstrings",
              "Unit test generation for trading functions",
              "Backtest documentation automation",
              "Changelog and version notes"],
             ["Docstring generator prompt",
              "Unit test generator for a strategy function"]),
        ],
    ),
    (
        "module_13_llm_quantitative_finance",
        "13_7_risk_narrative_reporting.ipynb",
        "Module 13.7 — Risk Narrative and Automated Reporting",
        "Portfolio Summaries, Risk Reports, Performance Commentary, and Client Communication",
        """\
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import warnings; warnings.filterwarnings('ignore')

print("Module 13.7 environment ready.")""",
        [
            ("Automated Portfolio Summaries",
             ["Daily P&L narrative generation",
              "Position change explanations",
              "Key driver identification",
              "Tone calibration for different audiences"],
             ["Daily portfolio summary generator",
              "Key driver narrative prompt"]),
            ("Risk Report Generation",
             ["VaR and CVaR narrative",
              "Drawdown explanation",
              "Stress test scenario narratives",
              "Regulatory-ready language"],
             ["Risk report template generator",
              "Drawdown explanation prompt"]),
            ("Performance Attribution Commentary",
             ["Factor attribution narrative",
              "Strategy vs benchmark comparison",
              "Client-facing performance explanation",
              "Avoiding misleading narratives"],
             ["Attribution commentary generator",
              "Client report template"]),
        ],
    ),
    (
        "module_13_llm_quantitative_finance",
        "13_8_market_intelligence_research.ipynb",
        "Module 13.8 — Market Intelligence and Research Automation",
        "Macro Analysis, Central Bank Communication, and Geopolitical Risk",
        """\
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import requests
import warnings; warnings.filterwarnings('ignore')

print("Module 13.8 environment ready.")""",
        [
            ("Central Bank Communication Analysis",
             ["Fed statement hawkish/dovish scoring",
              "FOMC minute analysis",
              "ECB and BoE communication",
              "Rate path inference from language"],
             ["Fed statement analyzer",
              "Hawkish/dovish score tracker"]),
            ("Geopolitical Risk Monitoring",
             ["News-based geopolitical risk index",
              "Event classification: trade war, sanctions, conflict",
              "Asset class impact mapping",
              "Early warning signal construction"],
             ["Geopolitical event classifier",
              "Risk index construction"]),
            ("Macro Regime Classification",
             ["Growth vs recession narrative signals",
              "Inflation regime language detection",
              "Cross-asset macro signal synthesis",
              "Macro regime to asset allocation mapping"],
             ["Macro regime classifier",
              "Asset allocation recommendation generator"]),
        ],
    ),
    (
        "module_13_llm_quantitative_finance",
        "13_9_conversational_trading_assistants.ipynb",
        "Module 13.9 — Conversational Trading Assistants",
        "Portfolio Chatbots, Natural Language Interfaces, and Educational Bots",
        """\
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import json
import warnings; warnings.filterwarnings('ignore')

print("Module 13.9 environment ready.")
print("Note: chatbot cells require LLM API keys.")""",
        [
            ("Building a Portfolio Q&A Chatbot",
             ["Conversation state management",
              "Grounding answers in live portfolio data",
              "Handling ambiguous queries",
              "Fallback and escalation logic"],
             ["Portfolio Q&A chatbot skeleton",
              "Conversation state manager"]),
            ("Natural Language Query Interface",
             ["NL to SQL for portfolio database queries",
              "NL to pandas for data analysis",
              "Query validation and safety",
              "Result formatting for non-technical users"],
             ["NL to pandas query converter",
              "Query result formatter"]),
            ("Compliance Assistant",
             ["Trade pre-approval chatbot",
              "Regulatory Q&A grounding on rulebook",
              "Audit trail for LLM decisions",
              "Limitations and human oversight"],
             ["Compliance Q&A bot skeleton",
              "Decision audit logger"]),
        ],
    ),
    (
        "module_13_llm_quantitative_finance",
        "13_10_advanced_llm_techniques.ipynb",
        "Module 13.10 — Advanced LLM Techniques",
        "RAG, Fine-Tuning, Embeddings, Agents, and Multi-Agent Systems",
        """\
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import json
import warnings; warnings.filterwarnings('ignore')

# Embedding / RAG imports (uncomment when available)
# import anthropic
# from anthropic import Anthropic

print("Module 13.10 environment ready.")""",
        [
            ("Retrieval-Augmented Generation (RAG)",
             ["Motivation: grounding LLMs in proprietary data",
              "Architecture: retriever + reader",
              "Chunking, embedding, and vector store",
              "Query expansion and re-ranking"],
             ["RAG pipeline for financial documents",
              "Semantic search over research reports"]),
            ("Fine-Tuning for Finance",
             ["When fine-tuning beats prompting",
              "LoRA and PEFT for efficient fine-tuning",
              "Fine-tuning FinBERT on custom sentiment data",
              "Evaluation and overfitting"],
             ["Fine-tuning data preparation pipeline",
              "Fine-tuning evaluation framework"]),
            ("Embeddings for Semantic Search",
             ["Text embeddings and cosine similarity",
              "Clustering documents with embeddings",
              "Hybrid search: keyword + semantic",
              "Vector databases: ChromaDB, Pinecone, pgvector"],
             ["Embed and cluster earnings call summaries",
              "Semantic search over financial documents"]),
            ("LLM Agents and Tool Use",
             ["Agent architectures: ReAct, plan-and-execute",
              "Tool calling: APIs, databases, calculators",
              "Multi-agent collaboration for research",
              "Safety and guardrails for financial agents"],
             ["Single agent with financial tools",
              "Multi-agent research system sketch"]),
        ],
    ),
    (
        "module_13_llm_quantitative_finance",
        "13_11_llm_enhanced_alpha_generation.ipynb",
        "Module 13.11 — LLM-Enhanced Alpha Generation",
        "Alternative Data Processing, Narrative Factors, and Hybrid Quant-LLM Models",
        """\
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import warnings; warnings.filterwarnings('ignore')

print("Module 13.11 environment ready.")""",
        [
            ("Unstructured Data Alpha Extraction",
             ["NLP pipeline from raw text to signal",
              "Signal decay: how quickly does text alpha erode?",
              "Coverage and frequency considerations",
              "IC and ICIR for text-based signals"],
             ["Text-to-signal pipeline",
              "Signal IC measurement"]),
            ("Narrative Momentum Indicators",
             ["Tracking narrative shifts over time",
              "Narrative momentum vs price momentum",
              "Combining text and price signals",
              "Narrative crowding and mean reversion"],
             ["Narrative momentum signal construction",
              "Narrative vs price momentum comparison"]),
            ("LLM-Based Factor Construction",
             ["LLM-derived quality scores from text",
              "Management credibility factor",
              "Innovation narrative factor",
              "Backtesting LLM-derived factors"],
             ["LLM quality score factor",
              "LLM factor backtest"]),
        ],
    ),
    (
        "module_13_llm_quantitative_finance",
        "13_12_ethics_bias_limitations.ipynb",
        "Module 13.12 — Ethics, Bias, and Limitations of LLMs in Finance",
        "Hallucination, Bias Detection, Regulatory Considerations, and Responsible AI",
        """\
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import warnings; warnings.filterwarnings('ignore')

print("Module 13.12 environment ready.")""",
        [
            ("Hallucination Risks in Finance",
             ["What is hallucination and why it is dangerous in finance",
              "Hallucination in numerical claims",
              "Detection strategies: grounding and verification",
              "Human-in-the-loop requirements"],
             ["Hallucination detection test suite",
              "Fact-checking pipeline sketch"]),
            ("Bias in LLM Outputs",
             ["Training data bias and financial implications",
              "Sentiment bias toward large-cap stocks",
              "Geographic and language bias",
              "Debiasing strategies"],
             ["Bias detection in sentiment scores",
              "Coverage analysis across market caps"]),
            ("Regulatory Considerations",
             ["MiFID II and AI-assisted advice",
              "SEC guidance on AI in investment decisions",
              "Explainability requirements",
              "Model documentation and governance"],
             ["Model card template for LLM application",
              "Compliance checklist for AI in trading"]),
            ("Responsible AI Framework",
             ["Human oversight and override mechanisms",
              "Audit trails for LLM decisions",
              "A/B testing LLM vs traditional methods",
              "Continuous monitoring for model drift"],
             ["Human oversight framework",
              "LLM decision audit logger"]),
        ],
    ),
    (
        "module_13_llm_quantitative_finance",
        "13_13_production_llm_systems.ipynb",
        "Module 13.13 — Production LLM Systems",
        "Caching, Rate Limiting, Async Processing, Monitoring, and Cost Management",
        """\
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import asyncio
import time
import json
import hashlib
import warnings; warnings.filterwarnings('ignore')

print("Module 13.13 environment ready.")""",
        [
            ("Caching Strategies",
             ["Semantic caching: cache by embedding similarity",
              "Exact-match caching with hashing",
              "Cache invalidation policies",
              "Cost savings from caching"],
             ["Hash-based cache implementation",
              "Cache hit rate measurement"]),
            ("Rate Limiting and Cost Management",
             ["Token budget management",
              "Request queuing and throttling",
              "Cost monitoring dashboard",
              "Model routing: cheap vs expensive model tiers"],
             ["Rate limiter implementation",
              "Cost tracker with budget alerts"]),
            ("Asynchronous Processing",
             ["asyncio for concurrent LLM calls",
              "Batch API for high-volume processing",
              "Task queues with Celery / RQ",
              "Streaming responses for low-latency UX"],
             ["Async LLM call wrapper",
              "Batch processing pipeline"]),
            ("Monitoring and Reliability",
             ["Latency and throughput monitoring",
              "Error rate tracking",
              "Fallback to alternative model on failure",
              "A/B testing different models or prompts"],
             ["LLM monitoring dashboard sketch",
              "Fallback chain implementation"]),
        ],
    ),
    (
        "module_13_llm_quantitative_finance",
        "13_14_case_studies.ipynb",
        "Module 13.14 — Case Studies and Real-World Applications",
        "Hedge Fund Workflows, Research Automation, and End-to-End LLM Systems",
        """\
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import warnings; warnings.filterwarnings('ignore')

print("Module 13.14 environment ready.")""",
        [
            ("Hedge Fund LLM Workflows",
             ["Systematic equity research automation",
              "Event-driven trading with NLP signals",
              "Earnings surprise prediction",
              "Analyst note processing pipeline"],
             ["Earnings surprise prediction pipeline",
              "Analyst note sentiment aggregator"]),
            ("Asset Management Applications",
             ["ESG scoring automation",
              "Client portfolio explainer",
              "Regulatory filing monitor",
              "Investment memo generation"],
             ["ESG score generator",
              "Client explainer system"]),
            ("End-to-End LLM-Enhanced Trading System",
             ["System architecture: data ingestion to signal to execution",
              "Integrating LLM signals with quantitative models",
              "Risk management for LLM-generated signals",
              "Performance attribution across LLM vs quant components"],
             ["System architecture diagram",
              "LLM signal integration with quant model"]),
        ],
    ),

    # ── Module 14 ───────────────────────────────────────────────────────────
    (
        "module_14_capstone_projects",
        "14_1_momentum_strategy.ipynb",
        "Capstone 1 — End-to-End Momentum Strategy",
        "Data Ingestion, Signal Generation, Backtesting, and Paper Trading",
        """\
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import warnings; warnings.filterwarnings('ignore')

np.random.seed(42)
plt.style.use('seaborn-v0_8-darkgrid')
print("Capstone 1 environment ready.")""",
        [
            ("Project Overview and Objectives",
             ["Build a complete momentum strategy from scratch",
              "Cover: data, signal, backtest, risk management, paper trading",
              "Deliverable: live (or paper) deployable strategy"],
             ["Define universe and data sources",
              "Set performance targets and risk budget"]),
            ("Data Pipeline",
             ["Download price data for chosen universe",
              "Adjust for splits and dividends",
              "Handle missing data and survivorship"],
             ["Build data pipeline",
              "Data quality checks"]),
            ("Signal Generation",
             ["Cross-sectional momentum: rank assets by past returns",
              "Time-series momentum: trend following per asset",
              "Signal combination and normalization"],
             ["Momentum signal construction",
              "Signal IC analysis"]),
            ("Backtesting and Risk Management",
             ["Full backtest with transaction costs",
              "Position sizing with volatility targeting",
              "Drawdown controls and stop-losses"],
             ["Backtest with full cost model",
              "Risk management layer"]),
            ("Paper Trading Deployment",
             ["Connect to broker paper trading account",
              "Monitor live performance vs backtest",
              "Ongoing signal monitoring dashboard"],
             ["Paper trading deployment script",
              "Performance monitoring dashboard"]),
        ],
    ),
    (
        "module_14_capstone_projects",
        "14_2_ml_factor_model.ipynb",
        "Capstone 2 — Machine Learning Factor Model",
        "Feature Engineering, ML Signal, Validation, and Portfolio Construction",
        """\
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import TimeSeriesSplit
import warnings; warnings.filterwarnings('ignore')

np.random.seed(42)
plt.style.use('seaborn-v0_8-darkgrid')
print("Capstone 2 environment ready.")""",
        [
            ("Project Overview",
             ["Build a multi-factor ML stock selection model",
              "Cover: feature engineering, model training, walk-forward validation",
              "Deliverable: ranked stock selection model with live signal"],
             ["Define feature universe",
              "Set validation framework"]),
            ("Feature Engineering",
             ["Price-based features: momentum, mean reversion, volatility",
              "Fundamental features: value, quality, growth",
              "Technical indicators as features",
              "Feature normalization and winsorization"],
             ["Feature matrix construction",
              "Feature correlation analysis"]),
            ("ML Model Training and Validation",
             ["RandomForest / XGBoost for cross-sectional prediction",
              "Walk-forward training and validation",
              "Feature importance analysis",
              "Overfitting detection"],
             ["Walk-forward ML model training",
              "Feature importance visualization"]),
            ("Portfolio Construction from ML Signal",
             ["Long-short quintile portfolio",
              "Transaction cost-aware portfolio construction",
              "Risk neutralization: market, sector",
              "Live signal generation pipeline"],
             ["ML factor portfolio construction",
              "Live ranking signal"]),
        ],
    ),
    (
        "module_14_capstone_projects",
        "14_3_options_volatility_strategy.ipynb",
        "Capstone 3 — Options Volatility Strategy",
        "Delta-Neutral Positioning, Volatility Forecasting, and Dynamic Hedging",
        """\
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm
from math import log, sqrt, exp
import warnings; warnings.filterwarnings('ignore')

np.random.seed(42)
plt.style.use('seaborn-v0_8-darkgrid')
print("Capstone 3 environment ready.")""",
        [
            ("Project Overview",
             ["Build a delta-neutral options strategy trading realized vs implied vol",
              "Cover: vol forecasting, position construction, Greeks management",
              "Deliverable: backtested vol trading strategy"],
             ["Strategy design document",
              "Universe and instrument selection"]),
            ("Volatility Forecasting",
             ["GARCH(1,1) realized vol forecasting",
              "HAR model for realized variance",
              "Implied vol as market forecast benchmark",
              "Forecasting accuracy evaluation"],
             ["GARCH vol forecaster",
              "HAR model implementation"]),
            ("Position Construction",
             ["Identify realized vs implied vol divergence",
              "Straddle / strangle position sizing",
              "Delta hedging to neutralize directional risk",
              "Vega exposure management"],
             ["Vol divergence signal",
              "Delta-neutral position construction"]),
            ("Backtesting and Greeks Management",
             ["Daily delta re-hedging simulation",
              "P&L decomposition: delta, gamma, theta, vega",
              "Transaction cost impact on vol strategies",
              "Risk management: vega limits, max loss"],
             ["Full vol strategy backtest",
              "Greeks P&L attribution"]),
        ],
    ),
    (
        "module_14_capstone_projects",
        "14_4_multi_asset_portfolio_system.ipynb",
        "Capstone 4 — Multi-Asset Portfolio System",
        "Cross-Asset Allocation, Risk Parity, and Dynamic Rebalancing",
        """\
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import minimize
import warnings; warnings.filterwarnings('ignore')

np.random.seed(42)
plt.style.use('seaborn-v0_8-darkgrid')
print("Capstone 4 environment ready.")""",
        [
            ("Project Overview",
             ["Build a multi-asset portfolio system: equities, bonds, commodities",
              "Cover: asset class selection, optimization, rebalancing",
              "Deliverable: production-ready allocation system"],
             ["Asset class universe definition",
              "Data sourcing for each asset class"]),
            ("Asset Class Return Modeling",
             ["Return and risk estimation per asset class",
              "Cross-asset correlation structure",
              "Regime-conditional covariance estimates",
              "Factor model for multi-asset universe"],
             ["Multi-asset return and covariance estimation",
              "Cross-asset correlation heatmap"]),
            ("Portfolio Optimization",
             ["Risk parity allocation",
              "Mean-variance with asset class constraints",
              "Black-Litterman with macro views",
              "Comparing allocation methods"],
             ["Risk parity optimizer",
              "Black-Litterman implementation"]),
            ("Rebalancing and Implementation",
             ["Threshold-based rebalancing",
              "Transaction cost-aware rebalancing",
              "Tax-aware rebalancing (for taxable accounts)",
              "Drift monitoring and alerts"],
             ["Rebalancing engine",
              "Full backtest with rebalancing costs"]),
        ],
    ),
    (
        "module_14_capstone_projects",
        "14_5_personal_trading_infrastructure.ipynb",
        "Capstone 5 — Personal Trading Infrastructure",
        "Data Pipelines, Backtesting Engine, Paper Trading, Monitoring, and Live Deployment",
        """\
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import logging
import json
import warnings; warnings.filterwarnings('ignore')

np.random.seed(42)
plt.style.use('seaborn-v0_8-darkgrid')
print("Capstone 5 environment ready.")""",
        [
            ("Project Overview",
             ["Build a complete personal trading infrastructure",
              "Components: data pipeline, backtester, paper trading, monitoring",
              "Deliverable: production-ready trading system"],
             ["System architecture design",
              "Component dependency diagram"]),
            ("Data Pipeline",
             ["Market data ingestion (yfinance / Polygon / Alpaca)",
              "Data storage and versioning",
              "Feature engineering pipeline",
              "Daily automated data refresh"],
             ["Automated data pipeline",
              "Feature store implementation"]),
            ("Backtesting Engine",
             ["Event-driven backtest framework",
              "Strategy plug-in architecture",
              "Performance reporting",
              "Parameter optimization module"],
             ["Backtesting engine core",
              "Strategy runner with reporting"]),
            ("Paper Trading and Live Deployment",
             ["Broker integration (Alpaca / IBKR)",
              "Risk controls layer",
              "Monitoring dashboard",
              "Kill switch and emergency procedures"],
             ["Full paper trading system",
              "Risk controls and monitoring"]),
        ],
    ),
    (
        "module_14_capstone_projects",
        "14_6_llm_trading_research_assistant.ipynb",
        "Capstone 6 — LLM-Powered Trading Research Assistant",
        "News Processing, Earnings Analysis, Sentiment Signals, and Automated Research Reports",
        """\
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import json
import warnings; warnings.filterwarnings('ignore')

print("Capstone 6 environment ready.")
print("Note: LLM cells require API keys.")""",
        [
            ("Project Overview",
             ["Build an end-to-end LLM research assistant",
              "Components: news pipeline, earnings analyzer, signal generator, report writer",
              "Deliverable: automated daily research report with backtested signals"],
             ["System design and component map",
              "Data source selection"]),
            ("News and Sentiment Pipeline",
             ["Real-time news ingestion",
              "LLM-based sentiment scoring",
              "Entity extraction and company mapping",
              "Daily sentiment signal construction"],
             ["News sentiment pipeline",
              "Sentiment signal aggregation"]),
            ("Earnings Call Analyzer",
             ["Transcript ingestion and preprocessing",
              "LLM tone and guidance extraction",
              "Surprise vs expectation scoring",
              "Post-earnings price reaction study"],
             ["Earnings analyzer pipeline",
              "Surprise score backtest"]),
            ("Automated Research Report Generation",
             ["Daily market summary generation",
              "Key signal highlights narrative",
              "Risk and opportunity identification",
              "Client-ready formatting"],
             ["Report generator pipeline",
              "End-to-end system integration"]),
        ],
    ),
]


def make_skeleton_notebook(module_title, subtitle, imports, sections, next_module=""):
    cells = []

    # ── Header ──────────────────────────────────────────────────────────────
    toc_lines = "\n".join(
        f"{i+1}. **{s[0]}**" for i, s in enumerate(sections)
    )
    header = f"""\
# {module_title}
## {subtitle}

---

### Learning Objectives

By the end of this notebook you will be able to:

{toc_lines}

---
"""
    cells.append(md_cell(header))

    # ── Setup ────────────────────────────────────────────────────────────────
    cells.append(code_cell(imports))

    # ── Sections ─────────────────────────────────────────────────────────────
    for i, (title, theory, practice) in enumerate(sections, 1):
        theory_lines = "\n".join(f"- {t}" for t in theory)
        practice_lines = "\n".join(f"- {p}" for p in practice)

        section_md = f"""\
---

## {i}. {title}

### Theory

{theory_lines}

---

### Practice

{practice_lines}
"""
        cells.append(md_cell(section_md))
        cells.append(code_cell(f"# TODO: {title}\n# Implement the practice exercises above\n"))

    # ── Closing ──────────────────────────────────────────────────────────────
    section_summary = "\n".join(
        f"| **{s[0]}** | {s[2][0] if s[2] else '—'} |"
        for s in sections
    )
    next_line = f"\n---\n*Next: {next_module}*" if next_module else ""

    closing = f"""\
---

## Closing Reflection

| Section | Key Practice |
|---------|-------------|
{section_summary}

---

### Looking Ahead

Continue building on these concepts in the next notebook.
{next_line}
"""
    cells.append(md_cell(closing))

    return make_notebook(cells)


# ---------------------------------------------------------------------------
# Generate all notebooks
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    print(f"Generating skeleton notebooks in: {os.path.abspath(NOTEBOOKS_DIR)}\n")
    created = 0
    for entry in MODULES:
        module_dir, filename, title, subtitle, imports, sections = entry
        path = os.path.join(NOTEBOOKS_DIR, module_dir, filename)
        nb = make_skeleton_notebook(title, subtitle, imports, sections)
        write_notebook(path, nb)
        created += 1
    print(f"\nDone — {created} notebooks created.")

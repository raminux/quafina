# Table of Contents

## Completed Modules

---

## Module 1: Mathematical Foundations for Quantitative Finance

### [1.1 Probability Theory & Statistics](notebooks/module_01_math/1_1_Enhanced_Probability_Statistics.ipynb)
**Theory:**
- Probability spaces, random variables, and distributions
- Expected value, variance, moments, and cumulants
- Joint distributions, covariance, and correlation
- Central Limit Theorem and Law of Large Numbers
- Hypothesis testing and statistical inference

**Practice:**
- Simulating distributions in Python (NumPy)
- Monte Carlo methods for probability estimation
- Statistical testing of trading hypotheses
- Correlation analysis of asset returns

### [1.2 Linear Algebra for Finance](notebooks/module_01_math/1_2_linear_algebra_for_finance.ipynb)
**Theory:**
- Vectors, matrices, and matrix operations
- Eigenvalues, eigenvectors, and PCA
- Optimization and quadratic forms
- Covariance matrices in portfolio theory

**Practice:**
- Portfolio optimization using matrix algebra
- Principal Component Analysis for risk factors
- Dimensionality reduction for trading signals
- Implementing efficient frontier calculations

### [1.3 Calculus & Differential Equations](notebooks/module_01_math/1_3_calculus_diff_equations.ipynb)
**Theory:**
- Derivatives and partial derivatives
- Taylor series and approximations
- Stochastic calculus basics (Ito's Lemma)
- Ordinary and partial differential equations

**Practice:**
- Option Greeks calculation
- Numerical solutions to Black-Scholes PDE
- Time series analysis with derivatives
- Duration and convexity for bonds

---

## Module 2: Financial Markets Fundamentals

### [2.1 Market Microstructure](notebooks/module_02_financial_markets_fundamentals/2_1_market_microstructure.ipynb)
**Theory:**
- Order types (market, limit, stop, iceberg)
- Order books and price formation
- Bid-ask spread and market impact
- Market makers vs. takers
- High-frequency trading basics
- Dark pools and alternative venues

**Practice:**
- Analyzing Level 2 order book data
- Calculating effective spreads and slippage
- Simulating order execution strategies
- Market impact models implementation

### [2.2 Asset Classes Deep Dive](notebooks/module_02_financial_markets_fundamentals/2_2_asset_classes.ipynb)
**Theory:**
- Equities: stocks, indices, ETFs
- Fixed income: bonds, treasuries, yield curves
- Derivatives: options, futures, swaps
- Foreign exchange (FX) markets
- Commodities and alternative assets
- Cryptocurrencies and digital assets

**Practice:**
- Fetching and analyzing data for each asset class
- Building pricing models for different instruments
- Cross-asset correlation analysis
- Multi-asset portfolio construction

### [2.3 Market Data & Infrastructure](notebooks/module_02_financial_markets_fundamentals/2_3_market_data_infrastructure.ipynb)
**Theory:**
- Types of market data (tick, bar, fundamental)
- Data vendors and APIs (Bloomberg, Reuters, Polygon)
- Exchange connectivity and protocols (FIX, REST, WebSocket)
- Data storage and databases (SQL, time-series DBs)

**Practice:**
- Setting up data pipelines with Python
- Working with Pandas for financial data
- Real-time data streaming implementation
- Building a data warehouse for backtesting

---

## Module 3: Time Series Analysis

### [3.1 Univariate Time Series](notebooks/module_03_time_series_analysis/3_1_univariate_time_series.ipynb)
**Theory:**
- Stationarity and unit root tests (ADF, KPSS)
- Autocorrelation and partial autocorrelation
- ARMA and ARIMA models
- Seasonality and trend decomposition
- GARCH models for volatility

**Practice:**
- Testing price series for stationarity
- Fitting ARIMA models to returns
- Forecasting with time series models
- Volatility modeling with GARCH

### [3.2 Multivariate Time Series](notebooks/module_03_time_series_analysis/3_2_multivariate_time_series.ipynb)
**Theory:**
- Vector Autoregression (VAR)
- Cointegration and error correction models
- Granger causality
- State-space models and Kalman filtering

**Practice:**
- Pairs trading with cointegration
- Building VAR models for related assets
- Implementing Kalman filters for dynamic hedging
- Multi-asset forecasting systems

---

## Module 4: Portfolio Theory & Risk Management

### [4.1 Modern Portfolio Theory](notebooks/module_04_portfolio_theory_risk_management/4_1_modern_portfolio_theory.ipynb)
**Theory:**
- Mean-variance optimization
- Efficient frontier and capital market line
- Sharpe ratio and risk-adjusted returns
- CAPM and factor models
- Black-Litterman model

**Practice:**
- Implementing Markowitz optimization
- Efficient frontier visualization
- Factor model construction
- Portfolio rebalancing strategies

### [4.2 Risk Metrics & Management](notebooks/module_04_portfolio_theory_risk_management/4_2_risk_metrics_management.ipynb)
**Theory:**
- Value at Risk (VaR) - parametric, historical, Monte Carlo
- Conditional VaR (Expected Shortfall)
- Maximum drawdown and recovery time
- Beta, alpha, and performance attribution
- Risk budgeting and risk parity

**Practice:**
- Calculating VaR with multiple methods
- Monte Carlo simulation for portfolio risk
- Drawdown analysis and visualization
- Building risk monitoring dashboards

### [4.3 Advanced Portfolio Techniques](notebooks/module_04_portfolio_theory_risk_management/4_3_advanced_portfolio_techniques.ipynb)
**Theory:**
- Kelly criterion for position sizing
- Hierarchical Risk Parity (HRP)
- Robust optimization methods
- Transaction cost models
- Portfolio rebalancing strategies

**Practice:**
- Implementing Kelly criterion
- HRP portfolio construction
- Comparing optimization methods
- Backtesting with transaction costs

---

## Module 5: Algorithmic Trading Strategies

### [5.1 Momentum & Trend Following](notebooks/module_05_algorithmic_trading_strategies/5_1_momentum_trend_following.ipynb)
**Theory:**
- Moving averages and crossover systems
- Momentum indicators (RSI, MACD, ADX)
- Breakout strategies
- Trend strength measurement
- Regime detection

**Practice:**
- Dual moving average system
- RSI mean reversion strategy
- Turtle trading system implementation
- Regime-switching strategies

### [5.2 Mean Reversion Strategies](notebooks/module_05_algorithmic_trading_strategies/5_2_mean_reversion_strategies.ipynb)
**Theory:**
- Statistical arbitrage principles
- Pairs trading and cointegration
- Bollinger Bands and z-scores
- Ornstein-Uhlenbeck process
- Half-life of mean reversion

**Practice:**
- Pairs trading algorithm
- Bollinger Band mean reversion
- Statistical arbitrage with multiple pairs
- Dynamic position sizing for mean reversion

### [5.3 Market Making & Arbitrage](notebooks/module_05_algorithmic_trading_strategies/5_3_market_making_arbitrage.ipynb)
**Theory:**
- Bid-ask spread capture
- Inventory management
- Statistical arbitrage
- Triangular arbitrage in FX
- Index arbitrage
- Crypto arbitrage opportunities

**Practice:**
- Simple market making algorithm
- Cross-exchange arbitrage detector
- Index arbitrage scanner
- Latency arbitrage concepts

### [5.4 Machine Learning Strategies](notebooks/module_05_algorithmic_trading_strategies/5_4_machine_learning_strategies.ipynb)
**Theory:**
- Feature engineering for trading
- Supervised learning (classification/regression)
- Ensemble methods (Random Forest, XGBoost)
- Time series cross-validation
- Overfitting prevention
- Walk-forward analysis

**Practice:**
- Price direction prediction with ML
- Feature importance analysis
- Building ensemble trading models
- Proper backtesting with ML

---

*See [plan.md](plan.md) for the full course roadmap (Modules 6–14).*

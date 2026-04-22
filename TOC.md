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

---

## Module 6: Derivatives & Options Trading

### [6.1 Options Pricing Theory](notebooks/module_06_derivatives_options_trading/6_1_options_pricing_theory.ipynb)
**Theory:**
- Black-Scholes model and assumptions
- Risk-neutral pricing and no-arbitrage
- Binomial trees and lattice methods
- Monte Carlo methods for pricing
- Volatility surface and smile

**Practice:**
- Implementing Black-Scholes pricer
- Binomial tree option pricing
- Monte Carlo pricing with variance reduction
- Volatility surface construction

### [6.2 Options Strategies](notebooks/module_06_derivatives_options_trading/6_2_options_strategies.ipynb)
**Theory:**
- Basic spreads: vertical, horizontal, diagonal
- Volatility strategies: straddles, strangles, butterflies
- Income strategies: covered calls, cash-secured puts
- Greeks management and delta hedging
- Portfolio-level options risk

**Practice:**
- Payoff diagram construction
- Greeks calculation and visualization
- Delta-neutral portfolio management
- Strategy selection by market regime

### [6.3 Advanced Derivatives](notebooks/module_06_derivatives_options_trading/6_3_advanced_derivatives.ipynb)
**Theory:**
- Exotic options: barriers, Asians, lookbacks
- Interest rate derivatives: caps, floors, swaptions
- Credit derivatives: CDS, CDOs
- Volatility derivatives: VIX futures, variance swaps
- Structured products

**Practice:**
- Exotic option pricing via Monte Carlo
- Interest rate model implementation
- CDS pricing and credit risk
- Variance swap replication

---

## Module 7: Machine Learning & AI for Trading

### [7.1 Classical Machine Learning](notebooks/module_07_machine_learning_ai_trading/7_1_classical_machine_learning.ipynb)
**Theory:**
- Supervised vs. unsupervised learning in finance
- Feature engineering from market data
- Regularization: Ridge, Lasso, ElasticNet
- Ensemble methods: Bagging, Boosting, Stacking
- Model selection and cross-validation for time series

**Practice:**
- Return prediction with regularized regression
- XGBoost for signal generation
- Feature importance and selection
- Walk-forward model evaluation

### [7.2 Deep Learning for Finance](notebooks/module_07_machine_learning_ai_trading/7_2_deep_learning_for_finance.ipynb)
**Theory:**
- Neural network architectures for sequences
- LSTM and GRU for time series
- Attention mechanisms and Transformers
- Autoencoders for anomaly detection
- Transfer learning in finance

**Practice:**
- LSTM price forecasting
- Transformer-based factor models
- Autoencoder for regime detection
- Fine-tuning pre-trained financial models

### [7.3 Reinforcement Learning](notebooks/module_07_machine_learning_ai_trading/7_3_reinforcement_learning.ipynb)
**Theory:**
- MDP formulation for trading
- Q-Learning and Deep Q-Networks (DQN)
- Policy gradient methods (PPO, A3C)
- Reward shaping for Sharpe maximization
- Multi-agent market simulation

**Practice:**
- Simple Q-Learning trading agent
- DQN portfolio manager
- Simulated trading environment
- RL agent evaluation and benchmarking

---

## Module 8: Backtesting & Strategy Evaluation

### [8.1 Backtesting Framework Design](notebooks/module_08_backtesting_strategy_evaluation/8_1_backtesting_framework_design.ipynb)
**Theory:**
- Event-driven vs. vectorized backtesting
- Look-ahead bias and survivorship bias
- Transaction costs, slippage, and market impact
- Position sizing and capital allocation
- Handling corporate actions and data adjustments

**Practice:**
- Building an event-driven backtester
- Incorporating realistic transaction costs
- Data quality checks and cleaning
- Vectorized backtesting with pandas

### [8.2 Performance Metrics](notebooks/module_08_backtesting_strategy_evaluation/8_2_performance_metrics.ipynb)
**Theory:**
- Return metrics: CAGR, annualization
- Risk-adjusted: Sharpe, Sortino, Calmar ratios
- Drawdown analysis: max drawdown, recovery time
- Alpha, beta, and information ratio
- Statistical significance of backtest results

**Practice:**
- Comprehensive performance report generation
- Benchmark comparison framework
- Drawdown visualization and analysis
- Bootstrap significance testing

### [8.3 Strategy Optimization & Validation](notebooks/module_08_backtesting_strategy_evaluation/8_3_strategy_optimization_validation.ipynb)
**Theory:**
- Parameter optimization and overfitting
- Walk-forward optimization
- Out-of-sample testing methodology
- Monte Carlo robustness testing
- Multiple testing correction (deflated Sharpe)

**Practice:**
- Grid search with walk-forward validation
- Monte Carlo permutation testing
- Regime-conditional performance analysis
- Strategy robustness stress tests

---

## Module 9: Execution & Order Management

### [9.1 Order Execution Algorithms](notebooks/module_09_execution_order_management/9_1_order_execution_algorithms.ipynb)
**Theory:**
- TWAP and VWAP execution algorithms
- Implementation shortfall (Almgren-Chriss)
- Participation rate algorithms
- Adaptive execution and market impact
- Dark pool routing

**Practice:**
- TWAP algorithm implementation
- VWAP schedule construction
- Market impact estimation
- Execution quality analysis (TCA)

### [9.2 High-Frequency Trading Concepts](notebooks/module_09_execution_order_management/9_2_high_frequency_trading_concepts.ipynb)
**Theory:**
- Latency and co-location
- Order book dynamics at microsecond scale
- Statistical arbitrage at high frequency
- Adverse selection and toxic flow
- Regulatory considerations (Reg NMS, MiFID II)

**Practice:**
- Order book simulation
- Tick data analysis
- Adverse selection metrics
- Latency simulation

### [9.3 Position Management](notebooks/module_09_execution_order_management/9_3_position_management.ipynb)
**Theory:**
- Real-time P&L calculation
- Margin and leverage management
- Risk limits and circuit breakers
- Hedging overlays
- Currency and commodity exposure management

**Practice:**
- Real-time portfolio tracker
- Risk limit monitoring system
- Automated hedging rules
- Multi-currency P&L attribution

---

## Module 10: Production Systems & Infrastructure

### [10.1 Trading System Architecture](notebooks/module_10_production_systems_infrastructure/10_1_trading_system_architecture.ipynb)
**Theory:**
- System design for low-latency trading
- Message queues (Kafka, RabbitMQ)
- Microservices vs. monolithic architectures
- Database design for trading (TimescaleDB, kdb+)
- Cloud vs. on-premise considerations

**Practice:**
- Architecture diagram and design
- Message queue simulation
- Time-series database setup
- System latency profiling

### [10.2 Risk Controls & Compliance](notebooks/module_10_production_systems_infrastructure/10_2_risk_controls_compliance.ipynb)
**Theory:**
- Pre-trade and post-trade risk checks
- Kill switches and circuit breakers
- Regulatory reporting (MiFID II, Dodd-Frank)
- Audit trails and trade surveillance
- Model risk management

**Practice:**
- Pre-trade risk check implementation
- Compliance rule engine
- Audit log system
- Risk limit breach alerting

### [10.3 Monitoring & Operations](notebooks/module_10_production_systems_infrastructure/10_3_monitoring_operations.ipynb)
**Theory:**
- System health monitoring
- P&L and performance dashboards
- Alerting and incident response
- Capacity planning
- Disaster recovery

**Practice:**
- Metrics collection system
- Real-time dashboard (Plotly Dash)
- Alert configuration
- Runbook automation

---

## Module 11: Live Trading & Broker Integration

### [11.1 Broker APIs & Connectivity](notebooks/module_11_live_trading_broker_integration/11_1_broker_apis_connectivity.ipynb)
**Theory:**
- REST vs. WebSocket APIs
- Authentication and security (OAuth, API keys)
- FIX protocol fundamentals
- Order lifecycle management
- Rate limiting and error handling

**Practice:**
- Interactive Brokers API connection
- Alpaca paper trading setup
- Order submission and management
- Real-time feed subscription

### [11.2 Paper Trading](notebooks/module_11_live_trading_broker_integration/11_2_paper_trading.ipynb)
**Theory:**
- Simulated vs. live execution differences
- Paper trading best practices
- Slippage modeling in simulation
- Transition from backtest to paper trade
- Monitoring and iteration

**Practice:**
- Paper trading system with Alpaca
- Performance tracking vs. backtest
- Execution quality measurement
- Strategy adjustment workflow

### [11.3 Going Live](notebooks/module_11_live_trading_broker_integration/11_3_going_live.ipynb)
**Theory:**
- Pre-live checklist and readiness review
- Capital allocation and scaling
- Live monitoring protocols
- Emergency shutdown procedures
- Continuous improvement process

**Practice:**
- Go-live checklist implementation
- Live P&L dashboard
- Automated health checks
- Post-trade analysis workflow

---

## Module 12: Advanced Topics & Research

### [12.1 Alternative Data](notebooks/module_12_advanced_topics_research/12_1_alternative_data.ipynb)
**Theory:**
- Types of alt data: satellite, credit card, web scraping
- Signal extraction from unstructured data
- Data licensing and compliance
- Alpha decay and crowding
- Alternative data vendors

**Practice:**
- Sentiment signal from news headlines
- Web scraping for fundamental data
- Satellite data signal construction
- Alt data alpha validation

### [12.2 Factor Investing](notebooks/module_12_advanced_topics_research/12_2_factor_investing.ipynb)
**Theory:**
- Fama-French five-factor model
- Quality, momentum, value, low-volatility factors
- Factor timing and rotation
- Factor crowding and capacity
- Smart beta and ETF construction

**Practice:**
- Multi-factor stock selection model
- Factor exposure analysis
- Factor portfolio construction
- Factor timing signals

### [12.3 Portfolio Construction Techniques](notebooks/module_12_advanced_topics_research/12_3_portfolio_construction_techniques.ipynb)
**Theory:**
- Black-Litterman with views
- Robust optimization (Ledoit-Wolf, shrinkage)
- Risk budgeting and factor risk parity
- Constraints: turnover, sector, factor
- Dynamic rebalancing

**Practice:**
- Black-Litterman implementation
- Covariance shrinkage comparison
- Constrained optimization
- Rebalancing cost-benefit analysis

### [12.4 Market-Neutral Strategies](notebooks/module_12_advanced_topics_research/12_4_market_neutral_strategies.ipynb)
**Theory:**
- Long-short equity construction
- Beta neutrality and factor neutrality
- Dollar vs. beta neutral portfolios
- Pairs trading at scale
- Statistical arbitrage portfolios

**Practice:**
- Long-short equity strategy
- Beta-hedged portfolio construction
- Factor-neutral signal isolation
- Gross/net exposure management

---

## Module 13: LLMs in Quantitative Finance

### [13.1 LLM Fundamentals for Finance](notebooks/module_13_llm_quantitative_finance/13_1_llm_fundamentals_for_finance.ipynb)
### [13.2 Sentiment Analysis & News Processing](notebooks/module_13_llm_quantitative_finance/13_2_sentiment_analysis_news_processing.ipynb)
### [13.3 Financial Document Analysis](notebooks/module_13_llm_quantitative_finance/13_3_financial_document_analysis.ipynb)
### [13.4 Fundamental Analysis Automation](notebooks/module_13_llm_quantitative_finance/13_4_fundamental_analysis_automation.ipynb)
### [13.5 Trading Strategy Generation](notebooks/module_13_llm_quantitative_finance/13_5_trading_strategy_generation.ipynb)
### [13.6 Code Generation & Debugging](notebooks/module_13_llm_quantitative_finance/13_6_code_generation_debugging.ipynb)
### [13.7 Risk Narrative & Reporting](notebooks/module_13_llm_quantitative_finance/13_7_risk_narrative_reporting.ipynb)
### [13.8 Market Intelligence & Research](notebooks/module_13_llm_quantitative_finance/13_8_market_intelligence_research.ipynb)
### [13.9 Conversational Trading Assistants](notebooks/module_13_llm_quantitative_finance/13_9_conversational_trading_assistants.ipynb)
### [13.10 Advanced LLM Techniques](notebooks/module_13_llm_quantitative_finance/13_10_advanced_llm_techniques.ipynb)
### [13.11 LLM-Enhanced Alpha Generation](notebooks/module_13_llm_quantitative_finance/13_11_llm_enhanced_alpha_generation.ipynb)
### [13.12 Ethics, Bias & Limitations](notebooks/module_13_llm_quantitative_finance/13_12_ethics_bias_limitations.ipynb)
### [13.13 Production LLM Systems](notebooks/module_13_llm_quantitative_finance/13_13_production_llm_systems.ipynb)
### [13.14 Case Studies](notebooks/module_13_llm_quantitative_finance/13_14_case_studies.ipynb)

---

## Module 14: Capstone Projects

### [14.1 Momentum Strategy](notebooks/module_14_capstone_projects/14_1_momentum_strategy.ipynb)
### [14.2 ML Factor Model](notebooks/module_14_capstone_projects/14_2_ml_factor_model.ipynb)
### [14.3 Options Volatility Strategy](notebooks/module_14_capstone_projects/14_3_options_volatility_strategy.ipynb)
### [14.4 Multi-Asset Portfolio System](notebooks/module_14_capstone_projects/14_4_multi_asset_portfolio_system.ipynb)
### [14.5 Personal Trading Infrastructure](notebooks/module_14_capstone_projects/14_5_personal_trading_infrastructure.ipynb)
### [14.6 LLM Trading Research Assistant](notebooks/module_14_capstone_projects/14_6_llm_trading_research_assistant.ipynb)

---

*See [plan.md](plan.md) for the full course roadmap and detailed descriptions.*

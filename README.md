# Project: Italian Industrial Production Forecasting

**Course:** Time Series and Forecasting (2025/2026) 
**Authors:** Paolo Minini & Francesco Sebastiano Memmola 

## 1. Project Overview

This study forecasts the Italian Industrial Production Index (IPI) using monthly data from 2000 to 2022. The central research question is whether incorporating richer macroeconomic information (multivariate models) improves one-step-ahead forecasts compared to simple univariate benchmarks, specifically in the presence of structural breaks like the 2008 Financial Crisis and the 2020 COVID-19 pandemic.

## 2. Data & Preprocessing

The dataset spans monthly observations from 2000 to 2022, divided into a training sample (2000-2018) and a test sample (2018-2022).

**Target Variable:** Italian Industrial Production Index (IPI), seasonally adjusted.


**Exogenous Variables (FRED):** Producer Price Index (PPI), Unemployment rate, Brent crude oil prices, and OECD Composite Leading Indicator (CLI).


**Factor Dataset (Barigozzi.eu):** A panel of 31 European macroeconomic indicators (labor, prices, interest rates, etc.) used to extract common factors via PCA.

**Transformations:** Variables were transformed (log-differences, monthly growth) to ensure stationarity.

**Structural Dummies:** Two deterministic dummies were included to handle shocks:

**Shift dummy:** 2008 Financial Crisis.

**Impulse dummy:** 2020 COVID-19 shock.





## 3. Methodology

All models were evaluated using a **recursive expanding-window design**, re-estimating the model at each step to mirror real-time forecasting conditions. The evaluation metric focuses exclusively on **1-step-ahead forecasts**.

### Models Implemented

1. **Benchmarks:**

**Random Walk (RW):** The baseline model (best forecast of tomorrow is today's value).


**ARIMA (0,1,2):** Selected via AIC/BIC as the best univariate specification.




2. **Multivariate Models:**

**VAR-X(1):** Vector Autoregression using the core exogenous variables and crisis dummies.

**Dynamic Factor VAR-X(1) (FAVAR-X):** Augments the model with a single Principal Component (Factor) extracted from the broad 31-variable dataset.





## 4. Key Results

Performance was evaluated using Root Mean Squared Forecast Error (RMSE) and Mean Absolute Forecast Error (MAE) relative to the Random Walk.

**The Random Walk outperformed all complex models** in the out-of-sample test period (2018–2022).

**Impact of COVID-19:** Complex models (VAR-X and FAVAR-X) failed to anticipate the sudden 2020 collapse. The forecasts only adjusted after the shock occurred, resulting in errors similar to or slightly worse than the naive benchmark.


**Conclusion:** While macro variables explain medium-term co-movements, they do not systematically improve short-term (1-step-ahead) forecast accuracy during periods dominated by extreme exogenous shocks.


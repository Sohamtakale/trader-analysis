# 📊 Trader Performance vs Market Sentiment Analysis

## 📌 Project Overview

This project analyzes how cryptocurrency trader behavior and performance change under different market sentiment conditions (Fear, Greed, Neutral).

Using historical trader transaction data and Bitcoin Fear & Greed Index data, we investigate:

* Whether trader profitability differs across sentiment regimes
* How trading behavior changes during Fear vs Greed
* How different trader segments respond to sentiment
* What actionable trading strategies can be derived

---

# 📂 Datasets Used

## 1️⃣ Bitcoin Market Sentiment Dataset

* Daily sentiment classification (Fear / Greed / Neutral)
* Used to categorize trading environment

## 2️⃣ Historical Trader Data (Hyperliquid)

Includes:

* Account
* Timestamp
* Closed PnL
* Trade size (USD)
* Trade direction (Buy/Sell)
* Transaction-level details

---

# ⚙️ Methodology

## Step 1 — Data Preparation

* Loaded both datasets
* Checked missing values and duplicates
* Converted timestamps to datetime
* Aggregated trades to daily trader-level metrics
* Merged sentiment dataset with trading data
* Removed rows with missing sentiment labels

Final dataset:
**1963 trader-day observations**

---

## Step 2 — Feature Engineering

Daily trader metrics created:

* `daily_pnl` → Total daily profit/loss
* `win_rate` → % profitable trades
* `trades_per_day` → Trade frequency
* `avg_trade_size` → Risk exposure proxy
* `long_ratio` → Direction bias
* Sentiment classification

Note:
Leverage was not directly available. Average trade size was used as a proxy for trader risk exposure.

---

# 📊 Part B — Behaviour & Performance Analysis

## 1️⃣ Performance Differences Across Sentiment

Findings:

* Fear sentiment produced highest average trader profitability
* Greed sentiment produced slightly higher win rate
* Neutral sentiment showed lowest performance

Interpretation:
Profitability differences are driven more by volatility and trade sizing than by trade accuracy.

---

## 2️⃣ Behaviour Changes Based On Sentiment

During Fear sentiment:

* Increased trade frequency
* Larger average trade size
* Slight increase in long bias

During Greed sentiment:

* Reduced trade size
* Lower trading frequency
* Slightly higher win rate but lower profitability

Conclusion:
Traders behave more aggressively during fearful markets.

---

## 3️⃣ Trader Segmentation

### 🔹 Activity Segmentation

High activity traders consistently outperformed low activity traders, especially during Fear periods.

---

### 🔹 Risk Segmentation

High risk traders generated largest profits during Fear sentiment but showed weaker performance during Greed.

Low risk traders showed stable but smaller returns.

---

### 🔹 Consistency Segmentation

Consistency measured using win-rate volatility.

Consistent traders demonstrated stable profitability patterns while inconsistent traders showed larger sentiment-driven performance swings.

---

# 🔍 Key Insights

1. Fear sentiment produces highest trader profitability.
2. High activity traders benefit most during volatile Fear periods.
3. Trade sizing contributes more to profitability than win-rate accuracy.
4. Aggressive risk-taking correlates with higher returns during volatility spikes.

---

# 💡 Part C — Actionable Strategy Recommendations

## Strategy 1 — Volatility Exploitation

Increase trading frequency and moderately increase trade size during Fear sentiment, particularly for high activity traders.

## Strategy 2 — Risk Moderation

Reduce trade size and apply stricter risk control during Greed sentiment to avoid overconfidence-driven losses.

---

# 📈 Visual Evidence

All supporting charts and tables are available in:

```
notebooks/analysis.ipynb
```

---

# 🛠 Tech Stack

* Python
* Pandas
* Matplotlib / Seaborn
* Jupyter Notebook
* Git & GitHub

---

# 📁 Project Structure

```
data/              Raw datasets
notebooks/         Analysis notebook
outputs/           Generated charts
src/               Utility scripts (if any)
README.md          Project overview & documentation
```

---

# 🔧 Setup Instructions

## 1️⃣ Clone Repository

```bash
git clone https://github.com/Sohamtakale/trader-analysis.git
cd trader-analysis
```

---

## 2️⃣ Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ How To Run The Project

## Run Notebook Analysis

```bash
jupyter notebook
```

Then open:

```
notebooks/analysis.ipynb
```

Run all cells sequentially.

---

## Generate Charts

Charts are generated automatically when running the notebook.

---

# 📦 Reproducibility

All preprocessing, feature engineering, and analysis steps are fully documented inside the notebook.

---

# 🚀 Future Improvements

* Predictive ML model for trader profitability
* Clustering traders into behavioral archetypes
* Streamlit dashboard for interactive visualization
* Risk-adjusted performance metrics

---

# 🧠 Conclusion

This analysis demonstrates that market sentiment significantly influences trader behaviour and performance. Fear-driven volatility provides higher profit opportunities, particularly for high activity and high risk traders. Incorporating sentiment-aware strategies can improve performance and risk management.

---


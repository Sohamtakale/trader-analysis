# 📊 Trader Performance vs Market Sentiment Analysis

## 📌 Project Overview

This project analyzes how cryptocurrency trader performance and behavior change under different market sentiment conditions (Fear, Greed, Neutral).

Using historical trader transaction data and Bitcoin Fear & Greed Index data, this project explores how sentiment impacts trader profitability, trading behavior, and risk exposure.

---

## 🎯 Project Objectives

* Analyze trader performance across different sentiment regimes
* Identify behavioral changes during Fear vs Greed markets
* Segment traders based on activity, risk, and consistency
* Generate actionable sentiment-aware trading insights

---

## 📂 Datasets Used

### 1️⃣ Bitcoin Market Sentiment Dataset

Contains daily market sentiment classification:

* Fear
* Greed
* Neutral

Used to categorize the trading environment.

---

### 2️⃣ Historical Trader Data (Hyperliquid)

Includes:

* Account
* Timestamp
* Closed PnL
* Trade size (USD)
* Trade direction (Buy/Sell)
* Transaction metadata

---

## ⚙️ Methodology Summary

### Data Preparation

* Loaded and inspected both datasets
* Checked missing values and duplicates
* Converted timestamps to datetime format
* Aggregated trade data to daily trader-level metrics
* Merged trading data with sentiment data
* Removed rows with missing sentiment classification

Final dataset:
**1963 trader-day observations**

---

### Feature Engineering

Daily trader metrics created:

* `daily_pnl` → Total daily profit/loss
* `win_rate` → Percentage of profitable trades
* `trades_per_day` → Trade frequency
* `avg_trade_size` → Risk exposure proxy
* `long_ratio` → Directional bias indicator

Note:
Leverage data was unavailable. Average trade size was used as a proxy for trading risk.

---

## 📈 Key Results Summary

* Traders generated highest profitability during Fear sentiment periods.
* Trading activity and trade size increased during volatile market conditions.
* High activity and high risk traders benefited most from Fear sentiment.
* Trade sizing had stronger impact on profitability than win rate alone.

---

## 📊 Output Visualizations

All generated charts are stored in:

```
outputs/
```

Example outputs include:

* Trader PnL by sentiment
* PnL by activity segment
* PnL by risk segment
* Consistency analysis

---

## 📁 Project Structure

```
trader-analysis/
│
├── data/              Raw datasets
├── notebooks/         Analysis notebook
│   └── analysis.ipynb
├── outputs/           Generated charts
├── src/               Utility scripts (optional)
├── requirements.txt   Python dependencies
├── README.md          Project documentation
└── .gitignore
```

---

## 🔧 Setup Instructions

### 1️⃣ Clone Repository

git clone https://github.com/Sohamtakale/trader-analysis.git
cd trader-analysis

---

### 2️⃣ Create Virtual Environment

python3 -m venv venv
source venv/bin/activate
---

### 3️⃣ Install Dependencies

pip install -r requirements.txt
---

## ▶️ Running The Project

### Launch Jupyter Notebook

jupyter notebook

Open:
notebooks/analysis.ipynb

Run all cells sequentially to reproduce results and charts.

---

## 📦 Reproducibility

All preprocessing, feature engineering, and analysis steps are documented inside the notebook to ensure reproducibility.

---

## 🛠 Tech Stack

* Python
* Pandas
* Matplotlib
* Seaborn
* Jupyter Notebook
* Git & GitHub

ANSWERS FOR BOTH PART B AND C ARE PRESENT IN REPORT.MD AND READMEMD.   

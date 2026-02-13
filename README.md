# README.md

# 📊 Trader Performance vs Market Sentiment Analysis

## Project Overview

This project analyzes how cryptocurrency trader performance and behaviour change across different market sentiment regimes (Fear, Greed, Neutral). The analysis uses trader transaction data along with Bitcoin Fear & Greed Index sentiment classification.

The goal is to identify behavioural patterns, performance differences, trader segmentation, and actionable trading insights.

---

## Repository Structure

```
trader-analysis/
│
├── data/                 # Raw datasets
├── notebooks/
│   ├── analysis.ipynb
│   └── clustering.ipynb (bonus)
├── dashboard/
│   └── app.py            # Streamlit dashboard (bonus)
├── outputs/              # Generated charts and screenshots
├── REPORT.md             # Detailed analysis answers
├── requirements.txt
└── README.md
```

---

## Setup Instructions

### 1. Clone Repository

```bash
git clone https://github.com/Sohamtakale/trader-analysis.git
cd trader-analysis
```

---

### 2. Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## How To Run The Analysis

### Run Jupyter Notebook

```bash
jupyter notebook
```

Open:

```
notebooks/analysis.ipynb
```

Run all cells sequentially to reproduce results, charts, and insights.

---

## How To Run Clustering (Bonus)

Open:

```
notebooks/clustering.ipynb
```

Run all cells to generate trader behavioural archetypes.

---

## How To Run Dashboard (Bonus)

```bash
streamlit run dashboard/app.py
```

The dashboard allows interactive exploration of trading performance across sentiment regimes and trader segments.

---

## Output Charts

Generated visualizations are saved inside:

```
outputs/
```

These include:

* PnL by sentiment
* Activity segment performance
* Risk segment performance
* Clustering visualizations
* Dashboard preview

---

## Reproducibility

All preprocessing, feature engineering, modelling, and visualization steps are documented within the notebooks.

---

## Tech Stack

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* Streamlit
* Git & GitHub

---

## Future Improvements

* Predictive modelling for next-day trader profitability
* Risk-adjusted performance metrics
* Expanded behavioural clustering
* Enhanced dashboard interactivity

---

# Executive Summary

**Trader Performance vs Market Sentiment Analysis**

## Methodology

This study analyzes how trader performance and behavior vary across different market sentiment regimes (Fear, Greed, Neutral) using historical trader transaction data and Bitcoin Fear & Greed Index classification.

The workflow consisted of:

### Data Preparation

1. Cleaned and validated both datasets (missing values, duplicates).
2. Converted timestamps to daily level.
3. Merged trader data with daily sentiment classification.
4. Aggregated trade-level data into daily account-level metrics.

### Feature Engineering
For each trader-day, the following metrics were computed:

- Daily PnL (profitability)
- Win rate
- Trade frequency
- Average trade size (used as leverage/risk proxy)
- Long/Short bias ratio

### Segmentation
Traders were segmented into:

- High vs Low Activity
- High vs Low Risk (based on trade size)
- Consistent vs Inconsistent (based on win-rate volatility)

This allowed comparison of performance and behavior across sentiment regimes and trader archetypes.

## Key Insights

**Performance is highest during Fear sentiment.**
Traders generate significantly higher average daily PnL during Fear periods compared to Greed and Neutral regimes. This suggests volatility-driven opportunities dominate during market downturns.

**Trade size drives profitability more than win rate.**
Win rate differences between Fear and Greed are small. However, larger position sizing during Fear leads to substantially higher profitability. Profitability is driven more by exposure than by accuracy.

**High-activity traders outperform consistently.**
Traders with higher daily trade frequency generate significantly higher returns, particularly during Fear periods.

**Risk-taking increases during Fear sentiment.**
Average trade size and activity both increase during Fear, indicating more aggressive behavior under volatile market conditions.

**Behavior changes more than accuracy.**
Sentiment influences trading behavior (frequency and size) more strongly than win rate itself.

## Strategy Recommendations
### 1. Fear Regime Volatility Strategy

**During Fear sentiment:**

- Increase trade participation for high-activity traders.
- Allow moderately higher position sizing.
- Focus on volatility-based setups.

**Rationale:** Fear periods historically produce the highest profitability due to volatility expansion.

### 2. Greed Regime Risk Control Strategy

**During Greed sentiment:**

- Reduce average trade size.
- Apply stricter risk management.
- Focus on selective entries rather than frequent trading.

**Rationale:** Greed periods show lower profitability and may reflect overconfidence-driven inefficiencies.

This analysis demonstrates that incorporating market sentiment into trading decisions can enhance performance and improve risk management. Sentiment-aware strategies allow alignment of risk exposure with prevailing market volatility conditions.

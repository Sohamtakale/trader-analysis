import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import os

# Page config
st.set_page_config(page_title="Trader Segmentation Dashboard", layout="wide")

# Paths
DATA_DIR = "data"
TRADES_FILE = os.path.join(DATA_DIR, "trader_data.csv")
SENTIMENT_FILE = os.path.join(DATA_DIR, "sentiment.csv")
CLUSTERED_DATA_FILE = os.path.join("outputs", "trader_features_with_clusters.csv")

@st.cache_data
def load_data():
    # Load clustered data (profiles)
    if os.path.exists(CLUSTERED_DATA_FILE):
        profiles = pd.read_csv(CLUSTERED_DATA_FILE)
    else:
        st.error("Clustered data not found. Please run the clustering script first.")
        return None, None, None

    # Load raw trades for detailed analysis
    trades = pd.read_csv(TRADES_FILE)
    trades['Timestamp IST'] = pd.to_datetime(trades['Timestamp IST'], format='mixed')
    trades['date'] = trades['Timestamp IST'].dt.date
    trades['date'] = pd.to_datetime(trades['date'])

    # Load sentiment
    sentiment = pd.read_csv(SENTIMENT_FILE)
    sentiment['date'] = pd.to_datetime(sentiment['date'])

    # Merge sentiment into trades
    trades = trades.merge(sentiment[['date', 'classification', 'value']], on='date', how='left')
    
    # Merge cluster into trades using Account match
    trades = trades.merge(profiles[['Account', 'cluster']], on='Account', how='left')

    return profiles, trades, sentiment

try:
    profiles, trades, sentiment = load_data()
except Exception as e:
    st.error(f"Error loading data: {e}")
    st.stop()

if profiles is not None:
    st.title("Trader Segmentation & Sentiment Analysis Dashboard")

    # sidebar filters
    st.sidebar.header("Filters")
    
    # Sentiment Filter
    sentiment_options = ['All'] + sorted(list(sentiment['classification'].unique()))
    selected_sentiment = st.sidebar.selectbox("Select Sentiment Regime", sentiment_options)

    # Cluster Filter
    cluster_options = ['All'] + sorted(list(profiles['cluster'].unique()))
    selected_cluster = st.sidebar.selectbox("Select Trader Segment (Cluster)", cluster_options)

    # --- Trader Segmentation View ---
    st.header("1. Trader Segmentation Analysis")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("Trader Clusters (PCA)")
        fig_pca = px.scatter(
            profiles, 
            x='pca_x', 
            y='pca_y', 
            color='cluster',
            hover_data=['Account', 'avg_trade_size', 'win_rate', 'avg_trades_per_day'],
            title="Trader Clusters (Dimension Reduced)",
            template="plotly_dark"
        )
        st.plotly_chart(fig_pca, use_container_width=True)

    with col2:
        st.subheader("Cluster Archetypes")
        cluster_summary = profiles.groupby('cluster')[['avg_trade_size', 'win_rate', 'avg_trades_per_day', 'pnl_variability', 'long_bias']].mean().reset_index()
        st.dataframe(cluster_summary.style.format({
            'avg_trade_size': '{:.2f}',
            'win_rate': '{:.2%}',
            'avg_trades_per_day': '{:.1f}',
            'pnl_variability': '{:.2f}',
            'long_bias': '{:.2%}'
        }), use_container_width=True)
        
        st.markdown("**Archetype Description:**")
        st.markdown("- **Cluster 0**: High volume/risk?")
        st.markdown("- **Cluster 1**: Conservative?")
        st.markdown("- **Cluster 2**: ...")  # Placeholder logic, real interpretation depends on data run

    # --- Interactive Analysis ---
    st.header("2. Performance under different Conditions")
    
    # Filter trades based on inputs
    filtered_trades = trades.copy()
    
    if selected_sentiment != 'All':
        filtered_trades = filtered_trades[filtered_trades['classification'] == selected_sentiment]
    
    if selected_cluster != 'All':
        filtered_trades = filtered_trades[filtered_trades['cluster'] == selected_cluster]

    # Metrics
    if not filtered_trades.empty:
        total_pnl = filtered_trades['Closed PnL'].sum()
        total_volume = filtered_trades['Size USD'].sum()
        avg_win_rate = (filtered_trades['Closed PnL'] > 0).mean()
        
        m1, m2, m3 = st.columns(3)
        m1.metric("Total PnL (Filtered)", f"${total_pnl:,.2f}")
        m2.metric("Total Volume", f"${total_volume:,.2f}")
        m3.metric("Win Rate", f"{avg_win_rate:.2%}")
        
        # Charts
        c1, c2 = st.columns(2)
        
        with c1:
            # PnL over time
            pnl_over_time = filtered_trades.groupby('date')['Closed PnL'].sum().reset_index()
            fig_pnl = px.line(pnl_over_time, x='date', y='Closed PnL', title="PnL Over Time (Filtered)")
            st.plotly_chart(fig_pnl, use_container_width=True)
            
        with c2:
            # Direction Distribution
            fig_dir = px.pie(filtered_trades, names='Direction', title="Trade Direction Distribution (Filtered)")
            st.plotly_chart(fig_dir, use_container_width=True)
            
    else:
        st.warning("No trades found for selected filters.")

else:
    st.warning("Data not loaded correctly.")

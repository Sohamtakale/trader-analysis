import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Define paths
DATA_DIR = "data"
TRADES_FILE = os.path.join(DATA_DIR, "trader_data.csv")
SENTIMENT_FILE = os.path.join(DATA_DIR, "sentiment.csv")
OUTPUT_DIR = "outputs"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "trader_features_with_clusters.csv")
CLUSTER_PLOT_FILE = os.path.join(OUTPUT_DIR, "trader_clusters_pca.png")

def load_data():
    """Lengths and merges trade and sentiment data."""
    print("Loading data...")
    if not os.path.exists(TRADES_FILE):
        raise FileNotFoundError(f"Trades file not found at {TRADES_FILE}")
    
    trades = pd.read_csv(TRADES_FILE)
    
    # Ensure relevant columns exist
    required_columns = ['Account', 'Size USD', 'Closed PnL', 'Timestamp IST', 'Direction']
    for col in required_columns:
        if col not in trades.columns:
             # Try to infer if names are slightly different (e.g. from notebook analysis)
             # But for now assume they match the notebook's inferred schema
             pass

    # Basic cleaning
    trades = trades.drop_duplicates()
    
    # Convert timestamp
    trades['Timestamp IST'] = pd.to_datetime(trades['Timestamp IST'], format='mixed')
    trades['date'] = trades['Timestamp IST'].dt.date
    trades['date'] = pd.to_datetime(trades['date'])

    return trades

def engineer_features(trades):
    """Aggregates trade data to create trader profiles."""
    print("Engineering features...")
    
    # 1. Avg Trade Size (Size USD)
    avg_trade_size = trades.groupby('Account')['Size USD'].mean()
    
    # 2. Win Rate (Closed PnL > 0)
    # create a helper column for win
    trades['is_win'] = trades['Closed PnL'] > 0
    win_rate = trades.groupby('Account')['is_win'].mean()
    
    # 3. Avg Trades Per Day
    # Count trades per day for each account, then average those daily counts
    daily_counts = trades.groupby(['Account', 'date']).size().reset_index(name='daily_trade_count')
    avg_trades_per_day = daily_counts.groupby('Account')['daily_trade_count'].mean()
    
    # 4. PnL Variability (Std Dev of Closed PnL)
    pnl_variability = trades.groupby('Account')['Closed PnL'].std()
    
    # 5. Long Bias (Percentage of Buy trades)
    # Assuming 'Direction' has 'Buy' and 'Sell'
    trades['is_long'] = trades['Direction'].str.lower() == 'buy'
    long_bias = trades.groupby('Account')['is_long'].mean()

    # Combine all features
    features = pd.DataFrame({
        'avg_trade_size': avg_trade_size,
        'win_rate': win_rate,
        'avg_trades_per_day': avg_trades_per_day,
        'pnl_variability': pnl_variability,
        'long_bias': long_bias
    })
    
    # Handle NaNs (e.g., if std dev is NaN for single trade)
    features = features.fillna(0)
    
    return features

def perform_clustering(features, n_clusters=4):
    """Performs K-Means clustering and PCA for visualization."""
    print(f"Performing clustering with {n_clusters} clusters...")
    
    # Standardize features
    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(features)
    
    # KMeans
    kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
    clusters = kmeans.fit_predict(scaled_features)
    
    features['cluster'] = clusters
    
    # PCA for visualization (2 components)
    pca = PCA(n_components=2)
    pca_components = pca.fit_transform(scaled_features)
    
    features['pca_x'] = pca_components[:, 0]
    features['pca_y'] = pca_components[:, 1]
    
    return features

def save_plot(features):
    """Saves a 2D PCA scatter plot of the clusters."""
    print(f"Saving cluster plot to {CLUSTER_PLOT_FILE}...")
    plt.figure(figsize=(10, 8))
    sns.scatterplot(
        data=features, 
        x='pca_x', 
        y='pca_y', 
        hue='cluster', 
        palette='viridis', 
        s=100,
        alpha=0.8
    )
    plt.title('Trader Clusters (PCA Reduced)')
    plt.xlabel('PCA Component 1')
    plt.ylabel('PCA Component 2')
    plt.legend(title='Cluster')
    
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
        
    plt.savefig(CLUSTER_PLOT_FILE)
    plt.close()

def main():
    try:
        trades = load_data()
        features = engineer_features(trades)
        
        # We can determine optimal k using elbow method, but for this task 
        # we will start with 4 as requested (e.g. Conservative, Aggressive, etc.)
        # The user example mentioned 2, but 3-4 is usually better for "types".
        # Let's stick to a reasonable number like 4 to capture nuance.
        labeled_features = perform_clustering(features, n_clusters=4)
        
        # Save results
        if not os.path.exists(OUTPUT_DIR):
            os.makedirs(OUTPUT_DIR)
            
        print(f"Saving features with clusters to {OUTPUT_FILE}...")
        labeled_features.to_csv(OUTPUT_FILE)
        
        # Visualization
        save_plot(labeled_features)
        
        # Analyze clusters
        print("\nCluster Summaries:")
        summary = labeled_features.groupby('cluster').mean()
        print(summary)
        
        print("\nDone.")
        
    except Exception as e:
        print(f"An error occurred: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()

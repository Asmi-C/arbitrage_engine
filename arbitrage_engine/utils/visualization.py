import matplotlib.pyplot as plt
import seaborn as sns

def plot_arbitrage_signals(df: pd.DataFrame):
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=df, x='Date', y='Spread', label='Price Spread')
    plt.axhline(y=df['Spread'].mean(), color='r', linestyle='--', label='Mean')
    plt.fill_between(df['Date'], 
                    df['Spread'].mean() + df['Spread'].std(), 
                    df['Spread'].mean() - df['Spread'].std(), 
                    alpha=0.2, label='±1σ')
    plt.title("Pairs Trading Spread Analysis")
    plt.savefig('static/arbitrage.png')
import pandas as pd
from backtesting import Backtest, Strategy

class ArbitrageStrategy(Strategy):
    def init(self):
        self.signal = 0
        
    def next(self):
        price_a = self.data.Close_A[-1]
        price_b = self.data.Close_B[-1]
        
        is_arb, z = self.pairs_trader.calculate_zscore(price_a, price_b)
        if is_arb:
            self.signal = self.pairs_trader.generate_signal(z)
            if self.signal == 1:
                self.buy(sl=price_a * 0.99, tp=price_a * 1.01)
            elif self.signal == -1:
                self.sell(sl=price_b * 1.01, tp=price_b * 0.99)

def run_backtest(data: pd.DataFrame):
    bt = Backtest(data, ArbitrageStrategy, commission=.002)
    stats = bt.run()
    print(f"Sharpe: {stats['Sharpe Ratio']:.2f}")
    return stats
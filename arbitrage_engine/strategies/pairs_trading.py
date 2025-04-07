import numpy as np
from typing import Tuple

class PairsTrader:
    def __init__(self, z_score_threshold: float = 2.0):
        self.threshold = z_score_threshold
        self.spread_mean = None
        self.spread_std = None
    
    def calculate_zscore(self, price_a: float, price_b: float) -> Tuple[bool, float]:
        spread = np.log(price_a) - np.log(price_b)
        if self.spread_mean is None:
            self.spread_mean = spread
            self.spread_std = 1e-3  # Avoid division by zero
        z_score = (spread - self.spread_mean) / self.spread_std
        return (abs(z_score) > self.threshold, z_score)
    
    def generate_signal(self, z_score: float) -> int:
        return 1 if z_score < -self.threshold else -1 if z_score > self.threshold else 0
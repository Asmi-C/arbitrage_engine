from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.linear_model import LinearRegression
import numpy as np

class ArbitragePredictor:
    def __init__(self):
        self.models = {
            "XGBoost": GradientBoostingRegressor(),
            "RandomForest": RandomForestRegressor(n_estimators=100),
            "OLS": LinearRegression()
        }
    
    def train(self, X: np.ndarray, y: np.ndarray):
        """Train all models with walk-forward validation"""
        for name, model in self.models.items():
            model.fit(X[:-100], y[:-100])  # Leave last 100 points for testing
            score = model.score(X[-100:], y[-100:])
            print(f"{name} R²: {score:.4f}")
    
    def predict(self, X: np.ndarray) -> dict:
        return {name: model.predict(X) for name, model in self.models.items()}
import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt


class EfficientFrontier:
    def __init__(self, ticker_list):
        self.ticker_list = ticker_list
        self.df = pd.DataFrame
        self.simulations = 40000

    def ImportFromYahooFinance(self):
        self.df = yf.download(self.ticker_list, period="1y", interval="1d")
        self.df = self.df.iloc[:, 0:4]

    def MathsMethods(self):
        np.random.seed(42)
        log_returns = np.log(self.df / self.df.shift(1))
        self.all_weights = np.zeros((self.simulations, len(self.df.columns)))
        self.return_array = np.zeros(self.simulations)
        self.vol_array = np.zeros(self.simulations)
        self.sharpe_array = np.zeros(self.simulations)

        for x in range(self.simulations):
            weights = np.array(np.random.random(len(self.df.columns)))
            weights = weights / np.sum(weights)
            self.all_weights[x, :] = weights
            self.return_array[x] = np.sum((log_returns.mean() * weights * 252))
            self.vol_array[x] = np.sqrt(np.dot(weights.T, np.dot(log_returns.cov() * 252, weights)))
            self.sharpe_array[x] = self.return_array[x] / self.vol_array[x]

    def Findings(self):
        position = self.sharpe_array.argmax()
        max_sharpe_ratio = (self.sharpe_array.max())
        print(f"The optimal Sharpe Ratio is: {max_sharpe_ratio}")

        optimal_weights = self.all_weights[position, :]
        print(f"The weights are: {optimal_weights}")

        optimal_returns = self.return_array[self.sharpe_array.argmax()]
        print(f"The optimal return is: {optimal_returns}")

        optimal_vol = self.vol_array[self.sharpe_array.argmax()]
        print(f"The optimal volatility is: {optimal_vol}")

        plt.style.use('dark_background')
        plt.figure(figsize=(12, 8))
        plt.scatter(self.vol_array, self.return_array, c=self.sharpe_array, cmap='viridis')
        plt.colorbar(label='Sharpe Ratio')
        plt.xlabel('Volatility')
        plt.ylabel('Return')
        plt.show()

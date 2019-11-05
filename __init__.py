import yfinance as yf
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt

tech_stocks = ("APT.AX","XRO.AX","NEA.AX","EML.AX")
data = yf.download(tech_stocks, period="1y",interval="1d")
df = data.iloc[:,0:4]

plt.figure(figsize=(14, 7))
for c in df.columns.values:
    plt.plot(df.index, df[c], lw=3, alpha=0.8,label=c)
plt.legend(loc='upper left', fontsize=12)
plt.ylabel('price in $')

log_ret = np.log(df/df.shift(1))
np.random.seed(42)
num_ports = 10000
all_weights = np.zeros((num_ports, len(df.columns)))
ret_arr = np.zeros(num_ports)
vol_arr = np.zeros(num_ports)
sharpe_arr = np.zeros(num_ports)

for x in range(num_ports):
    # Weights
    weights = np.array(np.random.random(4))
    weights = weights/np.sum(weights)
    all_weights[x,:] = weights
    
    # Expected return
    ret_arr[x] = np.sum( (log_ret.mean() * weights * 252))
    
    # Expected volatility
    vol_arr[x] = np.sqrt(np.dot(weights.T, np.dot(log_ret.cov()*252, weights)))
    
    # Sharpe Ratio
    sharpe_arr[x] = ret_arr[x]/vol_arr[x]


# Highest sharpe ratio and location in array
max_sharpe_ratio = (sharpe_arr.max())
print (max_sharpe_ratio)
position = sharpe_arr.argmax()
print (position) 

# Print weights, returns and volatility
optimal_weights = all_weights[position,:]
print (optimal_weights)
optimal_returns = ret_arr[sharpe_arr.argmax()]
print (optimal_returns)
optimal_vol = vol_arr[sharpe_arr.argmax()]
print (optimal_vol)

optimal_weights = all_weights[position,:]
print (optimal_weights)
optimal_returns = ret_arr[sharpe_arr.argmax()]
print (optimal_returns)
optimal_vol = vol_arr[sharpe_arr.argmax()]
print (optimal_vol)

plt.figure(figsize=(12,8))
plt.scatter(vol_arr, ret_arr, c=sharpe_arr, cmap='viridis')
plt.colorbar(label='Sharpe Ratio')
plt.xlabel('Volatility')
plt.ylabel('Return')
plt.show()






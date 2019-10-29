import yfinance as yf
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt

banks = ("NAB.AX","WBC.AX","CBA.AX","ANZ.AX","MQG.AX")
data = yf.download(banks, period="max",interval="1d")
df = data.iloc[:,0:5]

#Calculate historical VaR
#Calculate Standard Deviation VaR

log_ret = np.log(df/df.shift(1))

np.random.seed(42)
num_ports = 10000
all_weights = np.zeros((num_ports, len(df.columns)))
ret_arr = np.zeros(num_ports)
vol_arr = np.zeros(num_ports)
sharpe_arr = np.zeros(num_ports)

for x in range(num_ports):
    # Weights
    weights = np.array(np.random.random(5))
    weights = weights/np.sum(weights)
    all_weights[x,:] = weights
    
    # Expected return
    ret_arr[x] = np.sum( (log_ret.mean() * weights * 252))
    
    # Expected volatility
    vol_arr[x] = np.sqrt(np.dot(weights.T, np.dot(log_ret.cov()*252, weights)))
    
    # Sharpe Ratio
    sharpe_arr[x] = ret_arr[x]/vol_arr[x]


plt.figure(figsize=(12,8))
plt.scatter(vol_arr, ret_arr, c=sharpe_arr, cmap='viridis')
plt.colorbar(label='Sharpe Ratio')
plt.xlabel('Volatility')
plt.ylabel('Return')
plt.show()



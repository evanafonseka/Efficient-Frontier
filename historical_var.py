import pandas as pd
import os
import matplotlib.pyplot as plt
from __init__ import *

# Holding of $1,000,000 in optimal weights
total_p = optimal_weights * 1000000
holdings = {'Stocks':['ANZ.AX', 'CBA.AX','MQG.AX','NAB.AX','WBC.AX'], 
        'Quantity':[total_p]}

df = df
log_ret = np.log(df/df.shift(1))

# Market to market
port_val = log_ret * total_p 
port_val['Portfolio Value'] = port_val.sum(axis=1)

# Sorting values
port_rets = port_val['Portfolio Value']
port_rets = port_rets.sort_values(axis=0, ascending=True)
var = np.percentile(port_rets, 1)

# Creation of Histogram
plt.hist(port_rets,normed=True)
plt.xlabel('Portfolio Dollar Returns')
plt.ylabel('Frequency')
plt.title(r'Histogram of Portfolio Dollar Returns', fontsize=18, fontweight='bold')
plt.axvline(x=var, color='r', linestyle='--', label='Price at Confidence Interval: ' + str(round(var, 1)))
plt.legend(loc='upper right', fontsize = 'x-small')
plt.show()

print ("At a 99% confidence level the worst possible outcome is: " + str(round(var, 2)))





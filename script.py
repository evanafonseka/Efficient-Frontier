import pandas as pd  
import matplotlib.pyplot as plt
from functools import reduce

# Uploading the CSV's fromyahoo finance
anz = pd.read_csv(r'/Users/evanfonseka/Desktop/dev/efficient_frontier/anz.ax.csv')
cba = pd.read_csv(r'/Users/evanfonseka/Desktop/dev/efficient_frontier/cba.ax.csv')
mqg = pd.read_csv(r'/Users/evanfonseka/Desktop/dev/efficient_frontier/mqg.ax.csv')
nab = pd.read_csv(r'/Users/evanfonseka/Desktop/dev/efficient_frontier/nab.ax.csv')
wbc = pd.read_csv(r'/Users/evanfonseka/Desktop/dev/efficient_frontier/wbc.ax.csv')

# Cleaning up the data
anz = anz.drop(["Open","High","Low","Close","Volume"], axis=1)
anz = anz.rename(columns={"Adj Close": "ANZ"})

cba = cba.drop(["Open","High","Low","Close","Volume",], axis=1)
cba = cba.rename(columns={"Adj Close": "CBA"})

mqg = mqg.drop(["Open","High","Low","Close","Volume",], axis=1)
mqg = mqg.rename(columns={"Adj Close": "MQG"})

nab = nab.drop(["Open","High","Low","Close","Volume",], axis=1)
nab = nab.rename(columns={"Adj Close": "NAB"})

wbc = wbc.drop(["Open","High","Low","Close","Volume",], axis=1)
wbc = wbc.rename(columns={"Adj Close": "WBC"})



# Join all 5 dataframes on "Date"
dfs = [anz, cba, mqg, nab, wbc]
df = reduce(lambda left,right: pd.merge(left,right,on='Date'), dfs)
date = df.iloc[:,0:1]

#Calculating %change for each stock
no_date = df.iloc[:,1:]
returns = no_date.pct_change()


# calculate daily and annual returns of the stocks
returns_daily = no_date.pct_change()
returns_annual = returns_daily.mean() * 252
selected = returns_annual.index.get_level_values(0).values

# get daily and covariance of returns of the stock
cov_daily = returns_daily.cov()
cov_annual = cov_daily * 252

# empty lists to store returns, volatility and weights of imiginary portfolios
port_returns = []
port_volatility = []
stock_weights = []

# set the number of combinations for imaginary portfolios
num_assets = len(selected)
num_portfolios = 100000

# populate the empty lists with each portfolios returns,risk and weights
for single_portfolio in range(num_portfolios):
    weights = np.random.random(num_assets)
    weights /= np.sum(weights)
    returns = np.dot(weights, returns_annual)
    volatility = np.sqrt(np.dot(weights.T, np.dot(cov_annual, weights)))
    port_returns.append(returns)
    port_volatility.append(volatility)
    stock_weights.append(weights)

# a dictionary for Returns and Risk values of each portfolio
portfolio = {'Returns': port_returns,
             'Volatility': port_volatility}

# extend original dictionary to accomodate each ticker and weight in the portfolio
for counter,symbol in enumerate(selected):
    portfolio[symbol+' weight'] = [weight[counter] for weight in stock_weights]

# make a dataframe of the extended dictionary
df2 = pd.DataFrame(portfolio)

# get better labels for desired arrangement of columns
column_order = ['Returns', 'Volatility'] + [stock+' weight' for stock in selected]

# reorder dataframe columns
df3  = df2[column_order]

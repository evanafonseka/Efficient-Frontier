#yfinance wrapper

import yfinance as yf

banks = ("NAB.AX","WBC.AX","CBA.AX","ANZ.AX","MQG.AX")
data = yf.download(banks, period="60d",interval="5m")
df = data.iloc[:,0:5]


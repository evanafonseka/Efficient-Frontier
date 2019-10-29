#yfinance wrapper

import yfinance as yf

banks = ("NAB.AX","ANZ.AX","CBA.AX","ANZ.AX","MQG.AX")
data = yf.download(banks, period="60d",interval="1m")

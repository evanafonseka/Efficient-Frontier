# Efficient-Frontier: Applying financial theory to code

Throughout my university life there has always been an emphasis on finding the efficient frontier with regards to investing. It is simpy an optimal portfolio where it is appleaing to all risk averse investors (low risk, high return). The core idea of this calulation is to find the optimal weights of each stock that form an ideal portfolio with the highest Sharpe Ratio.
### Stock selection taken from Motley Fool

#### Portfolio consisting of the Top 4 ASX tech stocks for 2019: Afterpay, EML Payments, Nearmap and Xero

![tech_performance](https://user-images.githubusercontent.com/49772033/68191506-cea45700-0003-11ea-83ab-d2cc06c7a4dc.png)


- Data is pulled from Yahoo Finance
- Frequency = Daily Adjusted Close
- Period is from T-1year

###### Ran 10,000 possible outcomes to find the optimal weighting with the highest sharpe ratio

## Findings
#### Sharpe Ratio = 2.65
#### Return = 82.44%
#### Standard deviation = 31.13%

|Stock | Optimal Weight | 
|:----:|:-----:|
|APT.AX|8.1%|
|EML.AX|57.8%|
|NEA.AX|10.9%|
|XRO.AX|23.3%|

![tech_frontier](https://user-images.githubusercontent.com/49772033/68191433-a4eb3000-0003-11ea-9088-7c44dfc16dc1.png)





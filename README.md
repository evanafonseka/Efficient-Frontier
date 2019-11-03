# Efficient-Frontier: Applying financial theory to code

Throughout my university life there has always been an emphasis on finding the efficient frontier with regards to investing. It is simpy an optimal portfolio where it is appleaing to all risk averse investors (low risk, high return). The core idea of this calulation is to find the optimal weights of each stock that form an ideal portfolio with the highest Sharpe Ratio.

Portfolio consisting of the "Big 5" banks in Australia: ANZ, CBA, MQG, NAB and WBC.

![historical_performance](https://user-images.githubusercontent.com/49772033/67761229-00af3980-fa97-11e9-86e9-c21df9dd7452.png)





- Data is pulled from Yahoo Finance
- Frequency = Daily Adjusted Close
- Period Start = 1988-01-29	
- Period End = Today

Takes into account:
- Standard Deviation
- Expected Return
- Sharpe Ratio
- Ran 10,000 possible outcomes to find the optimal weighting with the highest sharpe ratio

## Findings

|Stock | Optimal Weight | 
|:----:|:-----:|
|ANZ.AX|9.7%|
|CBA.AX|54.8%|
|MQG.AX|23.4%|
|NAB.AX|5.4%|
|WBC.AX|6.7%|



![efficient_frontier](https://user-images.githubusercontent.com/49772033/67842691-c3a67e00-fb4e-11e9-8375-d434966b2579.png)






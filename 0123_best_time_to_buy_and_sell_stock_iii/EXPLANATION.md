# How We Solve Best Time to Buy and Sell Stock III

At most two transactions with four running states.

## Steps

1. Track the cheapest buy for the first trade.
2. Track the best profit after selling the first trade.
3. Treat the second buy as price minus first-trade profit.
4. Track the best profit after the second sell.
5. Return the second-sell profit.

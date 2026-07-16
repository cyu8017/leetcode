# How We Solve Best Time to Buy and Sell Stock IV

DP over at most `k` transactions, with an unlimited-trade shortcut.

## Steps

1. If `k` is large, sum every upward day-to-day gain.
2. Otherwise keep buy/sell states for each transaction count.
3. Update buy as the cheapest effective purchase after prior profit.
4. Update sell as the best profit after selling that purchase.
5. Return the profit after `k` sells.

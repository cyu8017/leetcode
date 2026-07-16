# How We Solve Best Time to Buy and Sell Stock II

Unlimited trades: take every upward day-to-day gain.

## Steps

1. Walk consecutive price pairs.
2. Whenever today is higher than yesterday, add the difference.
3. Skip flat or down moves.
4. Summing all rises equals the optimal multi-trade profit.
5. Return that sum.

# How We Solve Best Time to Buy and Sell Stock

One buy and one sell: track the lowest price so far and the best profit.

## Steps

1. Keep the minimum price seen so far.
2. For each later price, compute price minus that minimum.
3. Update the best profit when the gap is larger.
4. Update the minimum when a cheaper day appears.
5. Return the best profit (or 0 if none).

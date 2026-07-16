# How We Solve Best Time to Buy and Sell Stock with Cooldown

Track three states: free, holding, and cooldown after selling.

## Steps

1. Iterate prices while updating free, hold, and cooldown profits.
2. Buying moves from free to hold; selling moves from hold to cooldown.
3. Return the best profit among free and cooldown at the end.

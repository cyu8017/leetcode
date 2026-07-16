# How We Solve Ones and Zeroes

0/1 knapsack with two capacities: maximum strings using at most m zeros and n ones.

## Steps

1. Count zeros and ones in each string.
2. Update a 2D DP table from back to front for each string.
3. Return the maximum number of strings chosen.

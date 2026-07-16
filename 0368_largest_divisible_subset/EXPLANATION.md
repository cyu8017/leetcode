# How We Solve Largest Divisible Subset

Sorted DP extends chains when larger values divide the previous one.

## Steps

1. Sort nums ascending.
2. For each value, extend any valid smaller divisor chain.
3. Keep the longest chain found.

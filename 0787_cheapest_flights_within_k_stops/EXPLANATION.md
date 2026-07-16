# How We Solve Cheapest Flights Within K Stops

Bellman-Ford for at most `k+1` edges (≤ `k` stops).

## Steps

1. Initialize distances with `src = 0`.
2. Relax all flights for `k+1` rounds on a copied array.
3. Return `dst` distance, or `-1` if still infinite.

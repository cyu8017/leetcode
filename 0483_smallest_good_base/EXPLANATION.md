# How We Solve Smallest Good Base

Search for a base k whose geometric series 1 + k + k² + … equals n.

## Steps

1. Try series lengths from large to small (high exponent first).
2. Binary search base k for each length using the partial sum.
3. Return the first valid k; fallback is n − 1.

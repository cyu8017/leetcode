# How We Solve Guess Number Higher or Lower

Binary search on the answer range using the guess API.

## Steps

1. Maintain left and right bounds on 1..n.
2. Guess the midpoint and read -1, 0, or 1.
3. Narrow the range until the pick is found.

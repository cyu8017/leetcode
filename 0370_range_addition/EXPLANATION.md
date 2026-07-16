# How We Solve Range Addition

A difference array applies range increments in constant time.

## Steps

1. Add inc at start and subtract inc after end for each update.
2. Prefix-sum the difference array.
3. Return the final modified array.

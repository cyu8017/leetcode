# How We Solve Maximum Product Subarray

Track both the running max and min products because negatives can flip them.

## Steps

1. Seed best, max, and min with the first value.
2. For each next number, consider itself and products with the old max/min.
3. Update the running max and min from those candidates.
4. Keep the global best product seen so far.
5. Return that best value.

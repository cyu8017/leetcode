# How We Solve Patching Array

Greedy patching extends the reachable range [1, miss).

## Steps

1. While miss is at most n, use the next sorted number if it fits.
2. Otherwise add a patch equal to miss and increment patch count.
3. Extend miss by the added value each step.

# How We Solve Random Pick with Weight

Prefix sums turn weighted choice into one binary search.

## Steps

1. Build cumulative weights during construction.
2. Draw a random integer in `[0, total)`.
3. Binary search the prefix array for the chosen index.

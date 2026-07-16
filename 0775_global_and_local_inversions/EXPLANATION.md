# How We Solve Global and Local Inversions

Ideal iff no number is more than one index away from its value.

## Steps

1. Local inversions are adjacent swaps only.
2. A global non-local inversion means `|nums[i]-i| > 1`.
3. Check that bound for every index.

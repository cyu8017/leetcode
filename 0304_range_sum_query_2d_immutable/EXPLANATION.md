# How We Solve Range Sum Query 2D Immutable

Two-dimensional prefix sums support rectangle queries.

## Steps

1. Build a cumulative sum table with inclusion-exclusion.
2. Query any sub-rectangle using four prefix lookups.

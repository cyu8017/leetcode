# How We Solve Range Sum Query Immutable

Prefix sums answer range queries in constant time.

## Steps

1. Build a prefix array during construction.
2. Return prefix[right+1] minus prefix[left] for each query.

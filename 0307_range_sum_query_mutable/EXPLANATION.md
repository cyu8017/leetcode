# How We Solve Range Sum Query Mutable

A Fenwick tree supports point updates and prefix range sums.

## Steps

1. Initialize the BIT from the input array.
2. Apply updates as deltas to a single index.
3. Answer range sums with two prefix queries.

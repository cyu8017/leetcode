# How We Solve Insert Delete GetRandom O(1)

Array plus index map enables swap-delete in constant time.

## Steps

1. insert appends and records index in a hash map.
2. remove swaps the target with the last element and pops.
3. getRandom reads from the backing array in O(1).

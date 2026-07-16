# How We Solve Insert Delete GetRandom O(1) - Duplicates Allowed

Track every index per value so duplicates can coexist in the array.

## Steps

1. insert always appends; return false when the value already existed.
2. remove swaps one occurrence with the tail and updates all index sets.
3. getRandom samples from the backing array in O(1).

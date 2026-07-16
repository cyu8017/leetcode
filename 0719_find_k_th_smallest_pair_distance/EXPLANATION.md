# How We Solve Find K-th Smallest Pair Distance

Binary search the distance; count how many pairs are ≤ mid.

## Steps

1. Sort `nums`.
2. For a candidate distance, two-pointer count pairs within that distance.
3. Shrink until the smallest distance with at least `k` pairs.

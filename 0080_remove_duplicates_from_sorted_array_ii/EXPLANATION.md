# How We Solve Remove Duplicates from Sorted Array II

Keep at most two copies of each value in a sorted array.

## Steps

1. If length is 2 or less, return the length.
2. The first two spots are always kept.
3. For each later value, compare with the value two spots back.
4. If different, write it to the next open spot.
5. Return how many spots were used.

# How We Solve Array Partition

Sorting pairs adjacent values so each pair contributes its smaller half optimally.

## Steps

1. Sort the array.
2. Sum every even-indexed element after sorting.
3. That sum is the maximum of all `min(a, b)` pairings.

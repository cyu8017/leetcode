# How We Solve Kth Largest Element in an Array

Quickselect partitions around a pivot until the kth largest lands in place.

## Steps

1. Convert k to the target index `len(nums) - k`.
2. Pick a random pivot and partition the array.
3. If the pivot index equals the target, return that value.
4. Recurse on the left or right side depending on the pivot index.
5. Repeat until the target index is found.

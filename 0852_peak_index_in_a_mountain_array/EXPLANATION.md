# How We Solve Peak Index in a Mountain Array

Binary search for the unique peak.

## Steps

1. Compare `arr[mid]` with `arr[mid+1]`.
2. Ascending → peak is to the right; else peak is at/left of mid.
3. Converge to the peak index.

# How We Solve Find K Closest Elements

Binary search the left edge of a window of length `k` in the sorted array.

## Steps

1. Search `left` in `[0, n-k]` for the best window start.
2. Prefer the window whose right end is closer when `x - arr[mid] > arr[mid+k] - x`.
3. Return `arr[left:left+k]`.

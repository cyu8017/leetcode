# How We Solve Remove Boxes

Dynamic programming tracks the best score for a range with trailing same-color boxes.

## Steps

1. Define `dp(l, r, k)` as the max points for `boxes[l..r]` plus `k` extra copies of `boxes[r]`.
2. Either remove the trailing run for `(k+1)^2` points or merge with an earlier matching box.
3. Return the memoized result for the full array.

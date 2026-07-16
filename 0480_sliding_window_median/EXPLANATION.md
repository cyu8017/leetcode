# How We Solve Sliding Window Median

Maintain a sorted window with binary search insert and delete.

## Steps

1. Sort the initial window of size `k`.
2. Slide by removing the outgoing value and inserting the incoming one with `bisect`.
3. Read the middle element(s) for each window median.

# How We Solve Shortest Unsorted Continuous Subarray

Find the farthest positions that break the running max from the left and min from the right.

## Steps

1. Scan left to right; anything below the running max belongs in the unsorted window.
2. Scan right to left; anything above the running min belongs in the window.
3. Return the window length (or 0 if already sorted).

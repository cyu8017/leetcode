# How We Solve Max Consecutive Ones II

Sliding window allows at most one zero inside the window.

## Steps

1. Expand the right pointer and count zeros in the window.
2. Shrink from the left while more than one zero is present.
3. Track the maximum window size.

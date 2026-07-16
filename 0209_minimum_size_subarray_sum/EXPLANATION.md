# How We Solve Minimum Size Subarray Sum

Expand a sliding window until the sum meets the target, then shrink it.

## Steps

1. Move the right pointer and add each value to the running sum.
2. While the sum is at least the target, record the window length.
3. Subtract the left value and advance left.
4. Keep the shortest valid length seen.
5. Return 0 if no window ever reached the target.

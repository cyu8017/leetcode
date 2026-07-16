# How We Solve Longest Substring with At Most K Distinct Characters

Sliding window shrinks when distinct character count exceeds k.

## Steps

1. Expand right and count characters in the window.
2. While distinct count is greater than k, shrink from the left.
3. Track the maximum valid window length.

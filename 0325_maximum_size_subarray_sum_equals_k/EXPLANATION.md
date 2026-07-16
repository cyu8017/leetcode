# How We Solve Maximum Size Subarray Sum Equals k

Prefix sums with earliest index map maximize subarray length.

## Steps

1. Track the first index for each prefix sum.
2. If prefix minus k was seen, update the best length.
3. Return the maximum length found.

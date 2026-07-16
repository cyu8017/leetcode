# How We Solve Find Pivot Index

Find the index where left sum equals right sum.

## Steps

1. Compute the total sum.
2. Scan left-to-right accumulating the left sum.
3. Return the first index with `left == total - left - nums[i]`.

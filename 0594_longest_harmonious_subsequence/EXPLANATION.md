# How We Solve Longest Harmonious Subsequence

A harmonious subsequence uses only some value `x` and `x + 1`.

## Steps

1. Count frequencies of every number.
2. For each value that also has `value + 1`, add the two counts.
3. Track the maximum sum.

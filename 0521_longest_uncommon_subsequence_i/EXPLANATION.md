# How We Solve Longest Uncommon Subsequence I

If the strings differ, the longer one cannot be a subsequence of the other when lengths differ; if equal, no uncommon subsequence exists.

## Steps

1. Compare the two strings for equality.
2. Return `-1` when they are identical.
3. Otherwise return the maximum length.

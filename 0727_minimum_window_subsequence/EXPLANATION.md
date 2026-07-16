# How We Solve Minimum Window Subsequence

Find each match of `s2` as a subsequence in `s1`, then shrink from the left.

## Steps

1. From a start index, scan forward until `s2` is fully matched.
2. Walk backward to the tightest start of that match.
3. Keep the shortest window; resume just after that start.

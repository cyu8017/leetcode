# How We Solve Matchsticks to Square

Partition matchsticks into four equal sides with backtracking.

## Steps

1. Reject if total length is not divisible by four.
2. Sort matchsticks descending to prune early.
3. DFS assign each stick to a side, skipping duplicate side attempts.

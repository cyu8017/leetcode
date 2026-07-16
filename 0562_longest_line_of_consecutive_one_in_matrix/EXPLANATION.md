# How We Solve Longest Line of Consecutive One in Matrix

DP tracks consecutive ones ending at each cell in four directions.

## Steps

1. For each `1`, extend horizontal, vertical, diagonal, and anti-diagonal runs.
2. Use previously computed neighbors in those directions.
3. Track the global maximum run length.

# How We Solve K-diff Pairs in an Array

Each valid pair differs by exactly `k`, and duplicate values must not create duplicate pairs.

## Steps

1. Count frequency of each number.
2. For `k > 0`, add one pair for each value whose partner `value + k` exists.
3. For `k == 0`, add one pair for each value that appears at least twice.

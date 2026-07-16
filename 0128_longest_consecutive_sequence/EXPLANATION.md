# How We Solve Longest Consecutive Sequence

Use a set and only start counting at the beginning of a streak.

## Steps

1. Insert every number into a set.
2. For each number, skip it if `num - 1` is also present.
3. Otherwise walk `num + 1`, `num + 2`, ... while they exist.
4. Track the longest streak length.
5. Return that length.

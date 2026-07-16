# How We Solve Partition to K Equal Sum Subsets

Backtrack filling `k` buckets to `sum/k`, placing largest numbers first.

## Steps

1. Fail fast if total is not divisible by `k` or a number exceeds the target.
2. Try placing each number into a bucket that still has room.
3. Skip duplicate empty-bucket branches to prune.

# How We Solve K-th Symbol in Grammar

Each row replaces `0→01` and `1→10`; recurse on the parent half.

## Steps

1. Base: row 1 is `0`.
2. If `k` is in the left half, it equals the parent symbol.
3. Otherwise it is the flip of the corresponding left-half parent symbol.

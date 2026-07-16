# How We Solve Beautiful Arrangement II

Build `1..n-k` ascending, then zigzag the remaining `k` values to create `k` distinct diffs.

## Steps

1. Emit `1, 2, …, n-k`.
2. Alternate appending high and low from the leftover range.
3. That produces exactly `k` distinct adjacent absolute differences.

# How We Solve Max Chunks To Make Sorted II

A chunk can end at `i` when `max(left[:i+1]) <= min(right[i+1:])`.

## Steps

1. Build prefix maxima and suffix minima.
2. Count every index where the prefix max ≤ next suffix min.
3. That count is the maximum number of chunks.

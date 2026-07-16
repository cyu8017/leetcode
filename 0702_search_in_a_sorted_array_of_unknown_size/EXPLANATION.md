# How We Solve Search in a Sorted Array of Unknown Size

Exponentially expand the right bound, then binary search inside the window.

## Steps

1. Grow `right` by doubling until `reader.get(right) >= target`.
2. Binary search between `right/2` and `right`.
3. Return the index on hit, else `-1` (out-of-range reads as `2^31-1`).

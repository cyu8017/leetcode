# How We Solve The Skyline Problem

Sweep building events left to right while tracking active heights in a heap.

## Steps

1. Create start events `(left, -height, right)` and end events `(right, 0, 0)`.
2. Sort events by x, with starts before ends at the same x.
3. Remove heap entries whose buildings ended before the current x.
4. Push a new active height when a building starts.
5. Append `[x, currentMax]` whenever the max height changes.

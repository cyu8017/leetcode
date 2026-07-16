# How We Solve Cut Off Trees for Golf Event

Cut trees in increasing height order; BFS between consecutive targets.

## Steps

1. Collect and sort all cells with height `> 1`.
2. From the current position, BFS to the next tree (avoiding zeros).
3. Accumulate steps; return `-1` if any target is unreachable.

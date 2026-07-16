# How We Solve Circular Array Loop

Detect a cycle that moves in one direction only and has length greater than one.

## Steps

1. For each unvisited index, run fast/slow pointers with consistent direction.
2. Reject cycles of length one or direction changes mid-loop.
3. Mark exhausted paths by zeroing visited indices.

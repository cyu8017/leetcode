# How We Solve Bus Routes

BFS on stops; taking a bus explores all of its stops as one step.

## Steps

1. Map each stop to the buses that include it.
2. From the current stop, board unseen buses and enqueue new stops.
3. Return buses taken when `target` is reached, else `-1`.

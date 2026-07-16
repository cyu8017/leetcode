# How We Solve Escape The Ghosts

You escape iff you reach the target strictly sooner than every ghost.

## Steps

1. Compute your Manhattan distance from origin to target.
2. Compare each ghost’s Manhattan distance to the target.
3. Succeed only if every ghost is strictly farther.

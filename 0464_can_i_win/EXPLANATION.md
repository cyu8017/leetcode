# How We Solve Can I Win

Two players pick unused integers from 1..n; use bitmask memoization for game states.

## Steps

1. If the desired total is unreachable by the full sum, the first player loses.
2. Represent chosen numbers as a bitmask state.
3. Memoize whether the current player can force a win from each state.

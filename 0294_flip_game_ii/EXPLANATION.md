# How We Solve Flip Game II

Memoized game theory: a position wins if any move leaves the opponent losing.

## Steps

1. Try every valid flip from the current state.
2. If a move leads to a state the opponent cannot win, return true.
3. Memoize each state to avoid recomputation.
4. Return false when no winning move exists.

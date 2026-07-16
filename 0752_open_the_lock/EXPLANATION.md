# How We Solve Open the Lock

BFS over 4-digit lock states, skipping dead ends.

## Steps

1. Start from `"0000"`; each move turns one wheel ±1.
2. Ignore visited states and deadends.
3. Return steps to `target`, or `-1` if unreachable.

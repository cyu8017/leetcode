# How We Solve Gas Station

If total gas covers total cost, the unique start is after the worst prefix tank.

## Steps

1. Track overall surplus and the current tank from a candidate start.
2. Add `gas[i] - cost[i]` at each station.
3. When the tank goes negative, reset start to `i + 1` and tank to 0.
4. After one pass, succeed only if total surplus is non-negative.
5. Return that start index, or -1.

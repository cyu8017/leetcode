# How We Solve Frog Jump

Track reachable jump sizes at each stone with a DP set.

## Steps

1. Map every stone to the jump lengths that can land there.
2. From each jump k, try k-1, k, and k+1 forward.
3. Succeed when the last stone receives any jump.

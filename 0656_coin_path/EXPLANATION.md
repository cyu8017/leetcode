# How We Solve Coin Path

Backward DP for minimum cost to the last coin, preferring the lexicographically smallest path.

## Steps

1. From each index `i`, try jumps up to `maxJump` to reachable `j` with finite cost.
2. Keep the cheapest next hop (and smallest `j` on ties).
3. Reconstruct the 1-indexed path from index 0, or return `[]` if unreachable.

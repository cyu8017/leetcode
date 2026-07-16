# How We Solve K-Similar Strings

BFS over swaps that fix the first mismatched position.

## Steps

1. From the current string, find the first index differing from the target.
2. Swap with later positions that hold the needed character.
3. Shortest path length in this graph is `k`.

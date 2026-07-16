# How We Solve Flood Fill

DFS/BFS from the start pixel, recoloring the connected same-color region.

## Steps

1. If the start color already matches the new color, return immediately.
2. Recursively paint 4-neighbors that still have the original color.
3. Return the mutated image.

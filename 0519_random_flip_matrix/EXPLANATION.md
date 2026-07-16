# How We Solve Random Flip Matrix

Swap-and-pop on remaining cell indices gives uniform random flips.

## Steps

1. Keep a list of unused flattened indices.
2. Pick a random index, map it to `(row, col)`, and swap-remove it.
3. `reset` rebuilds the full index list.

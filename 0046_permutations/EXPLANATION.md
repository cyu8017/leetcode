# How We Solve Permutations

Make every order of the numbers (all permutations).

## Steps

1. Keep a path list and a used[] checklist.
2. If path is full, save a copy in the answer list.
3. Try each number index from left to right.
4. Skip numbers already used.
5. Mark used, add to path, go deeper, then undo (backtrack).
6. Return all saved orders.

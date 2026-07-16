# How We Solve Loud and Rich

DFS with memoization over the "richer than" graph.

## Steps

1. Edge `b → a` means `a` is richer than `b`.
2. For each person, answer is the quietest among themselves and richer people.
3. Memoize so each subtree is computed once.

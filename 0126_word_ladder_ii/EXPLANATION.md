# How We Solve Word Ladder II

BFS builds parent links for every shortest step, then DFS rebuilds paths.

## Steps

1. BFS from the begin word, generating one-letter neighbors.
2. Record parents only on the first level a word is reached.
3. Stop once the end word appears in a level.
4. DFS from the end word back through parents to the begin word.
5. Reverse each path and return all shortest ladders.

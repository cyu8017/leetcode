# How We Solve Word Squares

Build word squares row by row with a prefix map so each next word matches required column prefixes.

## Steps

1. Index words by every prefix they contain.
2. DFS row by row, forming the prefix from column letters chosen so far.
3. Try every word matching that prefix and backtrack when the square is complete.

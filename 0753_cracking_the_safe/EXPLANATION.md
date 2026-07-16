# How We Solve Cracking the Safe

Hierholzer’s algorithm builds a de Bruijn sequence for length-`n` passwords over `k` digits.

## Steps

1. Nodes are `(n-1)`-length prefixes; edges append one digit.
2. DFS unused edges and record digits on the way back.
3. Append the start prefix to finish the sequence.

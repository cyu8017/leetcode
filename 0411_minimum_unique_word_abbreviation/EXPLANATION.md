# How We Solve Minimum Unique Word Abbreviation

DFS builds abbreviations and keeps the shortest valid unique one.

## Steps

1. Match abbreviations against target and dictionary words with two pointers.
2. Recursively choose to skip or reveal each target character.
3. Return the shortest valid abbreviation, breaking ties lexicographically.

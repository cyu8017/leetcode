# How We Solve Implement Magic Dictionary

Store the dictionary; accept a query iff exactly one character differs from some word.

## Steps

1. `buildDict` keeps the word list.
2. `search` compares equal-length words characterwise.
3. Return true when the Hamming distance is exactly one.

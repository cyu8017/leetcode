# How We Solve Longest Word in Dictionary

Build words only if every prefix is also in the dictionary.

## Steps

1. Sort words (shorter first; ties lexicographic).
2. Keep a set of buildable words starting from `""`.
3. Accept a word when `word[:-1]` is buildable; track the longest (first wins ties).

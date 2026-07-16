# How We Solve Expressive Words

Compare run-length groups; stretches are valid only when the query run length is ≥ 3.

## Steps

1. Compress `s` and each word into `(char, count)` runs.
2. Runs must align on characters.
3. Word run ≤ query run, and unequal runs require query count ≥ 3.

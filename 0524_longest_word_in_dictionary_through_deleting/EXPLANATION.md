# How We Solve Longest Word in Dictionary through Deleting

Pick the longest dictionary word that is a subsequence of `s`, breaking ties lexicographically.

## Steps

1. Test each dictionary word as a subsequence of `s`.
2. Prefer longer matches, then smaller strings.
3. Return the best word found.

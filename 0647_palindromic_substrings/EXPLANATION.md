# How We Solve Palindromic Substrings

Expand around every center for odd- and even-length palindromes.

## Steps

1. For each index, expand while characters match.
2. Do the same for centers between adjacent indices.
3. Count every successful expansion.

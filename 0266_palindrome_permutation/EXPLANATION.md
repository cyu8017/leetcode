# How We Solve Palindrome Permutation

A string can permute into a palindrome when at most one character count is odd.

## Steps

1. Count each letter frequency.
2. Count how many letters have odd frequency.
3. Return true if that count is 0 or 1.
4. Otherwise return false.

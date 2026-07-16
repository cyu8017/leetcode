# How We Solve Longest Palindromic Substring

A palindrome reads the same forward and backward (like "aba").

## Steps

1. Try every letter as the middle of a palindrome.
2. Grow outward while both sides match.
3. Also try between two letters (even-length palindromes).
4. Remember the longest palindrome found.
5. Return that substring.

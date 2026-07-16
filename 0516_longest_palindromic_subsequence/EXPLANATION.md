# How We Solve Longest Palindromic Subsequence

Interval DP builds palindrome length inside each substring.

## Steps

1. Base case: single characters have length 1.
2. If ends match, add 2 to the inner interval result.
3. Otherwise take the better of dropping either end.

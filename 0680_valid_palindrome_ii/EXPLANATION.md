# How We Solve Valid Palindrome II

Allow one deletion: on the first mismatch, try skipping either side.

## Steps

1. Two-pointer scan while characters match.
2. On mismatch, check whether `s[l+1..r]` or `s[l..r-1]` is a palindrome.
3. Otherwise the string is already a palindrome.

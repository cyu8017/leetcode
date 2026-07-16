# How We Solve Palindrome Partitioning II

Precompute palindrome spans, then DP the minimum cuts to reach each index.

## Steps

1. Build a boolean table of every palindromic substring.
2. Let `cuts[i]` be the fewest cuts needed for `s[0..i]`.
3. If `s[0..i]` itself is a palindrome, `cuts[i] = 0`.
4. Otherwise try every split `j` where `s[j+1..i]` is a palindrome.
5. Return `cuts[n-1]`.

# How We Solve Shortest Palindrome

Find the longest palindromic prefix, then prepend the reverse of the remaining suffix.

## Steps

1. Build `s + "#" + reverse(s)`.
2. Compute the KMP prefix function on that string.
3. The last LPS value is the longest palindromic prefix length.
4. Reverse the suffix after that prefix.
5. Prepend that reversed suffix to `s`.

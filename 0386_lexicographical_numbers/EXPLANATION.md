# How We Solve Lexicographical Numbers

DFS over a 1-9 trie visits numbers in dictionary order.

## Steps

1. Start DFS from 1.
2. Append the current number, then explore current * 10.
3. If the last digit is below 9, also explore current + 1.

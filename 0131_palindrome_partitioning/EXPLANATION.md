# How We Solve Palindrome Partitioning

Backtrack every cut that leaves a palindrome prefix of the remaining string.

## Steps

1. Start DFS at index 0 with an empty path.
2. Try every end index and keep the slice only if it is a palindrome.
3. Recurse from the next index with that slice appended.
4. When the start reaches the end, record a complete partition.
5. Backtrack by popping after each recursive call.

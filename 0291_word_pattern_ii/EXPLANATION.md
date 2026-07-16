# How We Solve Word Pattern II

Backtrack over pattern characters and string splits with bijective mapping.

## Steps

1. If the pattern is exhausted, succeed only when the string is too.
2. If the current character already maps to a word, verify the prefix match.
3. Otherwise try every non-empty substring and assign a new word when unused.
4. Undo assignments on failure and continue searching.

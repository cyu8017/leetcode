# How We Solve Word Break II

Memoized DFS builds every sentence that segments the suffix.

## Steps

1. Put dictionary words in a set.
2. From each start index, try every dictionary word that matches a prefix.
3. Recurse on the remaining suffix and prepend the word to each continuation.
4. Memoize the list of sentences for each start index.
5. Return the sentences for index 0.

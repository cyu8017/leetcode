# How We Solve Word Ladder

BFS finds the shortest transformation length.

## Steps

1. Put the word list into a set for O(1) lookups.
2. Queue the begin word with length 1.
3. Expand every one-letter neighbor still in the set.
4. Mark words visited as they are enqueued.
5. Return the length when the end word is reached, else 0.

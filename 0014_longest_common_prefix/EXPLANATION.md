# How We Solve Longest Common Prefix

Find the shared start of all words (like "flower", "flow", "flight" -> "fl").

## Steps

1. Use the first word as the prefix guess.
2. Compare letter by letter with every other word.
3. When letters differ, cut the prefix shorter.
4. If prefix becomes empty, stop early.
5. After all words, return the prefix left.

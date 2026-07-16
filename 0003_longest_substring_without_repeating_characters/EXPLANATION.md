# How We Solve Longest Substring Without Repeating Characters

Find the **longest part** of a word where no letter repeats.

## Steps

1. Use two fingers: left and right on the word.
2. Move the right finger and grow the window.
3. If a letter repeats, move the left finger until the repeat is gone.
4. After each move, check if this window is the longest so far.
5. Keep sliding until the right finger reaches the end.
6. Return the best length.

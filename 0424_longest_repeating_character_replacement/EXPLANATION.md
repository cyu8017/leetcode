# How We Solve Longest Repeating Character Replacement

Use a sliding window that stays valid while replacements needed are at most `k`.

## Steps

1. Expand the right edge and track character frequencies in the window.
2. Keep the count of the dominant character in the window.
3. Shrink from the left while `(window size - dominant count) > k`.
4. Record the longest valid window length.

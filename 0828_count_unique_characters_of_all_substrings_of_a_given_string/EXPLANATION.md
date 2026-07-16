# How We Solve Unique Letter String

For each occurrence of a character, count substrings where it is unique.

## Steps

1. Record all positions of each letter (with sentinels `-1` and `n`).
2. Contribution at index `i` is `(i - prev) * (next - i)`.
3. Sum contributions over all occurrences.

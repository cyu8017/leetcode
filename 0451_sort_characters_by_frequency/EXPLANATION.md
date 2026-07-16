# How We Solve Sort Characters By Frequency

Count characters, then emit them from highest frequency to lowest.

## Steps

1. Build a frequency map for the string.
2. Sort characters by descending count, breaking ties by character code.
3. Repeat each character according to its count and concatenate.

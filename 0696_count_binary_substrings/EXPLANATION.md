# How We Solve Count Binary Substrings

Group runs of identical bits; each adjacent pair contributes `min(prev, cur)` substrings.

## Steps

1. Scan runs of `0`s and `1`s.
2. When the bit flips, add `min(previous_run, current_run)`.
3. Include the final pair after the scan.

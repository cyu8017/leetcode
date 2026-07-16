# How We Solve License Key Formatting

Normalize characters, then regroup from the left with the special first segment length.

## Steps

1. Remove dashes and uppercase all alphanumeric characters.
2. Let the first group length be `len % k` (or `k` when divisible).
3. Join remaining groups of size `k` with dashes.

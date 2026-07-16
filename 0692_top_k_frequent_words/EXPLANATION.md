# How We Solve Top K Frequent Words

Count frequencies, then sort by higher count and lexicographic order.

## Steps

1. Build a frequency map of the words.
2. Sort keys by `(-count, word)`.
3. Return the first `k` words.

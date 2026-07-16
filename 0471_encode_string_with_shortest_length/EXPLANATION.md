# How We Solve Encode String with Shortest Length

Dynamic programming builds the shortest encoding for each prefix using repeated-substring compression.

## Steps

1. For each substring, try all unit lengths that divide it evenly and encode as `k[unit]`.
2. DP over prefixes: combine shorter encodings with encoded suffixes.
3. Break ties by lexicographic order when lengths are equal.

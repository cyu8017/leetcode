# How We Solve Sentence Similarity

Words are similar only if equal or listed directly in a pair (not transitive).

## Steps

1. Lengths must match.
2. Build an undirected set of similar pairs.
3. Accept iff every aligned pair is equal or in that set.

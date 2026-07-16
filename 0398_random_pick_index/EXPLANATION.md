# How We Solve Random Pick Index

Index lists per value enable uniform random selection in O(1).

## Steps

1. Build a map from each value to its occurrence indices.
2. pick chooses uniformly among the stored indices for the target.
3. Constructor stores the mapping once for repeated queries.

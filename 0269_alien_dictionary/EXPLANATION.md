# How We Solve Alien Dictionary

Derive letter order from adjacent word comparisons and topologically sort.

## Steps

1. Build a graph of characters appearing in the words.
2. Compare each adjacent word to find the first differing letter.
3. Detect invalid prefix cases that imply no valid order.
4. Topologically sort characters with indegree zero.
5. Return the order or an empty string if a cycle exists.

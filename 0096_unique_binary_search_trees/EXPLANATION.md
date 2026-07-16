# How We Solve Unique Binary Search Trees

Count unique BSTs that store values 1 through n.

## Steps

1. Let dp[i] be the number of unique trees with i nodes.
2. An empty tree counts as 1.
3. For each size, try each possible root.
4. Multiply left-side counts by right-side counts.
5. Sum those products to get dp[n].

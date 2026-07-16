# 2421. Number of Good Paths

- **Difficulty:** Hard
- **LeetCode:** [https://leetcode.com/problems/number-of-good-paths/](https://leetcode.com/problems/number-of-good-paths/)
- **Tags:** array, hash-table, tree, union-find, graph-theory, sorting

## Problem

There is a tree (i.e. a connected, undirected graph with no cycles) consisting of `n` nodes numbered from `0` to `n - 1` and exactly `n - 1` edges.

You are given a **0-indexed** integer array `vals` of length `n` where `vals[i]` denotes the value of the `i^{th}` node. You are also given a 2D integer array `edges` where `edges[i] = [a_{i}, b_{i}]` denotes that there exists an **undirected** edge connecting nodes `a_{i}` and `b_{i}`.

A **good path** is a simple path that satisfies the following conditions:

- The starting node and the ending node have the **same** value.

	- All nodes between the starting node and the ending node have values **less than or equal to** the starting node (i.e. the starting node's value should be the maximum value along the path).

Return *the number of distinct good paths*.

Note that a path and its reverse are counted as the **same** path. For example, `0 -> 1` is considered to be the same as `1 -> 0`. A single node is also considered as a valid path.

**Example 1:**

```
**Input:** vals = [1,3,2,1,3], edges = [[0,1],[0,2],[2,3],[2,4]]
**Output:** 6
**Explanation:** There are 5 good paths consisting of a single node.
There is 1 additional good path: 1 -> 0 -> 2 -> 4.
(The reverse path 4 -> 2 -> 0 -> 1 is treated as the same as 1 -> 0 -> 2 -> 4.)
Note that 0 -> 2 -> 3 is not a good path because vals[2] > vals[0].
```

**Example 2:**

```
**Input:** vals = [1,1,2,2,3], edges = [[0,1],[1,2],[2,3],[2,4]]
**Output:** 7
**Explanation:** There are 5 good paths consisting of a single node.
There are 2 additional good paths: 0 -> 1 and 2 -> 3.
```

**Example 3:**

```
**Input:** vals = [1], edges = []
**Output:** 1
**Explanation:** The tree consists of only one node, so there is one good path.
```

**Constraints:**

- `n == vals.length`

	- `1 <= n <= 3 * 10^{4}`

	- `0 <= vals[i] <= 10^{5}`

	- `edges.length == n - 1`

	- `edges[i].length == 2`

	- `0 <= a_{i}, b_{i} < n`

	- `a_{i} != b_{i}`

	- `edges` represents a valid tree.

### Hints

1. Can you process nodes from smallest to largest value?
2. Try to build the graph from nodes with the smallest value to the largest value.
3. May union find help?

## Approach

<!-- Describe your solution approach here -->

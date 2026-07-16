# 3778. Minimum Distance Excluding One Maximum Weighted Edge

- **Difficulty:** Medium
- **LeetCode:** [https://leetcode.com/problems/minimum-distance-excluding-one-maximum-weighted-edge/](https://leetcode.com/problems/minimum-distance-excluding-one-maximum-weighted-edge/)
- **Premium:** Yes

## Problem

You are given a positive integer `n` and a 2D integer array `edges`, where `edges[i] = [u_{i}, v_{i}, w_{i}]`.

There is a **weighted** **connected** simple undirected graph with `n` nodes labeled from 0 to `n - 1`. Each `[u_{i}, v_{i}, w_{i}]` in `edges` represents an edge between node `u_{i}` and node `v_{i}` with **positive** weight `w_{i}`.

The **cost** of a path is the **sum** of weights of the edges in the path, **excluding** the edge with the **maximum** weight. If there are multiple edges in the path with the maximum weight, **only** the **first** such edge is excluded.

Return an integer representing the **minimum** **cost** of a path going from node 0 to node `n - 1`.



**Example 1:**

**Input:** n = 5, edges = [[0,1,2],[1,2,7],[2,3,7],[3,4,4]]

**Output:** 13

**Explanation:**

There is only one path going from node 0 to node 4: `0 -> 1 -> 2 -> 3 -> 4`.

The edge weights on this path are 2, 7, 7, and 4.

Excluding the first edge with maximum weight, which is `1 -> 2`, the cost of this path is `2 + 7 + 4 = 13`.

**Example 2:**

**Input:** n = 3, edges = [[0,1,1],[1,2,1],[0,2,50000]]

**Output:** 0

**Explanation:**

There are two paths going from node 0 to node 2:

	- `0 -> 1 -> 2`

The edge weights on this path are 1 and 1.

Excluding the first edge with maximum weight, which is `0 -> 1`, the cost of this path is 1.

	- `0 -> 2`

The only edge weight on this path is 1.

Excluding the first edge with maximum weight, which is `0 -> 2`, the cost of this path is 0.

The minimum cost is `min(1, 0) = 0`.



**Constraints:**

	- `2 <= n <= 5 * 10^{4}`

	- `n - 1 <= edges.length <= 10^{9}`

	- `edges[i] = [u_{i}, v_{i}, w_{i}]`

	- `0 <= u_{i} < v_{i} < n`

	- `[u_{i}, v_{i}] != [u_{j}, v_{j}]`

	- `1 <= w_{i} <= 5 * 10^{4}`

	- The graph is connected.

---
_Problem text from the [doocs/leetcode](https://github.com/doocs/leetcode) community mirror (LeetCode Premium)._

### Hints

1. Use Dijkstra
2. The problem is the same as finding the minimum path from 0 to `n - 1` with one edge excluded
3. Use states `(dist, node, excluded)` as your Dijkstra elements

## Approach

<!-- Describe your solution approach here -->

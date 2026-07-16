# 3123. Find Edges in Shortest Paths

- **Difficulty:** Hard
- **LeetCode:** [https://leetcode.com/problems/find-edges-in-shortest-paths/](https://leetcode.com/problems/find-edges-in-shortest-paths/)
- **Tags:** depth-first-search, breadth-first-search, graph-theory, heap-(priority-queue), shortest-path

## Problem

You are given an undirected weighted graph of `n` nodes numbered from 0 to `n - 1`. The graph consists of `m` edges represented by a 2D array `edges`, where `edges[i] = [a_{i}, b_{i}, w_{i}]` indicates that there is an edge between nodes `a_{i}` and `b_{i}` with weight `w_{i}`.

Consider all the shortest paths from node 0 to node `n - 1` in the graph. You need to find a **boolean** array `answer` where `answer[i]` is `true` if the edge `edges[i]` is part of **at least** one shortest path. Otherwise, `answer[i]` is `false`.

Return the array `answer`.

**Note** that the graph may not be connected.

**Example 1:**

**Input:** n = 6, edges = [[0,1,4],[0,2,1],[1,3,2],[1,4,3],[1,5,1],[2,3,1],[3,5,3],[4,5,2]]

**Output:** [true,true,true,false,true,true,true,false]

**Explanation:**

The following are **all** the shortest paths between nodes 0 and 5:

- The path `0 -> 1 -> 5`: The sum of weights is `4 + 1 = 5`.

	- The path `0 -> 2 -> 3 -> 5`: The sum of weights is `1 + 1 + 3 = 5`.

	- The path `0 -> 2 -> 3 -> 1 -> 5`: The sum of weights is `1 + 1 + 2 + 1 = 5`.

**Example 2:**

**Input:** n = 4, edges = [[2,0,1],[0,1,1],[0,3,4],[3,2,2]]

**Output:** [true,false,false,true]

**Explanation:**

There is one shortest path between nodes 0 and 3, which is the path `0 -> 2 -> 3` with the sum of weights `1 + 2 = 3`.

**Constraints:**

- `2 <= n <= 5 * 10^{4}`

	- `m == edges.length`

	- `1 <= m <= min(5 * 10^{4}, n * (n - 1) / 2)`

	- `0 <= a_{i}, b_{i} < n`

	- `a_{i} != b_{i}`

	- `1 <= w_{i} <= 10^{5}`

	- There are no repeated edges.

### Hints

1. Find all the shortest paths starting from nodes 0 and `n - 1` to all other nodes.
2. How to use the above calculated shortest paths to check if an edge is part of at least one shortest path from 0 to `n - 1`?

## Approach

<!-- Describe your solution approach here -->

# 3807. Minimum Cost to Repair Edges to Traverse a Graph

- **Difficulty:** Medium
- **LeetCode:** [https://leetcode.com/problems/minimum-cost-to-repair-edges-to-traverse-a-graph/](https://leetcode.com/problems/minimum-cost-to-repair-edges-to-traverse-a-graph/)
- **Premium:** Yes
- **Tags:** binary-search, breadth-first-search, graph-theory

## Problem

You are given an **undirected graph** with `n` nodes labeled from 0 to `n - 1`. The graph consists of `m` edges represented by a 2D integer array `edges`, where `edges[i] = [u_{i}, v_{i}, w_{i}]` indicates that there is an edge between nodes `u_{i}` and `v_{i}` with a repair cost of `w_{i}`.

You are also given an integer `k`. Initially, **all** edges are damaged.

You may choose a non-negative integer `money` and repair **all** edges whose repair cost is **less than or equal** to `money`. All other edges remain damaged and cannot be used.

You want to travel from node 0 to node `n - 1` using at most `k` edges.

Return an integer denoting the **minimum** amount of money required to make this possible, or return -1 if it is impossible.



**Example 1:**

****

**Input:** n = 3, edges = [[0,1,10],[1,2,10],[0,2,100]], k = 1

**Output:** 100

**Explanation:**

The only valid path using at most `k = 1` edge is `0 -> 2`, which requires repairing the edge with cost 100. Therefore, the minimum required amount of money is 100.

**Example 2:**

****

**Input:** n = 6, edges = [[0,2,5],[2,3,6],[3,4,7],[4,5,5],[0,1,10],[1,5,12],[0,3,9],[1,2,8],[2,4,11]], k = 2

**Output:** 12

**Explanation:**

	- With `money = 12`, all edges with repair cost at most 12 become usable.

	- This allows the path `0 -> 1 -> 5`, which uses exactly 2 edges and reaches node 5.

	- If `money < 12`, there is no available path of length at most `k = 2` from node 0 to node 5.

	- Therefore, the minimum required money is 12.

**Example 3:**

**​​​​​​​**

**Input:** n = 3, edges = [[0,1,1]], k = 1

**Output:** -1

**Explanation:**

It is impossible to reach node 2 from node 0 using any amount of money. Therefore, the answer is -1.



**Constraints:**

	- `2 <= n <= 5 * 10^{4}`

	- `1 <= edges.length == m <= 10^{5}`

	- `edges[i] = [u_{i}, v_{i}, w_{i}]`

	- `0 <= u_{i}, v_{i} < n`

	- `1 <= w_{i} <= 10^{9}`

	- `1 <= k <= n`

	- There are no self-loops or duplicate edges in the graph.

---
_Problem text from the [doocs/leetcode](https://github.com/doocs/leetcode) community mirror (LeetCode Premium)._

### Hints

1. Use binary search.
2. For a fixed value of `money`, check whether there exists a path from node `0` to node `n - 1` that uses at most `k` edges.
3. Use binary search to find the smallest value of `money` that makes this possible.

## Approach

<!-- Describe your solution approach here -->

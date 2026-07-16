# 3650. Minimum Cost Path with Edge Reversals

- **Difficulty:** Medium
- **LeetCode:** [https://leetcode.com/problems/minimum-cost-path-with-edge-reversals/](https://leetcode.com/problems/minimum-cost-path-with-edge-reversals/)
- **Tags:** graph-theory, heap-(priority-queue), shortest-path

## Problem

You are given a directed, weighted graph with `n` nodes labeled from 0 to `n - 1`, and an array `edges` where `edges[i] = [u_{i}, v_{i}, w_{i}]` represents a directed edge from node `u_{i}` to node `v_{i}` with cost `w_{i}`.

Each node `u_{i}` has a switch that can be used **at most once**: when you arrive at `u_{i}` and have not yet used its switch, you may activate it on one of its incoming edges `v_{i} → u_{i}` reverse that edge to `u_{i} → v_{i}` and **immediately** traverse it.

The reversal is only valid for that single move, and using a reversed edge costs `2 * w_{i}`.

Return the **minimum** total cost to travel from node 0 to node `n - 1`. If it is not possible, return -1.

**Example 1:**

**Input:** n = 4, edges = [[0,1,3],[3,1,1],[2,3,4],[0,2,2]]

**Output:** 5

**Explanation: **

**

- Use the path `0 → 1` (cost 3).

	- At node 1 reverse the original edge `3 → 1` into `1 → 3` and traverse it at cost `2 * 1 = 2`.

	- Total cost is `3 + 2 = 5`.

**Example 2:**

**Input:** n = 4, edges = [[0,2,1],[2,1,1],[1,3,1],[2,3,3]]

**Output:** 3

**Explanation:**

- No reversal is needed. Take the path `0 → 2` (cost 1), then `2 → 1` (cost 1), then `1 → 3` (cost 1).

	- Total cost is `1 + 1 + 1 = 3`.

**Constraints:**

- `2 <= n <= 5 * 10^{4}`

	- `1 <= edges.length <= 10^{5}`

	- `edges[i] = [u_{i}, v_{i}, w_{i}]`

	- `0 <= u_{i}, v_{i} <= n - 1`

	- `1 <= w_{i} <= 1000`

### Hints

1. Do we only need to reverse at most one edge for each node? If so, can we add reversed edges for each node and use the one that helps in the shortest path?
2. Add reverse edges: `{u, v, w}` -> `{v, u, 2 * w}`, and use Dijkstra.

## Approach

<!-- Describe your solution approach here -->

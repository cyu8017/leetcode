# 0323. Number of Connected Components in an Undirected Graph

- **Difficulty:** Medium
- **LeetCode:** [https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/)
- **Premium:** Yes
- **Tags:** depth-first-search, breadth-first-search, union-find, graph-theory

## Problem

You have a graph of `n` nodes. You are given an integer `n` and an array `edges` where `edges[i] = [a_{i}, b_{i}]` indicates that there is an edge between `a_{i}` and `b_{i}` in the graph.

Return *the number of connected components in the graph*.



**Example 1:**

**Input:** n = 5, edges = [[0,1],[1,2],[3,4]]
**Output:** 2

**Example 2:**

**Input:** n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]
**Output:** 1



**Constraints:**

	- `1 <= n <= 2000`

	- `1 <= edges.length <= 5000`

	- `edges[i] = [a_{i}, b_{i}]`

	- `a_{i} != b_{i}`

	- There are no repeated edges.

---
_Problem text from the [doocs/leetcode](https://github.com/doocs/leetcode) community mirror (LeetCode Premium)._

## Approach

<!-- Describe your solution approach here -->

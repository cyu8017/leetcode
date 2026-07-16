# 0261. Graph Valid Tree

- **Difficulty:** Medium
- **LeetCode:** [https://leetcode.com/problems/graph-valid-tree/](https://leetcode.com/problems/graph-valid-tree/)
- **Premium:** Yes
- **Tags:** depth-first-search, breadth-first-search, union-find, graph-theory

## Problem

You have a graph of `n` nodes labeled from `0` to `n - 1`. You are given an integer n and a list of `edges` where `edges[i] = [a_{i}, b_{i}]` indicates that there is an undirected edge between nodes `a_{i}` and `b_{i}` in the graph.

Return `true` *if the edges of the given graph make up a valid tree, and* `false` *otherwise*.



**Example 1:**

**Input:** n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
**Output:** true

**Example 2:**

**Input:** n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
**Output:** false



**Constraints:**

	- `1 <= n <= 2000`

	- `0 <= edges.length <= 5000`

	- `edges[i].length == 2`

	- `0 <= a_{i}, b_{i} < n`

	- `a_{i} != b_{i}`

	- There are no self-loops or repeated edges.

---
_Problem text from the [doocs/leetcode](https://github.com/doocs/leetcode) community mirror (LeetCode Premium)._

### Hints

1. Given `n = 5` and `edges = [[0, 1], [1, 2], [3, 4]]`, what should your return? Is this case a valid tree?
2. According to the [definition of tree on Wikipedia](https://en.wikipedia.org/wiki/Tree_(graph_theory)): “a tree is an undirected graph in which any two vertices are connected by *exactly* one path. In other words, any connected graph without simple cycles is a tree.”

## Approach

<!-- Describe your solution approach here -->

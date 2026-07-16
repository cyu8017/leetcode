# 1245. Tree Diameter

- **Difficulty:** Medium
- **LeetCode:** [https://leetcode.com/problems/tree-diameter/](https://leetcode.com/problems/tree-diameter/)
- **Premium:** Yes
- **Tags:** tree, depth-first-search, breadth-first-search, graph-theory, topological-sort

## Problem

The **diameter** of a tree is **the number of edges** in the longest path in that tree.

There is an undirected tree of `n` nodes labeled from `0` to `n - 1`. You are given a 2D array `edges` where `edges.length == n - 1` and `edges[i] = [a_{i}, b_{i}]` indicates that there is an undirected edge between nodes `a_{i}` and `b_{i}` in the tree.

Return *the **diameter** of the tree*.



**Example 1:**

**Input:** edges = [[0,1],[0,2]]
**Output:** 2
**Explanation:** The longest path of the tree is the path 1 - 0 - 2.

**Example 2:**

**Input:** edges = [[0,1],[1,2],[2,3],[1,4],[4,5]]
**Output:** 4
**Explanation:** The longest path of the tree is the path 3 - 2 - 1 - 4 - 5.



**Constraints:**

	- `n == edges.length + 1`

	- `1 <= n <= 10^{4}`

	- `0 <= a_{i}, b_{i} < n`

	- `a_{i} != b_{i}`

---
_Problem text from the [doocs/leetcode](https://github.com/doocs/leetcode) community mirror (LeetCode Premium)._

### Hints

1. Start at any node A and traverse the tree to find the furthest node from it, let's call it B.
2. Having found the furthest node B, traverse the tree from B to find the furthest node from it, lets call it C.
3. The distance between B and C is the tree diameter.

## Approach

<!-- Describe your solution approach here -->

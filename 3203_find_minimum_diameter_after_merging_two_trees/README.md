# 3203. Find Minimum Diameter After Merging Two Trees

- **Difficulty:** Hard
- **LeetCode:** [https://leetcode.com/problems/find-minimum-diameter-after-merging-two-trees/](https://leetcode.com/problems/find-minimum-diameter-after-merging-two-trees/)
- **Tags:** tree, depth-first-search, breadth-first-search, graph-theory

## Problem

There exist two **undirected **trees with `n` and `m` nodes, numbered from `0` to `n - 1` and from `0` to `m - 1`, respectively. You are given two 2D integer arrays `edges1` and `edges2` of lengths `n - 1` and `m - 1`, respectively, where `edges1[i] = [a_{i}, b_{i}]` indicates that there is an edge between nodes `a_{i}` and `b_{i}` in the first tree and `edges2[i] = [u_{i}, v_{i}]` indicates that there is an edge between nodes `u_{i}` and `v_{i}` in the second tree.

You must connect one node from the first tree with another node from the second tree with an edge.

Return the **minimum **possible **diameter **of the resulting tree.

The **diameter** of a tree is the length of the *longest* path between any two nodes in the tree.

**Example 1:**

**Input:** edges1 = [[0,1],[0,2],[0,3]], edges2 = [[0,1]]

**Output:** 3

**Explanation:**

We can obtain a tree of diameter 3 by connecting node 0 from the first tree with any node from the second tree.

**Example 2:**

**Input:** edges1 = [[0,1],[0,2],[0,3],[2,4],[2,5],[3,6],[2,7]], edges2 = [[0,1],[0,2],[0,3],[2,4],[2,5],[3,6],[2,7]]

**Output:** 5

**Explanation:**

We can obtain a tree of diameter 5 by connecting node 0 from the first tree with node 0 from the second tree.

**Constraints:**

- `1 <= n, m <= 10^{5}`

	- `edges1.length == n - 1`

	- `edges2.length == m - 1`

	- `edges1[i].length == edges2[i].length == 2`

	- `edges1[i] = [a_{i}, b_{i}]`

	- `0 <= a_{i}, b_{i} < n`

	- `edges2[i] = [u_{i}, v_{i}]`

	- `0 <= u_{i}, v_{i} < m`

	- The input is generated such that `edges1` and `edges2` represent valid trees.

### Hints

1. Suppose that we connected node `a` in tree1 with node `b` in tree2. The diameter length of the resulting tree will be the largest of the following 3 values:

- The diameter of tree 1.

- The diameter of tree 2.

- The length of the longest path that starts at node `a` and that is completely within Tree 1 + The length of the longest path that starts at node `b` and that is completely within Tree 2 + 1.


The added one in the third value is due to the additional edge that we have added between trees 1 and 2.
2. Values 1 and 2 are constant regardless of our choice of `a` and `b`. Therefore, we need to pick `a` and `b` in such a way that minimizes value 3.
3. If we pick `a` and `b` optimally, they will be in the diameters of Tree 1 and Tree 2, respectively. Exactly which nodes of the diameter should we pick?
4. `a` is the center of the diameter of tree 1, and `b` is the center of the diameter of tree 2.

## Approach

<!-- Describe your solution approach here -->

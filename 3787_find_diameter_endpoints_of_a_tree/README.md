# 3787. Find Diameter Endpoints of a Tree

- **Difficulty:** Medium
- **LeetCode:** [https://leetcode.com/problems/find-diameter-endpoints-of-a-tree/](https://leetcode.com/problems/find-diameter-endpoints-of-a-tree/)
- **Premium:** Yes
- **Tags:** tree, breadth-first-search, graph-theory

## Problem

You are given an **undirected tree** with `n` nodes, numbered from 0 to `n - 1`. It is represented by a 2D integer array `edges`​​​​​​​ of length `n - 1`, where `edges[i] = [a_{i}, b_{i}]` indicates that there is an edge between nodes `a_{i}` and `b_{i}` in the tree.

A node is called **special** if it is an **endpoint** of any** diameter path** of the tree.

Return a binary string `s` of length `n`, where `s[i] = '1'` if node `i` is special, and `s[i] = '0'` otherwise.

A **diameter path** of a tree is the **longest** simple path between any two nodes. A tree may have multiple diameter paths.

An **endpoint** of a path is the **first** or **last** node on that path.



**Example 1:**

****

**Input:** n = 3, edges = [[0,1],[1,2]]

**Output:** "101"

**Explanation:**

	- The diameter of this tree consists of 2 edges.

	- The only diameter path is the path from node 0 to node 2

	- The endpoints of this path are nodes 0 and 2, so they are special.

**Example 2:**

****

**Input:** n = 7, edges = [[0,1],[1,2],[2,3],[3,4],[3,5],[1,6]]

**Output:** "1000111"

**Explanation:**

The diameter of this tree consists of 4 edges. There are 4 diameter paths:

	- The path from node 0 to node 4

	- The path from node 0 to node 5

	- The path from node 6 to node 4

	- The path from node 6 to node 5

The special nodes are nodes `0, 4, 5, 6`, as they are endpoints in at least one diameter path.

**Example 3:**

**​​​​​​​**

**Input:** n = 2, edges = [[0,1]]

**Output:** "11"

**Explanation:**

	- The diameter of this tree consists of 1 edge.

	- The only diameter path is the path from node 0 to node 1

	- The endpoints of this path are nodes 0 and 1, so they are special.



**Constraints:**

	- `2 <= n <= 10^{5}`

	- `edges.length == n - 1`

	- `edges[i] = [a_{i}, b_{i}]`

	- `0 <= a_{i}, b_{i} < n`

	- The input is generated such that `edges` represents a valid tree.

---
_Problem text from the [doocs/leetcode](https://github.com/doocs/leetcode) community mirror (LeetCode Premium)._

### Hints

1. Start a breadth first search (BFS) from any node `start`; let the farthest node found be `A`.
2. Run BFS from `A`; a farthest node `B` is at the other end, and the path `A`-`B` is a diameter.
3. If several nodes tie as farthest from `start`, collect them into `cand_start`, each is a possible diameter endpoint.
4. Running BFS from any node in `cand_start` yields the opposite-end set `cand_other`, the other diameter endpoints.

## Approach

<!-- Describe your solution approach here -->

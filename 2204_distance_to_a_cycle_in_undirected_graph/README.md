# 2204. Distance to a Cycle in Undirected Graph

- **Difficulty:** Hard
- **LeetCode:** [https://leetcode.com/problems/distance-to-a-cycle-in-undirected-graph/](https://leetcode.com/problems/distance-to-a-cycle-in-undirected-graph/)
- **Premium:** Yes
- **Tags:** depth-first-search, breadth-first-search, graph-theory, topological-sort

## Problem

You are given a positive integer `n` representing the number of nodes in a **connected undirected graph** containing **exactly one** cycle. The nodes are numbered from `0` to `n - 1` (**inclusive**).

You are also given a 2D integer array `edges`, where `edges[i] = [node1_{i}, node2_{i}]` denotes that there is a **bidirectional** edge connecting `node1_{i}` and `node2_{i}` in the graph.

The distance between two nodes `a` and `b` is defined to be the **minimum** number of edges that are needed to go from `a` to `b`.

Return *an integer array `answer`** of size *`n`*, where *`answer[i]`* is the **minimum** distance between the *`i^{th}`* node and **any** node in the cycle.*



**Example 1:**

**Input:** n = 7, edges = [[1,2],[2,4],[4,3],[3,1],[0,1],[5,2],[6,5]]
**Output:** [1,0,0,0,0,1,2]
**Explanation:**
The nodes 1, 2, 3, and 4 form the cycle.
The distance from 0 to 1 is 1.
The distance from 1 to 1 is 0.
The distance from 2 to 2 is 0.
The distance from 3 to 3 is 0.
The distance from 4 to 4 is 0.
The distance from 5 to 2 is 1.
The distance from 6 to 2 is 2.

**Example 2:**

**Input:** n = 9, edges = [[0,1],[1,2],[0,2],[2,6],[6,7],[6,8],[0,3],[3,4],[3,5]]
**Output:** [0,0,0,1,2,2,1,2,2]
**Explanation:**
The nodes 0, 1, and 2 form the cycle.
The distance from 0 to 0 is 0.
The distance from 1 to 1 is 0.
The distance from 2 to 2 is 0.
The distance from 3 to 1 is 1.
The distance from 4 to 1 is 2.
The distance from 5 to 1 is 2.
The distance from 6 to 2 is 1.
The distance from 7 to 2 is 2.
The distance from 8 to 2 is 2.



**Constraints:**

	- `3 <= n <= 10^{5}`

	- `edges.length == n`

	- `edges[i].length == 2`

	- `0 <= node1_{i}, node2_{i} <= n - 1`

	- `node1_{i} != node2_{i}`

	- The graph is connected.

	- The graph has exactly one cycle.

	- There is at most one edge between any pair of vertices.

---
_Problem text from the [doocs/leetcode](https://github.com/doocs/leetcode) community mirror (LeetCode Premium)._

### Hints

1. This problem can be broken down into two parts: finding the cycle, and finding the distance between each node and the cycle.
2. How can we find the cycle? We can use DFS and keep track of the nodes we’ve seen, and the order that we see them in. Once we see a node we’ve already visited, we know that the cycle contains the node that was seen twice and all the nodes that we visited in between.
3. Now that we know which nodes are part of the cycle, how can we find the distances? We can run a multi-source BFS starting from the nodes in the cycle and expanding outward.

## Approach

<!-- Describe your solution approach here -->

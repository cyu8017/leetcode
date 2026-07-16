# 3970. Shortest Path With At Most K Consecutive Identical Characters

- **Difficulty:** Medium
- **LeetCode:** [https://leetcode.com/problems/shortest-path-with-at-most-k-consecutive-identical-characters/](https://leetcode.com/problems/shortest-path-with-at-most-k-consecutive-identical-characters/)
- **Tags:** string, graph-theory, heap-(priority-queue), shortest-path

## Problem

You are given an integer `n` representing the number of nodes in a **directed weighted** graph, numbered from 0 to `n - 1`. This is represented by a 2D integer array `edges`, where `edges[i] = [u_{i}, v_{i}, w_{i}]` represents a directed edge from node `u_{i}` to node `v_{i}` with weight `w_{i}`.

You are also given a string `labels` of length `n`, where `labels[i]` is the character assigned to node `i`, and an integer `k`.

Return the **minimum** **total** edge weight of a path from node 0 to node `n - 1` such that the concatenation of the labels of the nodes along the path contains **at most** `k` **consecutive** **identical** characters. If no valid path exists, return -1.

**Example 1:**

**Input:** n = 3, edges = [[0,1,1],[1,2,1],[0,2,3]], labels = "aab", k = 1

**Output:** 3

**Explanation:**

The optimal valid path from node 0 to node 2 is as follows:

- Use `edges[2] = [0, 2, 3]` to reach node 2 with a weight `w_{i} = 3`.

The corresponding concatenation of labels is `"ab"`, which satisfies at most `k = 1` consecutive identical characters. Thus, the answer is 3.

**Example 2:**

**Input:** n = 3, edges = [[0,1,1],[1,2,1],[0,2,3]], labels = "aab", k = 2

**Output:** 2

**Explanation:**

The optimal valid path from node 0 to node 2 is as follows:

- Use `edges[0] = [0, 1, 1]` to reach node 1 with weight `w_{i} = 1`.

	- Use `edges[1] = [1, 2, 1]` to reach node 2 with weight `w_{i} = 1`.

The corresponding concatenation of labels is `"aab"`, which satisfies at most `k = 2` consecutive identical characters. Thus, the answer is 2.

**Example 3:**

**Input:** n = 3, edges = [[0,1,1],[1,2,1]], labels = "aaa", k = 2

**Output:** -1

**Explanation:**

There is no valid path from node 0 to node 2 that satisfies at most `k = 2` consecutive identical characters. Thus, the answer is -1.

**Constraints:**

- `1 <= n == labels.length <= 5 * 10^{4}`

	- `0 <= edges.length <= 5 * 10^{4}`

	- `edges[i] == [u_{i}, v_{i}, w_{i}]`

	- `0 <= u_{i}, v_{i} <= n - 1`

	- `u_{i} != v_{i}`

	- `1 <= w_{i} <= 10^{4}`

	- `labels` consists of lowercase English letters

	- `1 <= k <= 50`

### Hints

1. The validity of a path depends not only on the current node, but also on how many consecutive times the current node’s label has appeared at the end of the path.
2. Use Dijkstra on states `(node, count)`, where `count` is the current consecutive run length of `labels[node]`.
3. When moving from node `u` to node `v`, the next count becomes `count + 1` if `labels[u] == labels[v]`, otherwise it becomes 1. Ignore transitions where the next count exceeds `k`.
4. The answer is the minimum distance among all states ending at node `n - 1`.

## Approach

<!-- Describe your solution approach here -->

# 1192. Critical Connections in a Network

- **Difficulty:** Hard
- **LeetCode:** [https://leetcode.com/problems/critical-connections-in-a-network/](https://leetcode.com/problems/critical-connections-in-a-network/)
- **Tags:** depth-first-search, graph-theory, biconnected-component

## Problem

There are `n` servers numbered from `0` to `n - 1` connected by undirected server-to-server `connections` forming a network where `connections[i] = [a_{i}, b_{i}]` represents a connection between servers `a_{i}` and `b_{i}`. Any server can reach other servers directly or indirectly through the network.

A *critical connection* is a connection that, if removed, will make some servers unable to reach some other server.

Return all critical connections in the network in any order.

**Example 1:**

```
**Input:** n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
**Output:** [[1,3]]
**Explanation:** [[3,1]] is also accepted.
```

**Example 2:**

```
**Input:** n = 2, connections = [[0,1]]
**Output:** [[0,1]]
```

**Constraints:**

- `2 <= n <= 10^{5}`

	- `n - 1 <= connections.length <= 10^{5}`

	- `0 <= a_{i}, b_{i} <= n - 1`

	- `a_{i} != b_{i}`

	- There are no repeated connections.

### Hints

1. Use Tarjan's algorithm.

## Approach

<!-- Describe your solution approach here -->

# 0743. Network Delay Time

- **Difficulty:** Medium
- **LeetCode:** [https://leetcode.com/problems/network-delay-time/](https://leetcode.com/problems/network-delay-time/)
- **Tags:** depth-first-search, breadth-first-search, graph-theory, heap-(priority-queue), shortest-path

## Problem

You are given a network of `n` nodes, labeled from `1` to `n`. You are also given `times`, a list of travel times as directed edges `times[i] = (u_{i}, v_{i}, w_{i})`, where `u_{i}` is the source node, `v_{i}` is the target node, and `w_{i}` is the time it takes for a signal to travel from source to target.

We will send a signal from a given node `k`. Return *the **minimum** time it takes for all the* `n` *nodes to receive the signal*. If it is impossible for all the `n` nodes to receive the signal, return `-1`.

**Example 1:**

```
**Input:** times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
**Output:** 2
```

**Example 2:**

```
**Input:** times = [[1,2,1]], n = 2, k = 1
**Output:** 1
```

**Example 3:**

```
**Input:** times = [[1,2,1]], n = 2, k = 2
**Output:** -1
```

**Constraints:**

- `1 <= k <= n <= 100`

	- `1 <= times.length <= 6000`

	- `times[i].length == 3`

	- `1 <= u_{i}, v_{i} <= n`

	- `u_{i} != v_{i}`

	- `0 <= w_{i} <= 100`

	- All the pairs `(u_{i}, v_{i})` are **unique**. (i.e., no multiple edges.)

### Hints

1. We visit each node at some time, and if that time is better than the fastest time we've reached this node, we travel along outgoing edges in sorted order.  Alternatively, we could use Dijkstra's algorithm.

## Approach

<!-- Describe your solution approach here -->

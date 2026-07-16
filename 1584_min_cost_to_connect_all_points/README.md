# 1584. Min Cost to Connect All Points

- **Difficulty:** Medium
- **LeetCode:** [https://leetcode.com/problems/min-cost-to-connect-all-points/](https://leetcode.com/problems/min-cost-to-connect-all-points/)
- **Tags:** array, union-find, graph-theory, minimum-spanning-tree

## Problem

You are given an array `points` representing integer coordinates of some points on a 2D-plane, where `points[i] = [x_{i}, y_{i}]`.

The cost of connecting two points `[x_{i}, y_{i}]` and `[x_{j}, y_{j}]` is the **manhattan distance** between them: `|x_{i} - x_{j}| + |y_{i} - y_{j}|`, where `|val|` denotes the absolute value of `val`.

Return *the minimum cost to make all points connected.* All points are connected if there is **exactly one** simple path between any two points.

**Example 1:**

```
**Input:** points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
**Output:** 20
**Explanation:**

We can connect the points as shown above to get the minimum cost of 20.
Notice that there is a unique path between every pair of points.
```

**Example 2:**

```
**Input:** points = [[3,12],[-2,5],[-4,1]]
**Output:** 18
```

**Constraints:**

- `1 <= points.length <= 1000`

	- `-10^{6} <= x_{i}, y_{i} <= 10^{6}`

	- All pairs `(x_{i}, y_{i})` are distinct.

### Hints

1. Connect each pair of points with a weighted edge, the weight being the manhattan distance between those points.
2. The problem is now the cost of minimum spanning tree in graph with above edges.

## Approach

<!-- Describe your solution approach here -->

# 3102. Minimize Manhattan Distances

- **Difficulty:** Hard
- **LeetCode:** [https://leetcode.com/problems/minimize-manhattan-distances/](https://leetcode.com/problems/minimize-manhattan-distances/)
- **Tags:** array, math, geometry, sorting, ordered-set

## Problem

You are given an array `points` representing integer coordinates of some points on a 2D plane, where `points[i] = [x_{i}, y_{i}]`.

The distance between two points is defined as their Manhattan distance.

Return *the **minimum** possible value for **maximum** distance between any two points by removing exactly one point*.

**Example 1:**

**Input:** points = [[3,10],[5,15],[10,2],[4,4]]

**Output:** 12

**Explanation:**

The maximum distance after removing each point is the following:

- After removing the 0^{th} point the maximum distance is between points (5, 15) and (10, 2), which is `|5 - 10| + |15 - 2| = 18`.

	- After removing the 1^{st} point the maximum distance is between points (3, 10) and (10, 2), which is `|3 - 10| + |10 - 2| = 15`.

	- After removing the 2^{nd} point the maximum distance is between points (5, 15) and (4, 4), which is `|5 - 4| + |15 - 4| = 12`.

	- After removing the 3^{rd} point the maximum distance is between points (5, 15) and (10, 2), which is `|5 - 10| + |15 - 2| = 18`.

12 is the minimum possible maximum distance between any two points after removing exactly one point.

**Example 2:**

**Input:** points = [[1,1],[1,1],[1,1]]

**Output:** 0

**Explanation:**

Removing any of the points results in the maximum distance between any two points of 0.

**Constraints:**

- `3 <= points.length <= 10^{5}`

	- `points[i].length == 2`

	- `1 <= points[i][0], points[i][1] <= 10^{8}`

### Hints

1. Notice that the Manhattan distance between two points `[x_{i}, y_{i}]` and `[x_{j}, y_{j}] is  max({x_{i} - x_{j} + y_{i} - y_{j}, x_{i} - x_{j} - y_{i} + y_{j}, - x_{i} + x_{j} + y_{i} - y_{j}, - x_{i} + x_{j} - y_{i} + y_{j}})`.
2. If you replace points as `[x_{i} - y_{i}, x_{i} + y_{i}]` then the Manhattan distance is `max(max(x_{i}) - min(x_{i}), max(y_{i}) - min(y_{i}))` over all `i`.
3. After those observations, the problem just becomes a simulation. Create multiset of points `[x_{i} - y_{i}, x_{i} + y_{i}]`, you can iterate on a point you might remove and get the maximum Manhattan distance over all other points.

## Approach

<!-- Describe your solution approach here -->

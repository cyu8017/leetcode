# 2477. Minimum Fuel Cost to Report to the Capital

- **Difficulty:** Medium
- **LeetCode:** [https://leetcode.com/problems/minimum-fuel-cost-to-report-to-the-capital/](https://leetcode.com/problems/minimum-fuel-cost-to-report-to-the-capital/)
- **Tags:** tree, depth-first-search, breadth-first-search, graph-theory

## Problem

There is a tree (i.e., a connected, undirected graph with no cycles) structure country network consisting of `n` cities numbered from `0` to `n - 1` and exactly `n - 1` roads. The capital city is city `0`. You are given a 2D integer array `roads` where `roads[i] = [a_{i}, b_{i}]` denotes that there exists a **bidirectional road** connecting cities `a_{i}` and `b_{i}`.

There is a meeting for the representatives of each city. The meeting is in the capital city.

There is a car in each city. You are given an integer `seats` that indicates the number of seats in each car.

A representative can use the car in their city to travel or change the car and ride with another representative. The cost of traveling between two cities is one liter of fuel.

Return *the minimum number of liters of fuel to reach the capital city*.

**Example 1:**

```
**Input:** roads = [[0,1],[0,2],[0,3]], seats = 5
**Output:** 3
**Explanation:**
- Representative_{1} goes directly to the capital with 1 liter of fuel.
- Representative_{2} goes directly to the capital with 1 liter of fuel.
- Representative_{3} goes directly to the capital with 1 liter of fuel.
It costs 3 liters of fuel at minimum.
It can be proven that 3 is the minimum number of liters of fuel needed.
```

**Example 2:**

```
**Input:** roads = [[3,1],[3,2],[1,0],[0,4],[0,5],[4,6]], seats = 2
**Output:** 7
**Explanation:**
- Representative_{2} goes directly to city 3 with 1 liter of fuel.
- Representative_{2} and representative_{3} go together to city 1 with 1 liter of fuel.
- Representative_{2} and representative_{3} go together to the capital with 1 liter of fuel.
- Representative_{1} goes directly to the capital with 1 liter of fuel.
- Representative_{5} goes directly to the capital with 1 liter of fuel.
- Representative_{6} goes directly to city 4 with 1 liter of fuel.
- Representative_{4} and representative_{6} go together to the capital with 1 liter of fuel.
It costs 7 liters of fuel at minimum.
It can be proven that 7 is the minimum number of liters of fuel needed.
```

**Example 3:**

```
**Input:** roads = [], seats = 1
**Output:** 0
**Explanation:** No representatives need to travel to the capital city.
```

**Constraints:**

- `1 <= n <= 10^{5}`

	- `roads.length == n - 1`

	- `roads[i].length == 2`

	- `0 <= a_{i}, b_{i} < n`

	- `a_{i} != b_{i}`

	- `roads` represents a valid tree.

	- `1 <= seats <= 10^{5}`

### Hints

1. Can you record the size of each subtree?
2. If n people meet on the same node, what is the minimum number of cars needed?

## Approach

<!-- Describe your solution approach here -->

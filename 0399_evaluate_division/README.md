# 0399. Evaluate Division

- **Difficulty:** Medium
- **LeetCode:** [https://leetcode.com/problems/evaluate-division/](https://leetcode.com/problems/evaluate-division/)
- **Tags:** array, string, depth-first-search, breadth-first-search, union-find, graph-theory, shortest-path

## Problem

You are given an array of variable pairs `equations` and an array of real numbers `values`, where `equations[i] = [A_{i}, B_{i}]` and `values[i]` represent the equation `A_{i} / B_{i} = values[i]`. Each `A_{i}` or `B_{i}` is a string that represents a single variable.

You are also given some `queries`, where `queries[j] = [C_{j}, D_{j}]` represents the `j^{th}` query where you must find the answer for `C_{j} / D_{j} = ?`.

Return *the answers to all queries*. If a single answer cannot be determined, return `-1.0`.

**Note:** The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.

**Note: **The variables that do not occur in the list of equations are undefined, so the answer cannot be determined for them.

**Example 1:**

```
**Input:** equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
**Output:** [6.00000,0.50000,-1.00000,1.00000,-1.00000]
**Explanation:**
Given: *a / b = 2.0*, *b / c = 3.0*
queries are: *a / c = ?*, *b / a = ?*, *a / e = ?*, *a / a = ?*, *x / x = ? *
return: [6.0, 0.5, -1.0, 1.0, -1.0 ]
note: x is undefined => -1.0
```

**Example 2:**

```
**Input:** equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
**Output:** [3.75000,0.40000,5.00000,0.20000]
```

**Example 3:**

```
**Input:** equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
**Output:** [0.50000,2.00000,-1.00000,-1.00000]
```

**Constraints:**

- `1 <= equations.length <= 20`

	- `equations[i].length == 2`

	- `1 <= A_{i}.length, B_{i}.length <= 5`

	- `values.length == equations.length`

	- `0.0 < values[i] <= 20.0`

	- `1 <= queries.length <= 20`

	- `queries[i].length == 2`

	- `1 <= C_{j}.length, D_{j}.length <= 5`

	- `A_{i}, B_{i}, C_{j}, D_{j}` consist of lower case English letters and digits.

### Hints

1. Do you recognize this as a graph problem?

## Approach

<!-- Describe your solution approach here -->

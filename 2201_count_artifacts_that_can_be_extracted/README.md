# 2201. Count Artifacts That Can Be Extracted

- **Difficulty:** Medium
- **LeetCode:** [https://leetcode.com/problems/count-artifacts-that-can-be-extracted/](https://leetcode.com/problems/count-artifacts-that-can-be-extracted/)
- **Tags:** array, hash-table, simulation

## Problem

There is an `n x n` **0-indexed** grid with some artifacts buried in it. You are given the integer `n` and a **0-indexed **2D integer array `artifacts` describing the positions of the rectangular artifacts where `artifacts[i] = [r1_{i}, c1_{i}, r2_{i}, c2_{i}]` denotes that the `i^{th}` artifact is buried in the subgrid where:

- `(r1_{i}, c1_{i})` is the coordinate of the **top-left** cell of the `i^{th}` artifact and

	- `(r2_{i}, c2_{i})` is the coordinate of the **bottom-right** cell of the `i^{th}` artifact.

You will excavate some cells of the grid and remove all the mud from them. If the cell has a part of an artifact buried underneath, it will be uncovered. If all the parts of an artifact are uncovered, you can extract it.

Given a **0-indexed** 2D integer array `dig` where `dig[i] = [r_{i}, c_{i}]` indicates that you will excavate the cell `(r_{i}, c_{i})`, return *the number of artifacts that you can extract*.

The test cases are generated such that:

- No two artifacts overlap.

	- Each artifact only covers at most `4` cells.

	- The entries of `dig` are unique.

**Example 1:**

```
**Input:** n = 2, artifacts = [[0,0,0,0],[0,1,1,1]], dig = [[0,0],[0,1]]
**Output:** 1
**Explanation:**
The different colors represent different artifacts. Excavated cells are labeled with a 'D' in the grid.
There is 1 artifact that can be extracted, namely the red artifact.
The blue artifact has one part in cell (1,1) which remains uncovered, so we cannot extract it.
Thus, we return 1.
```

**Example 2:**

```
**Input:** n = 2, artifacts = [[0,0,0,0],[0,1,1,1]], dig = [[0,0],[0,1],[1,1]]
**Output:** 2
**Explanation:** Both the red and blue artifacts have all parts uncovered (labeled with a 'D') and can be extracted, so we return 2.
```

**Constraints:**

- `1 <= n <= 1000`

	- `1 <= artifacts.length, dig.length <= min(n^{2}, 10^{5})`

	- `artifacts[i].length == 4`

	- `dig[i].length == 2`

	- `0 <= r1_{i}, c1_{i}, r2_{i}, c2_{i}, r_{i}, c_{i} <= n - 1`

	- `r1_{i} <= r2_{i}`

	- `c1_{i} <= c2_{i}`

	- No two artifacts will overlap.

	- The number of cells covered by an artifact is **at most** `4`.

	- The entries of `dig` are unique.

### Hints

1. Check if each coordinate of each artifact has been excavated. How can we do this quickly without iterating over the dig array every time?
2. Consider marking all excavated cells in a 2D boolean array.

## Approach

<!-- Describe your solution approach here -->

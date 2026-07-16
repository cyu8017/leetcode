# 3288. Length of the Longest Increasing Path

- **Difficulty:** Hard
- **LeetCode:** [https://leetcode.com/problems/length-of-the-longest-increasing-path/](https://leetcode.com/problems/length-of-the-longest-increasing-path/)
- **Tags:** array, binary-search, sorting

## Problem

You are given a 2D array of integers `coordinates` of length `n` and an integer `k`, where `0 <= k < n`.

`coordinates[i] = [x_{i}, y_{i}]` indicates the point `(x_{i}, y_{i})` in a 2D plane.

An **increasing path** of length `m` is defined as a list of points `(x_{1}, y_{1})`, `(x_{2}, y_{2})`, `(x_{3}, y_{3})`, ..., `(x_{m}, y_{m})` such that:

- `x_{i} < x_{i + 1}` and `y_{i} < y_{i + 1}` for all `i` where `1 <= i < m`.

	- `(x_{i}, y_{i})` is in the given coordinates for all `i` where `1 <= i <= m`.

Return the **maximum** length of an **increasing path** that contains `coordinates[k]`.

**Example 1:**

**Input:** coordinates = [[3,1],[2,2],[4,1],[0,0],[5,3]], k = 1

**Output:** 3

**Explanation:**

`(0, 0)`, `(2, 2)`, `(5, 3)` is the longest increasing path that contains `(2, 2)`.

**Example 2:**

**Input:** coordinates = [[2,1],[7,0],[5,6]], k = 2

**Output:** 2

**Explanation:**

`(2, 1)`, `(5, 6)` is the longest increasing path that contains `(5, 6)`.

**Constraints:**

- `1 <= n == coordinates.length <= 10^{5}`

	- `coordinates[i].length == 2`

	- `0 <= coordinates[i][0], coordinates[i][1] <= 10^{9}`

	- All elements in `coordinates` are **distinct**.

	- `0 <= k <= n - 1`

### Hints

1. Only keep coordinates with both `x` and `y` being strictly less than `coordinates[k]`.
2. Sort them by `x`’s, in the case of equal, the `y` values should be decreasing.
3. Calculate LIS only using `y` values.
4. Do the same for coordinates with both `x` and `y` being strictly larger than `coordinates[k]`.

## Approach

<!-- Describe your solution approach here -->

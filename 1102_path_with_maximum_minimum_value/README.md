# 1102. Path With Maximum Minimum Value

- **Difficulty:** Medium
- **LeetCode:** [https://leetcode.com/problems/path-with-maximum-minimum-value/](https://leetcode.com/problems/path-with-maximum-minimum-value/)
- **Premium:** Yes
- **Tags:** array, binary-search, depth-first-search, breadth-first-search, union-find, heap-(priority-queue), matrix

## Problem

Given an `m x n` integer matrix `grid`, return *the maximum **score** of a path starting at *`(0, 0)`* and ending at *`(m - 1, n - 1)` moving in the 4 cardinal directions.

The **score** of a path is the minimum value in that path.

	- For example, the score of the path `8 → 4 → 5 → 9` is `4`.



**Example 1:**

**Input:** grid = [[5,4,5],[1,2,6],[7,4,6]]
**Output:** 4
**Explanation:** The path with the maximum score is highlighted in yellow.

**Example 2:**

**Input:** grid = [[2,2,1,2,2,2],[1,2,2,2,1,2]]
**Output:** 2

**Example 3:**

**Input:** grid = [[3,4,6,3,4],[0,2,1,1,7],[8,8,3,2,7],[3,2,4,9,8],[4,1,2,0,0],[4,6,5,4,3]]
**Output:** 3



**Constraints:**

	- `m == grid.length`

	- `n == grid[i].length`

	- `1 <= m, n <= 100`

	- `0 <= grid[i][j] <= 10^{9}`

---
_Problem text from the [doocs/leetcode](https://github.com/doocs/leetcode) community mirror (LeetCode Premium)._

### Hints

1. What if we sort each cell of the matrix by the value?
2. Don't include small values in your path if you can only include large values.
3. Let's keep adding a possible cell to use in the path incrementally with decreasing values.
4. If the start and end cells are connected then we don't need to add more cells.
5. Use union-find data structure to check connectivity and return as answer the value of the given cell that makes start and end cells connected.

## Approach

<!-- Describe your solution approach here -->

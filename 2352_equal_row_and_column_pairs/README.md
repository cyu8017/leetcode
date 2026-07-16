# 2352. Equal Row and Column Pairs

- **Difficulty:** Medium
- **LeetCode:** [https://leetcode.com/problems/equal-row-and-column-pairs/](https://leetcode.com/problems/equal-row-and-column-pairs/)
- **Tags:** array, hash-table, matrix, simulation

## Problem

Given a **0-indexed** `n x n` integer matrix `grid`, *return the number of pairs *`(r_{i}, c_{j})`* such that row *`r_{i}`* and column *`c_{j}`* are equal*.

A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).

**Example 1:**

```
**Input:** grid = [[3,2,1],[1,7,6],[2,7,7]]
**Output:** 1
**Explanation:** There is 1 equal row and column pair:
- (Row 2, Column 1): [2,7,7]
```

**Example 2:**

```
**Input:** grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
**Output:** 3
**Explanation:** There are 3 equal row and column pairs:
- (Row 0, Column 0): [3,1,2,2]
- (Row 2, Column 2): [2,4,2,2]
- (Row 3, Column 2): [2,4,2,2]
```

**Constraints:**

- `n == grid.length == grid[i].length`

	- `1 <= n <= 200`

	- `1 <= grid[i][j] <= 10^{5}`

### Hints

1. We can use nested loops to compare every row against every column.
2. Another loop is necessary to compare the row and column element by element.
3. It is also possible to hash the arrays and compare the hashed values instead.

## Approach

<!-- Describe your solution approach here -->

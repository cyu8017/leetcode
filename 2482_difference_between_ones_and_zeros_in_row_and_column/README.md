# 2482. Difference Between Ones and Zeros in Row and Column

- **Difficulty:** Medium
- **LeetCode:** [https://leetcode.com/problems/difference-between-ones-and-zeros-in-row-and-column/](https://leetcode.com/problems/difference-between-ones-and-zeros-in-row-and-column/)
- **Tags:** array, matrix, simulation

## Problem

You are given a **0-indexed** `m x n` binary matrix `grid`.

A **0-indexed** `m x n` difference matrix `diff` is created with the following procedure:

- Let the number of ones in the `i^{th}` row be `onesRow_{i}`.

	- Let the number of ones in the `j^{th}` column be `onesCol_{j}`.

	- Let the number of zeros in the `i^{th}` row be `zerosRow_{i}`.

	- Let the number of zeros in the `j^{th}` column be `zerosCol_{j}`.

	- `diff[i][j] = onesRow_{i} + onesCol_{j} - zerosRow_{i} - zerosCol_{j}`

Return *the difference matrix *`diff`.

**Example 1:**

```
**Input:** grid = [[0,1,1],[1,0,1],[0,0,1]]
**Output:** [[0,0,4],[0,0,4],[-2,-2,2]]
**Explanation:**
- diff[0][0] = onesRow_{0} + onesCol_{0} - zerosRow_{0} - zerosCol_{0} = 2 + 1 - 1 - 2 = 0
- diff[0][1] = onesRow_{0} + onesCol_{1} - zerosRow_{0} - zerosCol_{1} = 2 + 1 - 1 - 2 = 0
- diff[0][2] = onesRow_{0} + onesCol_{2} - zerosRow_{0} - zerosCol_{2} = 2 + 3 - 1 - 0 = 4
- diff[1][0] = onesRow_{1} + onesCol_{0} - zerosRow_{1} - zerosCol_{0} = 2 + 1 - 1 - 2 = 0
- diff[1][1] = onesRow_{1} + onesCol_{1} - zerosRow_{1} - zerosCol_{1} = 2 + 1 - 1 - 2 = 0
- diff[1][2] = onesRow_{1} + onesCol_{2} - zerosRow_{1} - zerosCol_{2} = 2 + 3 - 1 - 0 = 4
- diff[2][0] = onesRow_{2} + onesCol_{0} - zerosRow_{2} - zerosCol_{0} = 1 + 1 - 2 - 2 = -2
- diff[2][1] = onesRow_{2} + onesCol_{1} - zerosRow_{2} - zerosCol_{1} = 1 + 1 - 2 - 2 = -2
- diff[2][2] = onesRow_{2} + onesCol_{2} - zerosRow_{2} - zerosCol_{2} = 1 + 3 - 2 - 0 = 2
```

**Example 2:**

```
**Input:** grid = [[1,1,1],[1,1,1]]
**Output:** [[5,5,5],[5,5,5]]
**Explanation:**
- diff[0][0] = onesRow_{0} + onesCol_{0} - zerosRow_{0} - zerosCol_{0} = 3 + 2 - 0 - 0 = 5
- diff[0][1] = onesRow_{0} + onesCol_{1} - zerosRow_{0} - zerosCol_{1} = 3 + 2 - 0 - 0 = 5
- diff[0][2] = onesRow_{0} + onesCol_{2} - zerosRow_{0} - zerosCol_{2} = 3 + 2 - 0 - 0 = 5
- diff[1][0] = onesRow_{1} + onesCol_{0} - zerosRow_{1} - zerosCol_{0} = 3 + 2 - 0 - 0 = 5
- diff[1][1] = onesRow_{1} + onesCol_{1} - zerosRow_{1} - zerosCol_{1} = 3 + 2 - 0 - 0 = 5
- diff[1][2] = onesRow_{1} + onesCol_{2} - zerosRow_{1} - zerosCol_{2} = 3 + 2 - 0 - 0 = 5
```

**Constraints:**

- `m == grid.length`

	- `n == grid[i].length`

	- `1 <= m, n <= 10^{5}`

	- `1 <= m * n <= 10^{5}`

	- `grid[i][j]` is either `0` or `1`.

### Hints

1. You need to reuse information about a row or a column many times. Try storing it to avoid computing it multiple times.
2. Use an array to store the number of 1’s in each row and another array to store the number of 1’s in each column. Once you know the number of 1’s in each row or column, you can also easily calculate the number of 0’s.

## Approach

<!-- Describe your solution approach here -->

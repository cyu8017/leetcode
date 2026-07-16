# 3938. Maximum Path Intersection Sum in a Grid

- **Difficulty:** Medium
- **LeetCode:** [https://leetcode.com/problems/maximum-path-intersection-sum-in-a-grid/](https://leetcode.com/problems/maximum-path-intersection-sum-in-a-grid/)
- **Tags:** array, dynamic-programming, matrix, prefix-sum

## Problem

You are given an `m x n` integer matrix `grid`.

Two players move across the grid:

- Player 1 starts at the top-left cell `(0, 0)` and can move only right or down. Their destination is the bottom-right cell `(m - 1, n - 1)`.

	- Player 2 starts at the bottom-left cell `(m - 1, 0)` and can move only right or up. Their destination is the top-right cell `(0, n - 1)`.

Each player must choose a valid path from their respective starting cell to their destination.

A cell is called **shared** if it belongs to **both** chosen paths.

Return an integer denoting the **maximum** possible sum of values of all **shared** cells.

**Example 1:**

​​​​​​​​​​​​​​​​​​​​​

**Input:** grid = [[1,2,0,-3],[1,-2,1,0],[-4,2,-1,3],[3,-3,3,-2],[-1,-5,0,1]]

**Output:** 4

**Explanation:**

The diagram shows one optimal choice of paths.

- Player 1 follows the red/purple path from the top-left cell to the bottom-right cell:

- `(0, 0) → (1, 0) → (2, 0) → (2, 1) → (2, 2) → (2, 3) → (3, 3) → (4, 3)`





	- Player 2 follows the blue/purple path from the bottom-left cell to the top-right cell:

- `(4, 0) → (4, 1) → (3, 1) → (2, 1) → (2, 2) → (2, 3) → (1, 3) → (0, 3)`





	- The shared cells are `(2, 1)`, `(2, 2)`, and `(2, 3)`.

	- The sum is `2 + (-1) + 3 = 4`, which is the maximum possible sum.

**Example 2:**

**Input:** grid = [[4,-2,-3],[-1,-3,-1],[-4,2,-1]]

**Output:** 3

**Explanation:**

One optimal pair of paths is shown in the diagram.

- Player 1 follows the red/purple path:

- `(0, 0) → (1, 0) → (1, 1) → (1, 2) → (2, 2)`





	- Player 2 follows the blue/purple path:

- `(2, 0) → (1, 0) → (0, 0) → (0, 1) → (0, 2)`





	- The shared cells are `(0, 0)` and `(1, 0)`.

	- The sum is `4 + (-1) = 3`, which is the maximum possible.

**Constraints:**

- `m == grid.length`

	- `n == grid[i].length`

	- `2 <= m, n <= 1000`

	- `4 <= m * n <= 5 * 10^{5}`

	- `-100 <= grid[i][j] <= 100`

### Hints

1. Notice that the shared cells must be contiguous and lie on the same row or column.
2. Additionally, if we have exactly one shared cell, then it must not lie on the first/last row, or the first/last column.
3. Reduce this problem to a 1D max subarray sum (of length at least 2) , and check for all `m` rows and `n` columns, making sure that we handle the case with exactly one shared cell separately.
4. A slighly modified kadane's algorithm is required to enforce subarray sums to have length at least 2.

## Approach

<!-- Describe your solution approach here -->

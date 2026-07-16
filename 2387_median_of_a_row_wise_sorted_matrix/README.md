# 2387. Median of a Row Wise Sorted Matrix

- **Difficulty:** Medium
- **LeetCode:** [https://leetcode.com/problems/median-of-a-row-wise-sorted-matrix/](https://leetcode.com/problems/median-of-a-row-wise-sorted-matrix/)
- **Premium:** Yes
- **Tags:** array, binary-search, matrix

## Problem

Given an `m x n` matrix `grid` containing an **odd** number of integers where each row is sorted in **non-decreasing** order, return *the **median** of the matrix*.

You must solve the problem in less than `O(m * n)` time complexity.



**Example 1:**

**Input:** grid = [[1,1,2],[2,3,3],[1,3,4]]
**Output:** 2
**Explanation:** The elements of the matrix in sorted order are 1,1,1,2,2,3,3,3,4. The median is 2.

**Example 2:**

**Input:** grid = [[1,1,3,3,4]]
**Output:** 3
**Explanation:** The elements of the matrix in sorted order are 1,1,3,3,4. The median is 3.



**Constraints:**

	- `m == grid.length`

	- `n == grid[i].length`

	- `1 <= m, n <= 500`

	- `m` and `n` are both odd.

	- `1 <= grid[i][j] <= 10^{6}`

	- `grid[i]` is sorted in non-decreasing order.

---
_Problem text from the [doocs/leetcode](https://github.com/doocs/leetcode) community mirror (LeetCode Premium)._

### Hints

1. How can you use the fact that the rows are sorted in non-decreasing order to solve the problem efficiently?
2. Try to binary search the answer.

## Approach

<!-- Describe your solution approach here -->

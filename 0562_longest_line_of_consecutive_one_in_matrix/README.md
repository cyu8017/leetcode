# 0562. Longest Line of Consecutive One in Matrix

- **Difficulty:** Medium
- **LeetCode:** [https://leetcode.com/problems/longest-line-of-consecutive-one-in-matrix/](https://leetcode.com/problems/longest-line-of-consecutive-one-in-matrix/)
- **Premium:** Yes
- **Tags:** array, dynamic-programming, matrix

## Problem

Given an `m x n` binary matrix `mat`, return *the length of the longest line of consecutive one in the matrix*.

The line could be horizontal, vertical, diagonal, or anti-diagonal.



**Example 1:**

**Input:** mat = [[0,1,1,0],[0,1,1,0],[0,0,0,1]]
**Output:** 3

**Example 2:**

**Input:** mat = [[1,1,1,1],[0,1,1,0],[0,0,0,1]]
**Output:** 4



**Constraints:**

	- `m == mat.length`

	- `n == mat[i].length`

	- `1 <= m, n <= 10^{4}`

	- `1 <= m * n <= 10^{4}`

	- `mat[i][j]` is either `0` or `1`.

---
_Problem text from the [doocs/leetcode](https://github.com/doocs/leetcode) community mirror (LeetCode Premium)._

### Hints

1. One solution is to count ones in each direction separately and find the longest line. Don't you think  it will take too much lines of code?
2. Is it possible to use some extra space to make the solution simple?
3. Can we use dynamic programming to make use of intermediate results?
4. Think of a 3D array which can be used to store the longest line obtained so far for each direction.

## Approach

<!-- Describe your solution approach here -->

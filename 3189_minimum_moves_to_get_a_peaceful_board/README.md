# 3189. Minimum Moves to Get a Peaceful Board

- **Difficulty:** Medium
- **LeetCode:** [https://leetcode.com/problems/minimum-moves-to-get-a-peaceful-board/](https://leetcode.com/problems/minimum-moves-to-get-a-peaceful-board/)
- **Premium:** Yes
- **Tags:** array, greedy, sorting, counting-sort

## Problem

Given a 2D array `rooks` of length `n`, where `rooks[i] = [x_{i}, y_{i}]` indicates the position of a rook on an `n x n` chess board. Your task is to move the rooks **1 cell **at a time vertically or horizontally (to an *adjacent* cell) such that the board becomes **peaceful**.

A board is **peaceful** if there is **exactly** one rook in each row and each column.

Return the **minimum** number of moves required to get a *peaceful board*.

**Note** that **at no point** can there be two rooks in the same cell.



**Example 1:**

**Input:** rooks = [[0,0],[1,0],[1,1]]

**Output:** 3

**Explanation:**

**Example 2:**

**Input:** rooks = [[0,0],[0,1],[0,2],[0,3]]

**Output:** 6

**Explanation:**



**Constraints:**

	- `1 <= n == rooks.length <= 500`

	- `0 <= x_{i}, y_{i} <= n - 1`

	- The input is generated such that there are no 2 rooks in the same cell.

---
_Problem text from the [doocs/leetcode](https://github.com/doocs/leetcode) community mirror (LeetCode Premium)._

### Hints

1. Think of a greedy method.
2. First, distribute the rooks in individual rows.
3. You can do this by sorting all rooks by their rows. Then assign the first one to the first row, the second one to the second row, and so on.
4. After you've distributed rooks across all rows, now do the same for columns.
5. Sort rooks by their columns and then assign the first one to the first column and so on.

## Approach

<!-- Describe your solution approach here -->

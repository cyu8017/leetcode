# 0531. Lonely Pixel I

- **Difficulty:** Medium
- **LeetCode:** [https://leetcode.com/problems/lonely-pixel-i/](https://leetcode.com/problems/lonely-pixel-i/)
- **Premium:** Yes
- **Tags:** array, hash-table, matrix

## Problem

Given an `m x n` `picture` consisting of black `'B'` and white `'W'` pixels, return *the number of **black** lonely pixels*.

A black lonely pixel is a character `'B'` that located at a specific position where the same row and same column don't have **any other** black pixels.



**Example 1:**

**Input:** picture = [["W","W","B"],["W","B","W"],["B","W","W"]]
**Output:** 3
**Explanation:** All the three 'B's are black lonely pixels.

**Example 2:**

**Input:** picture = [["B","B","B"],["B","B","W"],["B","B","B"]]
**Output:** 0



**Constraints:**

	- `m == picture.length`

	- `n == picture[i].length`

	- `1 <= m, n <= 500`

	- `picture[i][j]` is `'W'` or `'B'`.

---
_Problem text from the [doocs/leetcode](https://github.com/doocs/leetcode) community mirror (LeetCode Premium)._

## Approach

<!-- Describe your solution approach here -->

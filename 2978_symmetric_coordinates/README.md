# 2978. Symmetric Coordinates

- **Difficulty:** Medium
- **LeetCode:** [https://leetcode.com/problems/symmetric-coordinates/](https://leetcode.com/problems/symmetric-coordinates/)
- **Premium:** Yes
- **Tags:** database

## Problem

Table: `Coordinates`

+-------------+------+
| Column Name | Type |
+-------------+------+
| X           | int  |
| Y           | int  |
+-------------+------+
Each row includes X and Y, where both are integers. Table may contain duplicate values.

Two coordindates `(X1, Y1)` and `(X2, Y2)` are said to be **symmetric** coordintes if `X1 == Y2` and `X2 == Y1`.

Write a solution that outputs, among all these **symmetric** **coordintes**, only those **unique** coordinates that satisfy the condition `X1 <= Y1`.

Return *the result table ordered by *`X` *and * `Y` *(respectively)* *in **ascending order***.

The result format is in the following example.



**Example 1:**

**Input:**
Coordinates table:
+----+----+
| X  | Y  |
+----+----+
| 20 | 20 |
| 20 | 20 |
| 20 | 21 |
| 23 | 22 |
| 22 | 23 |
| 21 | 20 |
+----+----+
**Output:**
+----+----+
| x  | y  |
+----+----+
| 20 | 20 |
| 20 | 21 |
| 22 | 23 |
+----+----+
**Explanation:**
- (20, 20) and (20, 20) are symmetric coordinates because, X1 == Y2 and X2 == Y1. This results in displaying (20, 20) as a distinctive coordinates.
- (20, 21) and (21, 20) are symmetric coordinates because, X1 == Y2 and X2 == Y1. However, only (20, 21) will be displayed because X1

---
_Problem text from the [doocs/leetcode](https://github.com/doocs/leetcode) community mirror (LeetCode Premium)._

## Approach

<!-- Describe your solution approach here -->

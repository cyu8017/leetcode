# 0356. Line Reflection

- **Difficulty:** Medium
- **LeetCode:** [https://leetcode.com/problems/line-reflection/](https://leetcode.com/problems/line-reflection/)
- **Premium:** Yes
- **Tags:** array, hash-table, math

## Problem

Given `n` points on a 2D plane, find if there is such a line parallel to the y-axis that reflects the given points symmetrically.

In other words, answer whether or not if there exists a line that after reflecting all points over the given line, the original points' set is the same as the reflected ones.

**Note** that there can be repeated points.



**Example 1:**

**Input:** points = [[1,1],[-1,1]]
**Output:** true
**Explanation:** We can choose the line x = 0.

**Example 2:**

**Input:** points = [[1,1],[-1,-1]]
**Output:** false
**Explanation:** We can't choose a line.



**Constraints:**

	- `n == points.length`

	- `1 <= n <= 10^{4}`

	- `-10^{8} <= points[i][j] <= 10^{8}`



**Follow up:** Could you do better than `O(n^{2})`?

---
_Problem text from the [doocs/leetcode](https://github.com/doocs/leetcode) community mirror (LeetCode Premium)._

### Hints

1. Find the smallest and largest x-value for all points.
2. If there is a line then it should be at y = (minX + maxX) / 2.
3. For each point, make sure that it has a reflected point in the opposite side.

## Approach

<!-- Describe your solution approach here -->

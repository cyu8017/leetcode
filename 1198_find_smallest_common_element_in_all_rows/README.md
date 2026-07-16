# 1198. Find Smallest Common Element in All Rows

- **Difficulty:** Medium
- **LeetCode:** [https://leetcode.com/problems/find-smallest-common-element-in-all-rows/](https://leetcode.com/problems/find-smallest-common-element-in-all-rows/)
- **Premium:** Yes
- **Tags:** array, hash-table, binary-search, matrix, counting

## Problem

Given an `m x n` matrix `mat` where every row is sorted in **strictly** **increasing** order, return *the **smallest common element** in all rows*.

If there is no common element, return `-1`.



**Example 1:**

**Input:** mat = [[1,2,3,4,5],[2,4,5,8,10],[3,5,7,9,11],[1,3,5,7,9]]
**Output:** 5

**Example 2:**

**Input:** mat = [[1,2,3],[2,3,4],[2,3,5]]
**Output:** 2



**Constraints:**

	- `m == mat.length`

	- `n == mat[i].length`

	- `1 <= m, n <= 500`

	- `1 <= mat[i][j] <= 10^{4}`

	- `mat[i]` is sorted in strictly increasing order.

---
_Problem text from the [doocs/leetcode](https://github.com/doocs/leetcode) community mirror (LeetCode Premium)._

### Hints

1. Notice that each row has no duplicates.
2. Is counting the frequency of elements enough to find the answer?
3. Use a data structure to count the frequency of elements.
4. Find an element whose frequency equals the number of rows.

## Approach

<!-- Describe your solution approach here -->

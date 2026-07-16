# 3682. Minimum Index Sum of Common Elements

- **Difficulty:** Medium
- **LeetCode:** [https://leetcode.com/problems/minimum-index-sum-of-common-elements/](https://leetcode.com/problems/minimum-index-sum-of-common-elements/)
- **Premium:** Yes
- **Tags:** array, hash-table

## Problem

You are given two integer arrays `nums1` and `nums2` of equal length `n`.

We define a pair of indices `(i, j)` as a **good pair** if `nums1[i] == nums2[j]`.

Return the **minimum index sum** `i + j` among all possible good pairs. If no such pairs exist, return -1.



**Example 1:**

**Input:** nums1 = [3,2,1], nums2 = [1,3,1]

**Output:** 1

**Explanation:**

	- Common elements between `nums1` and `nums2` are 1 and 3.

	- For 3, `[i, j] = [0, 1]`, giving an index sum of `i + j = 1`.

	- For 1, `[i, j] = [2, 0]`, giving an index sum of `i + j = 2`.

	- The minimum index sum is 1.

**Example 2:**

**Input:** nums1 = [5,1,2], nums2 = [2,1,3]

**Output:** 2

**Explanation:**

	- Common elements between `nums1` and `nums2` are 1 and 2.

	- For 1, `[i, j] = [1, 1]`, giving an index sum of `i + j = 2`.

	- For 2, `[i, j] = [2, 0]`, giving an index sum of `i + j = 2`.

	- The minimum index sum is 2.

**Example 3:**

**Input:** nums1 = [6,4], nums2 = [7,8]

**Output:** -1

**Explanation:**

	- Since no common elements between `nums1` and `nums2`, the output is -1.



**Constraints:**

	- `1 <= nums1.length == nums2.length <= 10^{5}`

	- `-10^{5} <= nums1[i], nums2[i] <= 10^{5}`

---
_Problem text from the [doocs/leetcode](https://github.com/doocs/leetcode) community mirror (LeetCode Premium)._

### Hints

1. Build a hash map `pos1` that stores, for each value in `nums1`, the smallest index where it appears.
2. Iterate through `nums2`. For each index `j`, if `nums2[j]` exists in `pos1`, compute `pos1[nums2[j]] + j`.
3. Track the minimum index sum across all such matches.
4. If no common element is found, return `-1`.

## Approach

<!-- Describe your solution approach here -->

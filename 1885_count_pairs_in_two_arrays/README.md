# 1885. Count Pairs in Two Arrays

- **Difficulty:** Medium
- **LeetCode:** [https://leetcode.com/problems/count-pairs-in-two-arrays/](https://leetcode.com/problems/count-pairs-in-two-arrays/)
- **Premium:** Yes
- **Tags:** array, two-pointers, binary-search, sorting

## Problem

Given two integer arrays `nums1` and `nums2` of length `n`, count the pairs of indices `(i, j)` such that `i < j` and `nums1[i] + nums1[j] > nums2[i] + nums2[j]`.

Return *the **number of pairs** satisfying the condition.*



**Example 1:**

**Input:** nums1 = [2,1,2,1], nums2 = [1,2,1,2]
**Output:** 1
**Explanation**: The pairs satisfying the condition are:
- (0, 2) where 2 + 2 > 1 + 1.

**Example 2:**

**Input:** nums1 = [1,10,6,2], nums2 = [1,4,1,5]
**Output:** 5
**Explanation**: The pairs satisfying the condition are:
- (0, 1) where 1 + 10 > 1 + 4.
- (0, 2) where 1 + 6 > 1 + 1.
- (1, 2) where 10 + 6 > 4 + 1.
- (1, 3) where 10 + 2 > 4 + 5.
- (2, 3) where 6 + 2 > 1 + 5.



**Constraints:**

	- `n == nums1.length == nums2.length`

	- `1 <= n <= 10^{5}`

	- `1 <= nums1[i], nums2[i] <= 10^{5}`

---
_Problem text from the [doocs/leetcode](https://github.com/doocs/leetcode) community mirror (LeetCode Premium)._

### Hints

1. We can write it as nums1[i] - nums2[i] > nums2[j] - nums1[j] instead of nums1[i] + nums1[j] > nums2[i] + nums2[j].
2. Store nums1[idx] - nums2[idx] in a data structure.
3. Store nums2[idx] - nums1[idx] in a different data structure.
4. For each integer in the first data structure, count the number of the strictly smaller integers in the second data structure with a larger index in the original array.

## Approach

<!-- Describe your solution approach here -->

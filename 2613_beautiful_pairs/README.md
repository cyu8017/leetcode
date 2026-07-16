# 2613. Beautiful Pairs

- **Difficulty:** Hard
- **LeetCode:** [https://leetcode.com/problems/beautiful-pairs/](https://leetcode.com/problems/beautiful-pairs/)
- **Premium:** Yes
- **Tags:** array, math, divide-and-conquer, geometry, sorting, ordered-set

## Problem

You are given two **0-indexed** integer arrays `nums1` and `nums2` of the same length. A pair of indices `(i,j)` is called **beautiful** if`|nums1[i] - nums1[j]| + |nums2[i] - nums2[j]|` is the smallest amongst all possible indices pairs where `i < j`.

Return *the beautiful pair. In the case that there are multiple beautiful pairs, return the lexicographically smallest pair.*

Note that

	- `|x|` denotes the absolute value of `x`.

	- A pair of indices `(i_{1}, j_{1})` is lexicographically smaller than `(i_{2}, j_{2})` if `i_{1} < i_{2}` or `i_{1} == i_{2}` and `j_{1} < j_{2}`.



**Example 1:**

**Input:** nums1 = [1,2,3,2,4], nums2 = [2,3,1,2,3]
**Output:** [0,3]
**Explanation:** Consider index 0 and index 3. The value of |nums1[i]-nums1[j]| + |nums2[i]-nums2[j]| is 1, which is the smallest value we can achieve.

**Example 2:**

**Input:** nums1 = [1,2,4,3,2,5], nums2 = [1,4,2,3,5,1]
**Output:** [1,4]
**Explanation:** Consider index 1 and index 4. The value of |nums1[i]-nums1[j]| + |nums2[i]-nums2[j]| is 1, which is the smallest value we can achieve.



**Constraints:**

	- `2 <= nums1.length, nums2.length <= 10^{5}`

	- `nums1.length == nums2.length`

	- `0 <= nums1_{i}_{ }<= nums1.length`

	- `0 <= nums2_{i} <= nums2.length`

---
_Problem text from the [doocs/leetcode](https://github.com/doocs/leetcode) community mirror (LeetCode Premium)._

### Hints

1. Use Range Queries Data Structures to optimize the algorithm

## Approach

<!-- Describe your solution approach here -->

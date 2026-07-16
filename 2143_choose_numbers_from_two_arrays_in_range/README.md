# 2143. Choose Numbers From Two Arrays in Range

- **Difficulty:** Hard
- **LeetCode:** [https://leetcode.com/problems/choose-numbers-from-two-arrays-in-range/](https://leetcode.com/problems/choose-numbers-from-two-arrays-in-range/)
- **Premium:** Yes
- **Tags:** array, dynamic-programming

## Problem

You are given two **0-indexed** integer arrays `nums1` and `nums2` of length `n`.

A range `[l, r]` (**inclusive**) where `0 <= l <= r < n` is **balanced** if:

	- For every `i` in the range `[l, r]`, you pick either `nums1[i]` or `nums2[i]`.

	- The sum of the numbers you pick from `nums1` equals to the sum of the numbers you pick from `nums2` (the sum is considered to be `0` if you pick no numbers from an array).

Two **balanced** ranges from `[l_{1}, r_{1}]` and `[l_{2}, r_{2}]` are considered to be **different** if at least one of the following is true:

	- `l_{1} != l_{2}`

	- `r_{1} != r_{2}`

	- `nums1[i]` is picked in the first range, and `nums2[i]` is picked in the second range or **vice versa** for at least one `i`.

Return *the number of **different** ranges that are balanced. *Since the answer may be very large, return it **modulo** `10^{9} + 7`*.*



**Example 1:**

**Input:** nums1 = [1,2,5], nums2 = [2,6,3]
**Output:** 3
**Explanation:** The balanced ranges are:
- [0, 1] where we choose nums2[0], and nums1[1].
  The sum of the numbers chosen from nums1 equals the sum of the numbers chosen from nums2: 2 = 2.
- [0, 2] where we choose nums1[0], nums2[1], and nums1[2].
  The sum of the numbers chosen from nums1 equals the sum of the numbers chosen from nums2: 1 + 5 = 6.
- [0, 2] where we choose nums1[0], nums1[1], and nums2[2].
  The sum of the numbers chosen from nums1 equals the sum of the numbers chosen from nums2: 1 + 2 = 3.
Note that the second and third balanced ranges are different.
In the second balanced range, we choose nums2[1] and in the third balanced range, we choose nums1[1].

**Example 2:**

**Input:** nums1 = [0,1], nums2 = [1,0]
**Output:** 4
**Explanation:** The balanced ranges are:
- [0, 0] where we choose nums1[0].
  The sum of the numbers chosen from nums1 equals the sum of the numbers chosen from nums2: 0 = 0.
- [1, 1] where we choose nums2[1].
  The sum of the numbers chosen from nums1 equals the sum of the numbers chosen from nums2: 0 = 0.
- [0, 1] where we choose nums1[0] and nums2[1].
  The sum of the numbers chosen from nums1 equals the sum of the numbers chosen from nums2: 0 = 0.
- [0, 1] where we choose nums2[0] and nums1[1].
  The sum of the numbers chosen from nums1 equals the sum of the numbers chosen from nums2: 1 = 1.



**Constraints:**

	- `n == nums1.length == nums2.length`

	- `1 <= n <= 100`

	- `0 <= nums1[i], nums2[i] <= 100`

---
_Problem text from the [doocs/leetcode](https://github.com/doocs/leetcode) community mirror (LeetCode Premium)._

### Hints

1. If you know the possible sums you can get for a range [l, r], how can you use this information to calculate the possible sums you can get for a range [l, r + 1]?
2. For the range [l, r], if it is possible to choose elements such that the sum of elements you picked from nums1 is x and the sum of elements you picked from nums2 is y, then (x + nums1[r + 1], y) and (x, y + nums2[r + 1]) are possible sums you can get in the range [l, r + 1].
3. How can we save the possible sums obtainable at a given index so that we can reuse this information later?

## Approach

<!-- Describe your solution approach here -->

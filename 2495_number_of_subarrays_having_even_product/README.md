# 2495. Number of Subarrays Having Even Product

- **Difficulty:** Medium
- **LeetCode:** [https://leetcode.com/problems/number-of-subarrays-having-even-product/](https://leetcode.com/problems/number-of-subarrays-having-even-product/)
- **Premium:** Yes
- **Tags:** array, math, dynamic-programming

## Problem

Given a **0-indexed** integer array `nums`, return *the number of subarrays of *`nums`* having an even product*.



**Example 1:**

**Input:** nums = [9,6,7,13]
**Output:** 6
**Explanation:** There are 6 subarrays with an even product:
- nums[0..1] = 9 * 6 = 54.
- nums[0..2] = 9 * 6 * 7 = 378.
- nums[0..3] = 9 * 6 * 7 * 13 = 4914.
- nums[1..1] = 6.
- nums[1..2] = 6 * 7 = 42.
- nums[1..3] = 6 * 7 * 13 = 546.

**Example 2:**

**Input:** nums = [7,3,5]
**Output:** 0
**Explanation:** There are no subarrays with an even product.



**Constraints:**

	- `1 <= nums.length <= 10^{5}`

	- `1 <= nums[i] <= 10^{5}`

---
_Problem text from the [doocs/leetcode](https://github.com/doocs/leetcode) community mirror (LeetCode Premium)._

### Hints

1. The product of elements in a subarray is even if it contains at least one even element.
2. Iterate from left to right and save the last index of an even number. Let that saved index be “j”.
3. It can be seen that every subarray starting from earlier than index “j” and ending at the current index has an even product.

## Approach

<!-- Describe your solution approach here -->

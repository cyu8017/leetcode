# 3717. Minimum Operations to Make the Array Beautiful

- **Difficulty:** Medium
- **LeetCode:** [https://leetcode.com/problems/minimum-operations-to-make-the-array-beautiful/](https://leetcode.com/problems/minimum-operations-to-make-the-array-beautiful/)
- **Premium:** Yes
- **Tags:** array, dynamic-programming

## Problem

You are given an integer array `nums`.

An array is called **beautiful** if for every index `i > 0`, the value at `nums[i]` is **divisible** by `nums[i - 1]`.

In one operation, you may **increment** any element `nums[i]` (with `i > 0`) by `1`.

Return the **minimum number of operations** required to make the array beautiful.



**Example 1:**

**Input:** nums = [3,7,9]

**Output:** 2

**Explanation:**

Applying the operation twice on `nums[1]` makes the array beautiful: `[3,9,9]`

**Example 2:**

**Input:** nums = [1,1,1]

**Output:** 0

**Explanation:**

The given array is already beautiful.

**Example 3:**

**Input:** nums = [4]

**Output:** 0

**Explanation:**

The array has only one element, so it's already beautiful.



**Constraints:**

	- `1 <= nums.length <= 100`

	- `1 <= nums[i] <= 50​​​`

---
_Problem text from the [doocs/leetcode](https://github.com/doocs/leetcode) community mirror (LeetCode Premium)._

### Hints

1. Use dynamic programming.
2. For each index `i`, compute `dp[i][val]` where `dp[i][val]` is the minimum number of increments needed to make position `i` equal to `val`.
3. Carefully combine DP states for index `i` with those for index `i - 1`.

## Approach

<!-- Describe your solution approach here -->

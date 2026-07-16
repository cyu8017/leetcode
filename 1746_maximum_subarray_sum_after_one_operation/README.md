# 1746. Maximum Subarray Sum After One Operation

- **Difficulty:** Medium
- **LeetCode:** [https://leetcode.com/problems/maximum-subarray-sum-after-one-operation/](https://leetcode.com/problems/maximum-subarray-sum-after-one-operation/)
- **Premium:** Yes
- **Tags:** array, dynamic-programming

## Problem

You are given an integer array `nums`. You must perform **exactly one** operation where you can **replace** one element `nums[i]` with `nums[i] * nums[i]`.

Return *the **maximum** possible subarray sum after **exactly one** operation*. The subarray must be non-empty.



**Example 1:**

**Input:** nums = [2,-1,-4,-3]

**Output:** 17

**Explanation:** You can perform the operation on index 2 (0-indexed) to make nums = [2,-1,**16**,-3]. Now, the maximum subarray sum is 2 + -1 + 16 = 17.

**Example 2:**

**Input:** nums = [1,-1,1,1,-1,-1,1]

**Output:** 4

**Explanation:** You can perform the operation on index 1 (0-indexed) to make nums = [1,**1**,1,1,-1,-1,1]. Now, the maximum subarray sum is 1 + 1 + 1 + 1 = 4.



**Constraints:**

    - `1 <= nums.length <= 10^{5}`

    - `-10^{4} <= nums[i] <= 10^{4}`

---
_Problem text from the [doocs/leetcode](https://github.com/doocs/leetcode) community mirror (LeetCode Premium)._

### Hints

1. Think about dynamic programming
2. Define an array dp[nums.length][2], where dp[i][0] is the max subarray sum including nums[i] and without squaring any element.
3. dp[i][1] is the max subarray sum including nums[i] and having only one element squared.

## Approach

<!-- Describe your solution approach here -->

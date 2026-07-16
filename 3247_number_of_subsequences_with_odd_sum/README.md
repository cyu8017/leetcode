# 3247. Number of Subsequences with Odd Sum

- **Difficulty:** Medium
- **LeetCode:** [https://leetcode.com/problems/number-of-subsequences-with-odd-sum/](https://leetcode.com/problems/number-of-subsequences-with-odd-sum/)
- **Premium:** Yes
- **Tags:** array, math, dynamic-programming, combinatorics

## Problem

Given an array `nums`, return the number of subsequences with an odd sum of elements.

Since the answer may be very large, return it **modulo** `10^{9} + 7`.



**Example 1:**

**Input:** nums = [1,1,1]

**Output:** 4

**Explanation:**

The odd-sum subsequences are: `[1, 1, 1]`, `[1, 1, 1],` `[1, 1, 1]`, `[1, 1, 1]`.

**Example 2:**

**Input:** nums = [1,2,2]

**Output:** 4

**Explanation:**

The odd-sum subsequences are: `[1, 2, 2]`, `[1, 2, 2],` `[1, 2, 2]`, `[1, 2, 2]`.



**Constraints:**

	- `1 <= nums.length <= 10^{5}`

	- `1 <= nums[i] <= 10^{9}`

---
_Problem text from the [doocs/leetcode](https://github.com/doocs/leetcode) community mirror (LeetCode Premium)._

### Hints

1. Define `dp[i][0]` as the answer for the subarray `[0, i]`.
2. Similarly define `dp[i][1]` as the answer for the subarray `[0, i]` if we wanted to count even-sum subsequences.
3. If `nums[i]` is odd, `dp[i][x] = 2^{i}`.
4. Otherwise, `dp[i][x] = dp[i - 1][x] * 2`.
5. `dp[0][1] = 1` if `nums[0]` is odd, and 0 otherwise.
6. `dp[0][0] = 2` if `nums[0]` is even, and 1 otherwise (since an empty subsequence has an even sum).

## Approach

<!-- Describe your solution approach here -->

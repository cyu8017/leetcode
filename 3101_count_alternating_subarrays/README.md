# 3101. Count Alternating Subarrays

- **Difficulty:** Medium
- **LeetCode:** [https://leetcode.com/problems/count-alternating-subarrays/](https://leetcode.com/problems/count-alternating-subarrays/)
- **Tags:** array, math

## Problem

You are given a binary array `nums`.

We call a subarray **alternating** if **no** two **adjacent** elements in the subarray have the **same** value.

Return *the number of alternating subarrays in *`nums`.

**Example 1:**

**Input:** nums = [0,1,1,1]

**Output:** 5

**Explanation:**

The following subarrays are alternating: `[0]`, `[1]`, `[1]`, `[1]`, and `[0,1]`.

**Example 2:**

**Input:** nums = [1,0,1,0]

**Output:** 10

**Explanation:**

Every subarray of the array is alternating. There are 10 possible subarrays that we can choose.

**Constraints:**

- `1 <= nums.length <= 10^{5}`

	- `nums[i]` is either `0` or `1`.

### Hints

1. Try using dynamic programming.
2. Let `dp[i]` be the number of alternating subarrays ending at index `i`.
3. The final answer is the sum of `dp[i]` over all  indices `i` from `0` to `n - 1`.

## Approach

<!-- Describe your solution approach here -->

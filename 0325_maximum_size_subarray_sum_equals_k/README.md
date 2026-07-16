# 0325. Maximum Size Subarray Sum Equals k

- **Difficulty:** Medium
- **LeetCode:** [https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/](https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/)
- **Premium:** Yes
- **Tags:** array, hash-table, prefix-sum

## Problem

Given an integer array `nums` and an integer `k`, return *the maximum length of a **subarray** that sums to* `k`. If there is not one, return `0` instead.



**Example 1:**

**Input:** nums = [1,-1,5,-2,3], k = 3
**Output:** 4
**Explanation:** The subarray [1, -1, 5, -2] sums to 3 and is the longest.

**Example 2:**

**Input:** nums = [-2,-1,2,1], k = 1
**Output:** 2
**Explanation:** The subarray [-1, 2] sums to 1 and is the longest.



**Constraints:**

	- `1 <= nums.length <= 2 * 10^{5}`

	- `-10^{4} <= nums[i] <= 10^{4}`

	- `-10^{9} <= k <= 10^{9}`

---
_Problem text from the [doocs/leetcode](https://github.com/doocs/leetcode) community mirror (LeetCode Premium)._

### Hints

1. Compute the prefix sum array where psum[i] is the sum of all the elements from *0* to *i*.
2. At each index *i*, the sum of the prefix is psum[i], so we are searching for the index x where psum[x] = psum[i] - k.
The subarray [x + 1, i] will be of sum k.
3. Use a hashmap to get the index x efficiently or to determine that it does not exist.

## Approach

<!-- Describe your solution approach here -->

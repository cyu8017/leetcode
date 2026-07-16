# 1099. Two Sum Less Than K

- **Difficulty:** Easy
- **LeetCode:** [https://leetcode.com/problems/two-sum-less-than-k/](https://leetcode.com/problems/two-sum-less-than-k/)
- **Premium:** Yes
- **Tags:** array, two-pointers, binary-search, sorting

## Problem

Given an array `nums` of integers and integer `k`, return the maximum `sum` such that there exists `i < j` with `nums[i] + nums[j] = sum` and `sum < k`. If no `i`, `j` exist satisfying this equation, return `-1`.



**Example 1:**

**Input:** nums = [34,23,1,24,75,33,54,8], k = 60
**Output:** 58
**Explanation: **We can use 34 and 24 to sum 58 which is less than 60.

**Example 2:**

**Input:** nums = [10,20,30], k = 15
**Output:** -1
**Explanation: **In this case it is not possible to get a pair sum less that 15.



**Constraints:**

	- `1 <= nums.length <= 100`

	- `1 <= nums[i] <= 1000`

	- `1 <= k <= 2000`

---
_Problem text from the [doocs/leetcode](https://github.com/doocs/leetcode) community mirror (LeetCode Premium)._

### Hints

1. What if we have the array sorted?
2. Loop the array and get the value A[i] then we need to find a value A[j] such that A[i] + A[j] < K  which means A[j] < K - A[i]. In order to do that we can find that value with a binary search.

## Approach

<!-- Describe your solution approach here -->

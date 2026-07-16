# 3231. Minimum Number of Increasing Subsequence to Be Removed

- **Difficulty:** Hard
- **LeetCode:** [https://leetcode.com/problems/minimum-number-of-increasing-subsequence-to-be-removed/](https://leetcode.com/problems/minimum-number-of-increasing-subsequence-to-be-removed/)
- **Premium:** Yes
- **Tags:** array, binary-search

## Problem

Given an array of integers `nums`, you are allowed to perform the following operation any number of times:

	- Remove a **strictly increasing** subsequence from the array.

Your task is to find the **minimum** number of operations required to make the array **empty**.



**Example 1:**

**Input:** nums = [5,3,1,4,2]

**Output:** 3

**Explanation:**

We remove subsequences `[1, 2]`, `[3, 4]`, `[5]`.

**Example 2:**

**Input:** nums = [1,2,3,4,5]

**Output:** 1

**Example 3:**

**Input:** nums = [5,4,3,2,1]

**Output:** 5



**Constraints:**

	- `1 <= nums.length <= 10^{5}`

	- `1 <= nums[i] <= 10^{5}`

---
_Problem text from the [doocs/leetcode](https://github.com/doocs/leetcode) community mirror (LeetCode Premium)._

### Hints

1. Find the longest non-increasing subsequence.
2. No two elements of this sequence can be removed in one operation.
3. Try to prove that the answer is equal to the length of this sequence.

## Approach

<!-- Describe your solution approach here -->

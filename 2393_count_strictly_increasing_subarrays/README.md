# 2393. Count Strictly Increasing Subarrays

- **Difficulty:** Medium
- **LeetCode:** [https://leetcode.com/problems/count-strictly-increasing-subarrays/](https://leetcode.com/problems/count-strictly-increasing-subarrays/)
- **Premium:** Yes
- **Tags:** array, math, dynamic-programming

## Problem

You are given an array `nums` consisting of **positive** integers.

Return *the number of **subarrays** of *`nums`* that are in **strictly increasing** order.*

A **subarray** is a **contiguous** part of an array.



**Example 1:**

**Input:** nums = [1,3,5,4,4,6]
**Output:** 10
**Explanation:** The strictly increasing subarrays are the following:
- Subarrays of length 1: [1], [3], [5], [4], [4], [6].
- Subarrays of length 2: [1,3], [3,5], [4,6].
- Subarrays of length 3: [1,3,5].
The total number of subarrays is 6 + 3 + 1 = 10.

**Example 2:**

**Input:** nums = [1,2,3,4,5]
**Output:** 15
**Explanation:** Every subarray is strictly increasing. There are 15 possible subarrays that we can take.



**Constraints:**

	- `1 <= nums.length <= 10^{5}`

	- `1 <= nums[i] <= 10^{6}`

---
_Problem text from the [doocs/leetcode](https://github.com/doocs/leetcode) community mirror (LeetCode Premium)._

### Hints

1. Find the number of strictly increasing subarrays that end at a specific index. Can you calculate that for each index from 0 to n - 1?
2. The answer will be the sum of the number of subarrays that end at each index.

## Approach

<!-- Describe your solution approach here -->

# 3641. Longest Semi-Repeating Subarray

- **Difficulty:** Medium
- **LeetCode:** [https://leetcode.com/problems/longest-semi-repeating-subarray/](https://leetcode.com/problems/longest-semi-repeating-subarray/)
- **Premium:** Yes
- **Tags:** array, hash-table, sliding-window

## Problem

You are given an integer array `nums` of length `n` and an integer `k`.

A **semi‑repeating** subarray is a contiguous subarray in which at most `k` elements repeat (i.e., appear more than once).

Return the length of the longest **semi‑repeating** subarray in `nums`.



**Example 1:**

**Input:** nums = [1,2,3,1,2,3,4], k = 2

**Output:** 6

**Explanation:**

The longest semi-repeating subarray is `[2, 3, 1, 2, 3, 4]`, which has two repeating elements (2 and 3).

**Example 2:**

**Input:** nums = [1,1,1,1,1], k = 4

**Output:** 5

**Explanation:**

The longest semi-repeating subarray is `[1, 1, 1, 1, 1]`, which has only one repeating element (1).

**Example 3:**

**Input:** nums = [1,1,1,1,1], k = 0

**Output:** 1

**Explanation:**

The longest semi-repeating subarray is `[1]`, which has no repeating elements.



**Constraints:**

	- `1 <= nums.length <= 10^{5}`

	- `1 <= nums[i] <= 10^{5}`

	- `0 <= k <= nums.length`

---
_Problem text from the [doocs/leetcode](https://github.com/doocs/leetcode) community mirror (LeetCode Premium)._

### Hints

1. Use a sliding window with left/right pointers.
2. Keep a freq map and a count of elements with freq > 1.
3. If repeating-count `> k`, shift the left pointer until it's `<= k`.

## Approach

<!-- Describe your solution approach here -->

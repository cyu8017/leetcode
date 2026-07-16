# 0930. Binary Subarrays With Sum

- **Difficulty:** Medium
- **LeetCode:** [https://leetcode.com/problems/binary-subarrays-with-sum/](https://leetcode.com/problems/binary-subarrays-with-sum/)
- **Tags:** array, hash-table, sliding-window, prefix-sum

## Problem

Given a binary array `nums` and an integer `goal`, return *the number of non-empty **subarrays** with a sum* `goal`.

A **subarray** is a contiguous part of the array.

**Example 1:**

```
**Input:** nums = [1,0,1,0,1], goal = 2
**Output:** 4
**Explanation:** The 4 subarrays are bolded and underlined below:
[**1,0,1**,0,1]
[**1,0,1,0**,1]
[1,**0,1,0,1**]
[1,0,**1,0,1**]
```

**Example 2:**

```
**Input:** nums = [0,0,0,0,0], goal = 0
**Output:** 15
```

**Constraints:**

- `1 <= nums.length <= 3 * 10^{4}`

	- `nums[i]` is either `0` or `1`.

	- `0 <= goal <= nums.length`

### Hints

1. Can you transform the problem into finding two prefix sums whose difference equals `goal`?
2. While iterating through the array, keep track of how many times each prefix sum has appeared so far.
3. If the current prefix sum is `curr`, how many previous prefix sums equal to `curr - goal` exist?

## Approach

<!-- Describe your solution approach here -->

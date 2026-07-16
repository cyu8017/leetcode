# 1862. Sum of Floored Pairs

- **Difficulty:** Hard
- **LeetCode:** [https://leetcode.com/problems/sum-of-floored-pairs/](https://leetcode.com/problems/sum-of-floored-pairs/)
- **Tags:** array, math, binary-search, counting, enumeration, prefix-sum

## Problem

Given an integer array `nums`, return the sum of `floor(nums[i] / nums[j])` for all pairs of indices `0 <= i, j < nums.length` in the array. Since the answer may be too large, return it **modulo** `10^{9} + 7`.

The `floor()` function returns the integer part of the division.

**Example 1:**

```
**Input:** nums = [2,5,9]
**Output:** 10
**Explanation:**
floor(2 / 5) = floor(2 / 9) = floor(5 / 9) = 0
floor(2 / 2) = floor(5 / 5) = floor(9 / 9) = 1
floor(5 / 2) = 2
floor(9 / 2) = 4
floor(9 / 5) = 1
We calculate the floor of the division for every pair of indices in the array then sum them up.
```

**Example 2:**

```
**Input:** nums = [7,7,7,7,7,7,7]
**Output:** 49
```

**Constraints:**

- `1 <= nums.length <= 10^{5}`

	- `1 <= nums[i] <= 10^{5}`

### Hints

1. Find the frequency (number of occurrences) of all elements in the array.
2. For each element, iterate through its multiples and multiply frequencies to find the answer.

## Approach

<!-- Describe your solution approach here -->

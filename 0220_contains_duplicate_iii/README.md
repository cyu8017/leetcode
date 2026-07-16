# 0220. Contains Duplicate III

- **Difficulty:** Hard
- **LeetCode:** [https://leetcode.com/problems/contains-duplicate-iii/](https://leetcode.com/problems/contains-duplicate-iii/)
- **Tags:** array, sliding-window, sorting, bucket-sort, ordered-set

## Problem

You are given an integer array `nums` and two integers `indexDiff` and `valueDiff`.

Find a pair of indices `(i, j)` such that:

- `i != j`,

	- `abs(i - j) <= indexDiff`.

	- `abs(nums[i] - nums[j]) <= valueDiff`, and

Return `true`* if such pair exists or *`false`* otherwise*.

**Example 1:**

```
**Input:** nums = [1,2,3,1], indexDiff = 3, valueDiff = 0
**Output:** true
**Explanation:** We can choose (i, j) = (0, 3).
We satisfy the three conditions:
i != j --> 0 != 3
abs(i - j)  abs(0 - 3)  abs(1 - 1) <= 0
```

**Example 2:**

```
**Input:** nums = [1,5,9,1,5,9], indexDiff = 2, valueDiff = 3
**Output:** false
**Explanation:** After trying all the possible pairs (i, j), we cannot satisfy the three conditions, so we return false.
```

**Constraints:**

- `2 <= nums.length <= 10^{5}`

	- `-10^{9} <= nums[i] <= 10^{9}`

	- `1 <= indexDiff <= nums.length`

	- `0 <= valueDiff <= 10^{9}`

### Hints

1. Time complexity O(n logk)  - This will give an indication that sorting is involved for k elements.
2. Use already existing state to evaluate next state  -  Like, a set of k sorted numbers are only needed to be tracked. When we are processing the next number in array, then we can utilize the existing sorted state and it is not necessary to sort next overlapping set of k numbers again.

## Approach

<!-- Describe your solution approach here -->

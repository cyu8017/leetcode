# 2200. Find All K-Distant Indices in an Array

- **Difficulty:** Easy
- **LeetCode:** [https://leetcode.com/problems/find-all-k-distant-indices-in-an-array/](https://leetcode.com/problems/find-all-k-distant-indices-in-an-array/)
- **Tags:** array, two-pointers

## Problem

You are given a **0-indexed** integer array `nums` and two integers `key` and `k`. A **k-distant index** is an index `i` of `nums` for which there exists at least one index `j` such that `|i - j| <= k` and `nums[j] == key`.

Return *a list of all k-distant indices sorted in **increasing order**.

**Example 1:**

```
**Input:** nums = [3,4,9,1,3,9,5], key = 9, k = 1
**Output:** [1,2,3,4,5,6]
**Explanation:** Here, nums[2] == key and nums[5] == key.
- For index 0, |0 - 2| > k and |0 - 5| > k, so there is no j where |0 - j|  and nums[j] == key. Thus, 0 is not a k-distant index.
- For index 1, |1 - 2| Thus, we return [1,2,3,4,5,6] which is sorted in increasing order.
```

**Example 2:**

```
**Input:** nums = [2,2,2,2,2], key = 2, k = 2
**Output:** [0,1,2,3,4]
**Explanation:** For all indices i in nums, there exists some index j such that |i - j| <= k and nums[j] == key, so every index is a k-distant index.
Hence, we return [0,1,2,3,4].
```

**Constraints:**

- `1 <= nums.length <= 1000`

	- `1 <= nums[i] <= 1000`

	- `key` is an integer from the array `nums`.

	- `1 <= k <= nums.length`

### Hints

1. For every occurrence of key in nums, find all indices within distance k from it.
2. Use a hash table to remove duplicate indices.

## Approach

<!-- Describe your solution approach here -->

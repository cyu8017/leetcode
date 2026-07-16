# 3978. Unique Middle Element

- **Difficulty:** Easy
- **LeetCode:** [https://leetcode.com/problems/unique-middle-element/](https://leetcode.com/problems/unique-middle-element/)

## Problem

You are given an integer array `nums` of odd length `n`.

Return `true` if the middle element of `nums` appears **exactly** once in the array. Otherwise return `false`.

**Example 1:**

**Input:** nums = [1,2,3]

**Output:** true

**Explanation:**

The middle element of `nums` is 2, which appears exactly once.

Thus, the answer is `true`.

**Example 2:**

**Input:** nums = [1,2,2]

**Output:** false

**Explanation:**

The middle element of `nums` is 2, which appears twice.

Thus, the answer is `false`.

**Constraints:**

- `1 <= n == nums.length <= 100`

	- `n` is odd.

	- `1 <= nums[i] <= 100`

### Hints

1. The middle index is `nums.length / 2`.
2. Count how many times `nums[nums.length / 2]` appears in `nums`.

## Approach

<!-- Describe your solution approach here -->

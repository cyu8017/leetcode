# 3165. Maximum Sum of Subsequence With Non-adjacent Elements

- **Difficulty:** Hard
- **LeetCode:** [https://leetcode.com/problems/maximum-sum-of-subsequence-with-non-adjacent-elements/](https://leetcode.com/problems/maximum-sum-of-subsequence-with-non-adjacent-elements/)
- **Tags:** array, divide-and-conquer, dynamic-programming, segment-tree

## Problem

You are given an array `nums` consisting of integers. You are also given a 2D array `queries`, where `queries[i] = [pos_{i}, x_{i}]`.

For query `i`, we first set `nums[pos_{i}]` equal to `x_{i}`, then we calculate the answer to query `i` which is the **maximum** sum of a subsequence of `nums` where **no two adjacent elements are selected**.

Return the *sum* of the answers to all queries.

Since the final answer may be very large, return it **modulo** `10^{9} + 7`.

A **subsequence** is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

**Example 1:**

**Input:** nums = [3,5,9], queries = [[1,-2],[0,-3]]

**Output:** 21

**Explanation:**

After the 1^{st} query, `nums = [3,-2,9]` and the maximum sum of a subsequence with non-adjacent elements is `3 + 9 = 12`.

After the 2^{nd} query, `nums = [-3,-2,9]` and the maximum sum of a subsequence with non-adjacent elements is 9.

**Example 2:**

**Input:** nums = [0,-1], queries = [[0,-5]]

**Output:** 0

**Explanation:**

After the 1^{st} query, `nums = [-5,-1]` and the maximum sum of a subsequence with non-adjacent elements is 0 (choosing an empty subsequence).

**Constraints:**

- `1 <= nums.length <= 5 * 10^{4}`

	- `-10^{5} <= nums[i] <= 10^{5}`

	- `1 <= queries.length <= 5 * 10^{4}`

	- `queries[i] == [pos_{i}, x_{i}]`

	- `0 <= pos_{i} <= nums.length - 1`

	- `-10^{5} <= x_{i} <= 10^{5}`

### Hints

1. Can you solve each query in `O(nums.length)` with dynamic programming?
2. In order to optimize, we will use segment tree where each node contains the maximum value of (front element has been chosen or not, back element has been chosen or not).

## Approach

<!-- Describe your solution approach here -->

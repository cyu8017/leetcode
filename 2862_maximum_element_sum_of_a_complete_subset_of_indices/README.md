# 2862. Maximum Element-Sum of a Complete Subset of Indices

- **Difficulty:** Hard
- **LeetCode:** [https://leetcode.com/problems/maximum-element-sum-of-a-complete-subset-of-indices/](https://leetcode.com/problems/maximum-element-sum-of-a-complete-subset-of-indices/)
- **Tags:** array, math, number-theory

## Problem

You are given a **1**-indexed** array `nums`. Your task is to select a **complete subset** from `nums` where every pair of selected indices multiplied is a perfect square,. i. e. if you select `a_{i}` and `a_{j}`, `i * j` must be a perfect square.

Return the *sum* of the complete subset with the *maximum sum*.

**Example 1:**

**Input:** nums = [8,7,3,5,7,2,4,9]

**Output:** 16

**Explanation:**

We select elements at indices 2 and 8 and `2 * 8` is a perfect square.

**Example 2:**

**Input:** nums = [8,10,3,8,1,13,7,9,4]

**Output:** 20

**Explanation:**

We select elements at indices 1, 4, and 9. `1 * 4`, `1 * 9`, `4 * 9` are perfect squares.

**Constraints:**

- `1 <= n == nums.length <= 10^{4}`

	- `1 <= nums[i] <= 10^{9}`

### Hints

1. Define **P(x)** as the product of primes **p** with odd exponents in **x**'s factorization. Examples: For `x = 18`, factorization `2^{1} × 3^{2}`, **P(18) = 2**; for `x = 45`, factorization `3^{2} × 5^{1}`, **P(45) = 5**; for `x = 50`, factorization `2^{1} × 5^{2}`, **P(50) = 2**; for `x = 210`, factorization `2^{1} × 3^{1} × 5^{1} × 7^{1}`, **P(210) = 210**.
2. If `P(i) = P(j)`, `nums[i]` and `nums[j]` can be grouped together.
3. Pick the group with the largest sum.

## Approach

<!-- Describe your solution approach here -->

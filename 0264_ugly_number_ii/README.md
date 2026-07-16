# 0264. Ugly Number II

- **Difficulty:** Medium
- **LeetCode:** [https://leetcode.com/problems/ugly-number-ii/](https://leetcode.com/problems/ugly-number-ii/)
- **Tags:** hash-table, math, dynamic-programming, heap-(priority-queue)

## Problem

An **ugly number** is a positive integer whose prime factors are limited to `2`, `3`, and `5`.

Given an integer `n`, return *the* `n^{th}` **ugly number**.

**Example 1:**

```
**Input:** n = 10
**Output:** 12
**Explanation:** [1, 2, 3, 4, 5, 6, 8, 9, 10, 12] is the sequence of the first 10 ugly numbers.
```

**Example 2:**

```
**Input:** n = 1
**Output:** 1
**Explanation:** 1 has no prime factors, therefore all of its prime factors are limited to 2, 3, and 5.
```

**Constraints:**

- `1 <= n <= 1690`

### Hints

1. The naive approach is to call `isUgly` for every number until you reach the n^{th} one. Most numbers are *not* ugly. Try to focus your effort on generating only the ugly ones.
2. An ugly number must be multiplied by either 2, 3, or 5 from a smaller ugly number.
3. The key is how to maintain the order of the ugly numbers. Try a similar approach of merging from three sorted lists: L_{1}, L_{2}, and L_{3}.
4. Assume you have U_{k}, the k^{th} ugly number. Then U_{k+1} must be Min(L_{1} * 2, L_{2} * 3, L_{3} * 5).

## Approach

<!-- Describe your solution approach here -->

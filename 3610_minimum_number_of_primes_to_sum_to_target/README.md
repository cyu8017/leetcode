# 3610. Minimum Number of Primes to Sum to Target

- **Difficulty:** Medium
- **LeetCode:** [https://leetcode.com/problems/minimum-number-of-primes-to-sum-to-target/](https://leetcode.com/problems/minimum-number-of-primes-to-sum-to-target/)
- **Premium:** Yes
- **Tags:** array, math, dynamic-programming, number-theory

## Problem

You are given two integers `n` and `m`.

You have to select a multiset of **prime numbers** from the **first** `m` prime numbers such that the sum of the selected primes is **exactly** `n`. You may use each prime number **multiple** times.

Return the **minimum** number of prime numbers needed to sum up to `n`, or -1 if it is not possible.



**Example 1:**

**Input:** n = 10, m = 2

**Output:** 4

**Explanation:**

The first 2 primes are [2, 3]. The sum 10 can be formed as 2 + 2 + 3 + 3, requiring 4 primes.

**Example 2:**

**Input:** n = 15, m = 5

**Output:** 3

**Explanation:**

The first 5 primes are [2, 3, 5, 7, 11]. The sum 15 can be formed as 5 + 5 + 5, requiring 3 primes.

**Example 3:**

**Input:** n = 7, m = 6

**Output:** 1

**Explanation:**

The first 6 primes are [2, 3, 5, 7, 11, 13]. The sum 7 can be formed directly by prime 7, requiring only 1 prime.



**Constraints:**

	- `1 <= n <= 1000`

	- `1 <= m <= 1000`

---
_Problem text from the [doocs/leetcode](https://github.com/doocs/leetcode) community mirror (LeetCode Premium)._

### Hints

1. Can we use dynamic programming?
2. Generate the first `m` prime numbers.
3. Let `dp[i]` represent the minimum number of prime numbers that sum up to `i`. Use the generated prime numbers for the transition.

## Approach

<!-- Describe your solution approach here -->

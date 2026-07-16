# 3821. Find Nth Smallest Integer With K One Bits

- **Difficulty:** Hard
- **LeetCode:** [https://leetcode.com/problems/find-nth-smallest-integer-with-k-one-bits/](https://leetcode.com/problems/find-nth-smallest-integer-with-k-one-bits/)
- **Tags:** math, bit-manipulation, combinatorics

## Problem

You are given two positive integers `n` and `k`.

Return an integer denoting the `n^{th}` smallest positive integer that has **exactly** `k` ones in its binary representation. It is guaranteed that the answer is **strictly less** than `2^{50}`.

**Example 1:**

**Input:** n = 4, k = 2

**Output:** 9

**Explanation:**

The 4 smallest positive integers that have exactly `k = 2` ones in their binary representations are:

- `3 = 11_{2}`

	- `5 = 101_{2}`

	- `6 = 110_{2}`

	- `9 = 1001_{2}`

**Example 2:**

**Input:** n = 3, k = 1

**Output:** 4

**Explanation:**

The 3 smallest positive integers that have exactly `k = 1` one in their binary representations are:

- `1 = 1_{2}`

	- `2 = 10_{2}`

	- `4 = 100_{2}`

**Constraints:**

- `1 <= n <= 2^{50}`

	- `1 <= k <= 50`

	- The answer is strictly less than `2^{50}`.

### Hints

1. Since the answer is strictly less than `2^{50}`, we can iterate over the number of bits (the length) of the result.
2. Precompute binomial coefficients `C(n, k)` to count how many numbers with exactly `k` set bits exist for a given length.
3. Determine the position of the most significant bit first, then greedily determine the remaining bits from MSB to LSB based on the remaining count `n`.

## Approach

<!-- Describe your solution approach here -->

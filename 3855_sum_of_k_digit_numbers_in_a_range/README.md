# 3855. Sum of K-Digit Numbers in a Range

- **Difficulty:** Hard
- **LeetCode:** [https://leetcode.com/problems/sum-of-k-digit-numbers-in-a-range/](https://leetcode.com/problems/sum-of-k-digit-numbers-in-a-range/)
- **Tags:** math, divide-and-conquer, combinatorics, number-theory

## Problem

You are given three integers `l`, `r`, and `k`.

Consider all possible integers consisting of **exactly** `k` digits, where each digit is chosen independently from the integer range `[l, r]` (inclusive). If 0 is included in the range, leading zeros are allowed.

Return an integer representing the **sum of all such numbers.**​​​​​​​ Since the answer may be very large, return it **modulo** `10^{9} + 7`.

**Example 1:**

**Input:** l = 1, r = 2, k = 2

**Output:** 66

**Explanation:**

- All numbers formed using `k = 2` digits in the range `[1, 2]` are `11, 12, 21, 22`.

	- The total sum is `11 + 12 + 21 + 22 = 66`.

**Example 2:**

**Input:** l = 0, r = 1, k = 3

**Output:** 444

**Explanation:**

- All numbers formed using `k = 3` digits in the range `[0, 1]` are `000, 001, 010, 011, 100, 101, 110, 111`​​​​​​​.

	- These numbers without leading zeros are `0, 1, 10, 11, 100, 101, 110, 111`.

	- The total sum is 444.

**Example 3:**

**Input:** l = 5, r = 5, k = 10

**Output:** 555555520

**Explanation:**​​​​​​​

- 5555555555 is the only valid number consisting of `k = 10` digits in the range `[5, 5]`.

	- The total sum is `5555555555 % (10^{9} + 7) = 555555520`.

**Constraints:**

- `0 <= l <= r <= 9`

	- `1 <= k <= 10^{9}`

### Hints

1. Use combinatorics.
2. For some position `p` among the `k` digits, the sum is `10^p * (l + (l+1) + ... + r) * (r - l + 1)^(k-1)`.
3. Summing `p` over `[0, k-1]` gives `(l + (l+1) + ... + r) * (r - l + 1)^(k-1) * (10^k - 1) / 9`.

## Approach

<!-- Describe your solution approach here -->

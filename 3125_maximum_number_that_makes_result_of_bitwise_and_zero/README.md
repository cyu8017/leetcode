# 3125. Maximum Number That Makes Result of Bitwise AND Zero

- **Difficulty:** Medium
- **LeetCode:** [https://leetcode.com/problems/maximum-number-that-makes-result-of-bitwise-and-zero/](https://leetcode.com/problems/maximum-number-that-makes-result-of-bitwise-and-zero/)
- **Premium:** Yes
- **Tags:** string, greedy, sorting

## Problem

Given an integer `n`, return the **maximum** integer `x` such that `x <= n`, and the bitwise `AND` of all the numbers in the range `[x, n]` is 0.



**Example 1:**

**Input:** n = 7

**Output:** 3

**Explanation:**

The bitwise `AND` of `[6, 7]` is 6.

The bitwise `AND` of `[5, 6, 7]` is 4.

The bitwise `AND` of `[4, 5, 6, 7]` is 4.

The bitwise `AND` of `[3, 4, 5, 6, 7]` is 0.

**Example 2:**

**Input:** n = 9

**Output:** 7

**Explanation:**

The bitwise `AND` of `[7, 8, 9]` is 0.

**Example 3:**

**Input:** n = 17

**Output:** 15

**Explanation:**

The bitwise `AND` of `[15, 16, 17]` is 0.



**Constraints:**

	- `1 <= n <= 10^{15}`

---
_Problem text from the [doocs/leetcode](https://github.com/doocs/leetcode) community mirror (LeetCode Premium)._

### Hints

1. Examine the set bits of `n`.
2. When performing bitwise AND operations sequentially down from `n`, the last set bit to turn to 0 identifies the highest set bit.
3. If the index of the highest set bit is `x`, the answer is `2^{x} - 1`.

## Approach

<!-- Describe your solution approach here -->

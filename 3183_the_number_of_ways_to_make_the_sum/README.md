# 3183. The Number of Ways to Make the Sum

- **Difficulty:** Medium
- **LeetCode:** [https://leetcode.com/problems/the-number-of-ways-to-make-the-sum/](https://leetcode.com/problems/the-number-of-ways-to-make-the-sum/)
- **Premium:** Yes
- **Tags:** array, dynamic-programming

## Problem

You have an **infinite** number of coins with values 1, 2, and 6, and **only** 2 coins with value 4.

Given an integer `n`, return the number of ways to make the sum of `n` with the coins you have.

Since the answer may be very large, return it **modulo** `10^{9} + 7`.

**Note** that the order of the coins doesn't matter and `[2, 2, 3]` is the same as `[2, 3, 2]`.



**Example 1:**

**Input:** n = 4

**Output:** 4

**Explanation:**

Here are the four combinations: `[1, 1, 1, 1]`, `[1, 1, 2]`, `[2, 2]`, `[4]`.

**Example 2:**

**Input:** n = 12

**Output:** 22

**Explanation:**

Note that `[4, 4, 4]` is **not** a valid combination since we cannot use 4 three times.

**Example 3:**

**Input:** n = 5

**Output:** 4

**Explanation:**

Here are the four combinations: `[1, 1, 1, 1, 1]`, `[1, 1, 1, 2]`, `[1, 2, 2]`, `[1, 4]`.



**Constraints:**

	- `1 <= n <= 10^{5}`

---
_Problem text from the [doocs/leetcode](https://github.com/doocs/leetcode) community mirror (LeetCode Premium)._

### Hints

1. Consider using dynamic programming.
2. Define `dp[i][x]` as the number of ways to make the sum `x` using only the first `i` coins; and define `coin[i]` as the value of coin `i`.
3. We can calculate `dp[i][x]` as the sum of `dp[i - 1][x]` and `dp[i][x - coin[i]]`.
4. Remember that 4 can at most be multiplied twice, so we calculate the `dp` for our infinite coins and then manually handle the existence of 4.

## Approach

<!-- Describe your solution approach here -->

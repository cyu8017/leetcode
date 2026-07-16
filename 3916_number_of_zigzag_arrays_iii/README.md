# 3916. Number of ZigZag Arrays III

- **Difficulty:** Hard
- **LeetCode:** [https://leetcode.com/problems/number-of-zigzag-arrays-iii/](https://leetcode.com/problems/number-of-zigzag-arrays-iii/)
- **Premium:** Yes
- **Tags:** math, dynamic-programming, prefix-sum

## Problem

You are given three integers `n`, `l`, and `r`.

A **ZigZag** array of length `n` is defined as follows:

	- Each element lies in the range `[l, r]`.

	- No **two** adjacent elements are equal.

	- No **three** consecutive elements form a **strictly increasing** or **strictly decreasing** sequence.

Return the total number of valid **ZigZag** arrays.

Since the answer may be large, return it **modulo** `10^{9} + 7`.



**Example 1:**

**Input:** n = 3, l = 4, r = 5

**Output:** 2

**Explanation:**

There are only 2 valid ZigZag arrays of length `n = 3` using values in the range `[4, 5]`:

	- `[4, 5, 4]`

	- `[5, 4, 5]`

**Example 2:**

**Input:** n = 3, l = 1, r = 3

**Output:** 10

**Explanation:**

There are 10 valid ZigZag arrays of length `n = 3` using values in the range `[1, 3]`:

	- `[1, 2, 1]`, `[1, 3, 1]`, `[1, 3, 2]`

	- `[2, 1, 2]`, `[2, 1, 3]`, `[2, 3, 1]`, `[2, 3, 2]`

	- `[3, 1, 2]`, `[3, 1, 3]`, `[3, 2, 3]`

All arrays meet the ZigZag conditions.



**Constraints:**

	- `3 <= n <= 200`

	- `1 <= l < r <= 10^{​​​​​​​9}`

---
_Problem text from the [doocs/leetcode](https://github.com/doocs/leetcode) community mirror (LeetCode Premium)._

### Hints

1. Let `m = r - l + 1`. The actual values do not matter, only how many distinct choices you have.
2. The answer as a function of `m` is a polynomial of degree at most `n`. So instead of working up to large `m`, compute values for small `m`.
3. Use Dynamic Programming: `dp[i][j][dir]` = number of arrays of length `i` ending at value `j` with last move direction `dir` (`up`/`down`). Use prefix sums to transition in `O(n^2)` total for all `m <= n+1`.
4. After computing answers for `m = 1, 2, ..., n+1`, use Lagrange interpolation to evaluate the polynomial at the actual `m` in `O(n)` or `O(n^2)` time.

## Approach

<!-- Describe your solution approach here -->

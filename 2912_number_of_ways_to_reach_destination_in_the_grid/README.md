# 2912. Number of Ways to Reach Destination in the Grid

- **Difficulty:** Hard
- **LeetCode:** [https://leetcode.com/problems/number-of-ways-to-reach-destination-in-the-grid/](https://leetcode.com/problems/number-of-ways-to-reach-destination-in-the-grid/)
- **Premium:** Yes
- **Tags:** math, dynamic-programming, combinatorics

## Problem

You are given two integers `n` and `m` which represent the size of a **1-indexed **grid. You are also given an integer `k`, a **1-indexed** integer array `source` and a **1-indexed** integer array `dest`, where `source` and `dest` are in the form `[x, y]` representing a cell on the given grid.

You can move through the grid in the following way:

	- You can go from cell `[x_{1}, y_{1}]` to cell `[x_{2}, y_{2}]` if either `x_{1} == x_{2}` or `y_{1} == y_{2}`.

	- Note that you **can't** move to the cell you are already in e.g. `x_{1} == x_{2}` and `y_{1} == y_{2}`.

Return *the number of ways you can reach* `dest` *from* `source` *by moving through the grid* **exactly** `k` *times.*

Since the answer may be very large, return it **modulo** `10^{9} + 7`.



**Example 1:**

**Input:** n = 3, m = 2, k = 2, source = [1,1], dest = [2,2]
**Output:** 2
**Explanation:** There are 2 possible sequences of reaching [2,2] from [1,1]:
- [1,1] -> [1,2] -> [2,2]
- [1,1] -> [2,1] -> [2,2]

**Example 2:**

**Input:** n = 3, m = 4, k = 3, source = [1,2], dest = [2,3]
**Output:** 9
**Explanation:** There are 9 possible sequences of reaching [2,3] from [1,2]:
- [1,2] -> [1,1] -> [1,3] -> [2,3]
- [1,2] -> [1,1] -> [2,1] -> [2,3]
- [1,2] -> [1,3] -> [3,3] -> [2,3]
- [1,2] -> [1,4] -> [1,3] -> [2,3]
- [1,2] -> [1,4] -> [2,4] -> [2,3]
- [1,2] -> [2,2] -> [2,1] -> [2,3]
- [1,2] -> [2,2] -> [2,4] -> [2,3]
- [1,2] -> [3,2] -> [2,2] -> [2,3]
- [1,2] -> [3,2] -> [3,3] -> [2,3]



**Constraints:**

	- `2 <= n, m <= 10^{9}`

	- `1 <= k <= 10^{5}`

	- `source.length == dest.length == 2`

	- `1 <= source[1], dest[1] <= n`

	- `1 <= source[2], dest[2] <= m`

---
_Problem text from the [doocs/leetcode](https://github.com/doocs/leetcode) community mirror (LeetCode Premium)._

### Hints

1. We are asked to count the number of sequences of length `k + 1` that start from `(x_{s}, y_{s})` and end with `(x_{d}, y_{d})`. i.e., `(x_{s}, y_{s}), (x_{1}, y_{1}), ..., (x_{k - 1}, y_{k - 1}), (x_{d}, y_{d})`.
2. The key point is to see `x` and `y` separately.
3. Suppose we do `i` vertical moves and `k - i` horizontal moves.
4. In each vertical move, we change only `y`. Now let's count the number of sequences of length `i + 1` that start with `source[2]` and end with `dest[2]`. Let's call this number `vertical_count`.
5. Do the same for horizontal moves and let it be `horizontal_count`.
6. For each `i`, the number of ways would be `vertical_count * horizontal_count * C(n, i)` since the order of vertical and horizontal moves could be arbitrary.

## Approach

<!-- Describe your solution approach here -->

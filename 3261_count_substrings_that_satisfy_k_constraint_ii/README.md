# 3261. Count Substrings That Satisfy K-Constraint II

- **Difficulty:** Hard
- **LeetCode:** [https://leetcode.com/problems/count-substrings-that-satisfy-k-constraint-ii/](https://leetcode.com/problems/count-substrings-that-satisfy-k-constraint-ii/)
- **Tags:** array, string, binary-search, sliding-window, prefix-sum

## Problem

You are given a **binary** string `s` and an integer `k`.

You are also given a 2D integer array `queries`, where `queries[i] = [l_{i}, r_{i}]`.

A **binary string** satisfies the **k-constraint** if **either** of the following conditions holds:

- The number of `0`'s in the string is at most `k`.

	- The number of `1`'s in the string is at most `k`.

Return an integer array `answer`, where `answer[i]` is the number of substrings of `s[l_{i}..r_{i}]` that satisfy the **k-constraint**.

**Example 1:**

**Input:** s = "0001111", k = 2, queries = [[0,6]]

**Output:** [26]

**Explanation:**

For the query `[0, 6]`, all substrings of `s[0..6] = "0001111"` satisfy the k-constraint except for the substrings `s[0..5] = "000111"` and `s[0..6] = "0001111"`.

**Example 2:**

**Input:** s = "010101", k = 1, queries = [[0,5],[1,4],[2,3]]

**Output:** [15,9,3]

**Explanation:**

The substrings of `s` with a length greater than 3 do not satisfy the k-constraint.

**Constraints:**

- `1 <= s.length <= 10^{5}`

	- `s[i]` is either `'0'` or `'1'`.

	- `1 <= k <= s.length`

	- `1 <= queries.length <= 10^{5}`

	- `queries[i] == [l_{i}, r_{i}]`

	- `0 <= l_{i} <= r_{i} < s.length`

	- All queries are distinct.

### Hints

1. Answering online queries is tough. Try to answer them offline since the queries are known beforehand.
2. For each index, how do you calculate the left boundary so that the given condition is satisfied?
3. Using the precomputed left boundaries and a range data structure, you can now answer the queries optimally.

## Approach

<!-- Describe your solution approach here -->

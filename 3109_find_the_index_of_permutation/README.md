# 3109. Find the Index of Permutation

- **Difficulty:** Medium
- **LeetCode:** [https://leetcode.com/problems/find-the-index-of-permutation/](https://leetcode.com/problems/find-the-index-of-permutation/)
- **Premium:** Yes
- **Tags:** array, binary-search, divide-and-conquer, binary-indexed-tree, segment-tree, merge-sort, ordered-set

## Problem

Given an array `perm` of length `n` which is a permutation of `[1, 2, ..., n]`, return the index of `perm` in the lexicographically sorted array of all of the permutations of `[1, 2, ..., n]`.

Since the answer may be very large, return it **modulo** `10^{9} + 7`.



**Example 1:**

**Input:** perm = [1,2]

**Output:** 0

**Explanation:**

There are only two permutations in the following order:

`[1,2]`, `[2,1]`

And `[1,2]` is at index 0.

**Example 2:**

**Input:** perm = [3,1,2]

**Output:** 4

**Explanation:**

There are only six permutations in the following order:

`[1,2,3]`, `[1,3,2]`, `[2,1,3]`, `[2,3,1]`, `[3,1,2]`, `[3,2,1]`

And `[3,1,2]` is at index 4.



**Constraints:**

	- `1 <= n == perm.length <= 10^{5}`

	- `perm` is a permutation of `[1, 2, ..., n]`.

---
_Problem text from the [doocs/leetcode](https://github.com/doocs/leetcode) community mirror (LeetCode Premium)._

### Hints

1. If `perm[0]` is `x`, there are at least `(x - 1) * (n - 1)!` permutations before `perm. (All the ones starting with numbers less than x`)
2. Can you find out what happens for `perm[1]` onwards?
3. Think about the count of the numbers that can be in place of `perm[i]` and come before it.

## Approach

<!-- Describe your solution approach here -->

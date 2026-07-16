# 0267. Palindrome Permutation II

- **Difficulty:** Medium
- **LeetCode:** [https://leetcode.com/problems/palindrome-permutation-ii/](https://leetcode.com/problems/palindrome-permutation-ii/)
- **Premium:** Yes
- **Tags:** hash-table, string, backtracking

## Problem

Given a string s, return *all the palindromic permutations (without duplicates) of it*.

You may return the answer in **any order**. If `s` has no palindromic permutation, return an empty list.



**Example 1:**

**Input:** s = "aabb"
**Output:** ["abba","baab"]

**Example 2:**

**Input:** s = "abc"
**Output:** []



**Constraints:**

	- `1 <= s.length <= 16`

	- `s` consists of only lowercase English letters.

---
_Problem text from the [doocs/leetcode](https://github.com/doocs/leetcode) community mirror (LeetCode Premium)._

### Hints

1. If a palindromic permutation exists, we just need to generate the first half of the string.
2. To generate all distinct permutations of a (half of) string, use a similar approach from: [Permutations II](/problems/permutations-ii) or [Next Permutation](/problems/next-permutation).

## Approach

<!-- Describe your solution approach here -->

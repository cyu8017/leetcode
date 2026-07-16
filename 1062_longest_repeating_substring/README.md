# 1062. Longest Repeating Substring

- **Difficulty:** Medium
- **LeetCode:** [https://leetcode.com/problems/longest-repeating-substring/](https://leetcode.com/problems/longest-repeating-substring/)
- **Premium:** Yes
- **Tags:** string, binary-search, dynamic-programming, rolling-hash, suffix-array, hash-function

## Problem

Given a string `s`, return *the length of the longest repeating substrings*. If no repeating substring exists, return `0`.



**Example 1:**

**Input:** s = "abcd"
**Output:** 0
**Explanation: **There is no repeating substring.

**Example 2:**

**Input:** s = "abbaba"
**Output:** 2
**Explanation: **The longest repeating substrings are "ab" and "ba", each of which occurs twice.

**Example 3:**

**Input:** s = "aabcaabdaab"
**Output:** 3
**Explanation: **The longest repeating substring is "aab", which occurs `3` times.



**Constraints:**

	- `1 <= s.length <= 2000`

	- `s` consists of lowercase English letters.

---
_Problem text from the [doocs/leetcode](https://github.com/doocs/leetcode) community mirror (LeetCode Premium)._

### Hints

1. Generate all substrings in O(N^2) time with hashing.
2. Choose those hashing of strings with the largest length.

## Approach

<!-- Describe your solution approach here -->

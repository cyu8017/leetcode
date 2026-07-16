# 1554. Strings Differ by One Character

- **Difficulty:** Medium
- **LeetCode:** [https://leetcode.com/problems/strings-differ-by-one-character/](https://leetcode.com/problems/strings-differ-by-one-character/)
- **Premium:** Yes
- **Tags:** hash-table, string, rolling-hash, hash-function

## Problem

Given a list of strings `dict` where all the strings are of the same length.

Return `true` if there are 2 strings that only differ by 1 character in the same index, otherwise return `false`.



**Example 1:**

**Input:** dict = ["abcd","acbd", "aacd"]
**Output:** true
**Explanation:** Strings "a**b**cd" and "a**a**cd" differ only by one character in the index 1.

**Example 2:**

**Input:** dict = ["ab","cd","yz"]
**Output:** false

**Example 3:**

**Input:** dict = ["abcd","cccc","abyd","abab"]
**Output:** true



**Constraints:**

	- The number of characters in `dict <= 10^{5}`

	- `dict[i].length == dict[j].length`

	- `dict[i]` should be unique.

	- `dict[i]` contains only lowercase English letters.

---
_Problem text from the [doocs/leetcode](https://github.com/doocs/leetcode) community mirror (LeetCode Premium)._

### Hints

1. BruteForce, check all pairs and verify if they differ in one character. O(n^2 * m) where n is the number of words and m is the length of each string.
2. O(m^2 * n), Use hashset, to insert all possible combinations adding a character "*". For example: If dict[i] = "abc", insert ("*bc", "a*c" and "ab*").

## Approach

<!-- Describe your solution approach here -->

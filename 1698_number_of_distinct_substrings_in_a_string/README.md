# 1698. Number of Distinct Substrings in a String

- **Difficulty:** Medium
- **LeetCode:** [https://leetcode.com/problems/number-of-distinct-substrings-in-a-string/](https://leetcode.com/problems/number-of-distinct-substrings-in-a-string/)
- **Premium:** Yes
- **Tags:** string, trie, rolling-hash, suffix-array, hash-function

## Problem

Given a string `s`, return *the number of **distinct** substrings of* `s`.

A **substring** of a string is obtained by deleting any number of characters (possibly zero) from the front of the string and any number (possibly zero) from the back of the string.



**Example 1:**

**Input:** s = "aabbaba"
**Output:** 21
**Explanation:** The set of distinct strings is ["a","b","aa","bb","ab","ba","aab","abb","bab","bba","aba","aabb","abba","bbab","baba","aabba","abbab","bbaba","aabbab","abbaba","aabbaba"]

**Example 2:**

**Input:** s = "abcdefg"
**Output:** 28



**Constraints:**

	- `1 <= s.length <= 500`

	- `s` consists of lowercase English letters.



**Follow up:** Can you solve this problem in `O(n)` time complexity?

---
_Problem text from the [doocs/leetcode](https://github.com/doocs/leetcode) community mirror (LeetCode Premium)._

### Hints

1. Calculate the prefix hashing array for s.
2. Use the prefix hashing array to calculate the hashing value of each substring.
3. Compare the hashing values to determine the unique substrings.
4. There could be collisions if you use hashing, what about double hashing.

## Approach

<!-- Describe your solution approach here -->

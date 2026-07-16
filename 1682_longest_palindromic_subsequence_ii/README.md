# 1682. Longest Palindromic Subsequence II

- **Difficulty:** Medium
- **LeetCode:** [https://leetcode.com/problems/longest-palindromic-subsequence-ii/](https://leetcode.com/problems/longest-palindromic-subsequence-ii/)
- **Premium:** Yes
- **Tags:** string, dynamic-programming

## Problem

A subsequence of a string `s` is considered a **good palindromic subsequence** if:

	- It is a subsequence of `s`.

	- It is a palindrome (has the same value if reversed).

	- It has an **even** length.

	- No two consecutive characters are equal, except the two middle ones.

For example, if `s = "abcabcabb"`, then `"abba"` is considered a **good palindromic subsequence**, while `"bcb"` (not even length) and `"bbbb"` (has equal consecutive characters) are not.

Given a string `s`, return *the **length** of the **longest good palindromic subsequence** in *`s`.



**Example 1:**

**Input:** s = "bbabab"
**Output:** 4
**Explanation:** The longest good palindromic subsequence of s is "baab".

**Example 2:**

**Input:** s = "dcbccacdb"
**Output:** 4
**Explanation:** The longest good palindromic subsequence of s is "dccd".



**Constraints:**

	- `1 <= s.length <= 250`

	- `s` consists of lowercase English letters.

---
_Problem text from the [doocs/leetcode](https://github.com/doocs/leetcode) community mirror (LeetCode Premium)._

### Hints

1. As with any good dp problem that uses palindromes, try building the palindrome from the edges
2. The prime point is to check that no two adjacent characters are equal, so save the past character while building the palindrome.

## Approach

<!-- Describe your solution approach here -->

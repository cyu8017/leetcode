# 1055. Shortest Way to Form String

- **Difficulty:** Medium
- **LeetCode:** [https://leetcode.com/problems/shortest-way-to-form-string/](https://leetcode.com/problems/shortest-way-to-form-string/)
- **Premium:** Yes
- **Tags:** two-pointers, string, binary-search, greedy

## Problem

A **subsequence** of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., `"ace"` is a subsequence of `"abcde"` while `"aec"` is not).

Given two strings `source` and `target`, return *the minimum number of **subsequences** of *`source`* such that their concatenation equals *`target`. If the task is impossible, return `-1`.



**Example 1:**

**Input:** source = "abc", target = "abcbc"
**Output:** 2
**Explanation:** The target "abcbc" can be formed by "abc" and "bc", which are subsequences of source "abc".

**Example 2:**

**Input:** source = "abc", target = "acdbc"
**Output:** -1
**Explanation:** The target string cannot be constructed from the subsequences of source string due to the character "d" in target string.

**Example 3:**

**Input:** source = "xyz", target = "xzyxz"
**Output:** 3
**Explanation:** The target string can be constructed as follows "xz" + "y" + "xz".



**Constraints:**

	- `1 <= source.length, target.length <= 1000`

	- `source` and `target` consist of lowercase English letters.

---
_Problem text from the [doocs/leetcode](https://github.com/doocs/leetcode) community mirror (LeetCode Premium)._

### Hints

1. Which conditions have to been met in order to be impossible to form the target string?
2. If there exists a character in the target string which doesn't exist in the source string then it will be impossible to form the target string.
3. Assuming we are in the case which is possible to form the target string, how can we assure the minimum number of used subsequences of source?
4. For each used subsequence try to match the leftmost character of the current subsequence with the leftmost character of the target string, if they match then erase both character otherwise erase just the subsequence character whenever the current subsequence gets empty, reset it to a new copy of subsequence and increment the count, do this until the target sequence gets empty. Finally return the count.

## Approach

<!-- Describe your solution approach here -->

# 1794. Count Pairs of Equal Substrings With Minimum Difference

- **Difficulty:** Medium
- **LeetCode:** [https://leetcode.com/problems/count-pairs-of-equal-substrings-with-minimum-difference/](https://leetcode.com/problems/count-pairs-of-equal-substrings-with-minimum-difference/)
- **Premium:** Yes
- **Tags:** hash-table, string, greedy

## Problem

You are given two strings `firstString` and `secondString` that are **0-indexed** and consist only of lowercase English letters. Count the number of index quadruples `(i,j,a,b)` that satisfy the following conditions:

	- `0 <= i <= j < firstString.length`

	- `0 <= a <= b < secondString.length`

	- The substring of `firstString` that starts at the `i^{th}` character and ends at the `j^{th}` character (inclusive) is **equal** to the substring of `secondString` that starts at the `a^{th}` character and ends at the `b^{th}` character (inclusive).

	- `j - a` is the **minimum** possible value among all quadruples that satisfy the previous conditions.

Return *the **number** of such quadruples*.



**Example 1:**

**Input:** firstString = "abcd", secondString = "bccda"
**Output:** 1
**Explanation:** The quadruple (0,0,4,4) is the only one that satisfies all the conditions and minimizes j - a.

**Example 2:**

**Input:** firstString = "ab", secondString = "cd"
**Output:** 0
**Explanation:** There are no quadruples satisfying all the conditions.



**Constraints:**

	- `1 <= firstString.length, secondString.length <= 2 * 10^{5}`

	- Both strings consist only of lowercase English letters.

---
_Problem text from the [doocs/leetcode](https://github.com/doocs/leetcode) community mirror (LeetCode Premium)._

### Hints

1. If the chosen substrings are of size larger than 1, then you can remove all but the first character from both substrings, and you'll get equal substrings of size 1, with the same a but less j. Hence, it's always optimal to choose substrings of size 1.
2. If you choose a specific letter, then it's optimal to choose its first occurrence in firstString, and its last occurrence in secondString, to minimize j-a.

## Approach

<!-- Describe your solution approach here -->

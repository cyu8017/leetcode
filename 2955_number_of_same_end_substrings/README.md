# 2955. Number of Same-End Substrings

- **Difficulty:** Medium
- **LeetCode:** [https://leetcode.com/problems/number-of-same-end-substrings/](https://leetcode.com/problems/number-of-same-end-substrings/)
- **Premium:** Yes
- **Tags:** array, hash-table, string, counting, prefix-sum

## Problem

You are given a **0-indexed** string `s`, and a 2D array of integers `queries`, where `queries[i] = [l_{i}, r_{i}]` indicates a substring of `s` starting from the index `l_{i}` and ending at the index `r_{i}` (both **inclusive**), i.e. `s[l_{i}..r_{i}]`.

Return *an array *`ans`* where* `ans[i]` *is the number of **same-end** substrings of* `queries[i]`.

A **0-indexed** string `t` of length `n` is called **same-end** if it has the same character at both of its ends, i.e., `t[0] == t[n - 1]`.

A **substring** is a contiguous non-empty sequence of characters within a string.



**Example 1:**

**Input:** s = "abcaab", queries = [[0,0],[1,4],[2,5],[0,5]]
**Output:** [1,5,5,10]
**Explanation:** Here is the same-end substrings of each query:
1^{st} query: s[0..0] is "a" which has 1 same-end substring: "**a**".
2^{nd} query: s[1..4] is "bcaa" which has 5 same-end substrings: "**b**caa", "b**c**aa", "bc**a**a", "bca**a**", "bc**aa**".
3^{rd} query: s[2..5] is "caab" which has 5 same-end substrings: "**c**aab", "c**a**ab", "ca**a**b", "caa**b**", "c**aa**b".
4^{th} query: s[0..5] is "abcaab" which has 10 same-end substrings: "**a**bcaab", "a**b**caab", "ab**c**aab", "abc**a**ab", "abca**a**b", "abcaa**b**", "abc**aa**b", "**abca**ab", "**abcaa**b", "a**bcaab**".

**Example 2:**

**Input:** s = "abcd", queries = [[0,3]]
**Output:** [4]
**Explanation:** The only query is s[0..3] which is "abcd". It has 4 same-end substrings: "**a**bcd", "a**b**cd", "ab**c**d", "abc**d**".



**Constraints:**

	- `2 <= s.length <= 3 * 10^{4}`

	- `s` consists only of lowercase English letters.

	- `1 <= queries.length <= 3 * 10^{4}`

	- `queries[i] = [l_{i}, r_{i}]`

	- `0 <= l_{i} <= r_{i} < s.length`

---
_Problem text from the [doocs/leetcode](https://github.com/doocs/leetcode) community mirror (LeetCode Premium)._

### Hints

1. If there are `t` occurrences of a character in a substring, there exists `t * (t + 1) / 2` Same-End substrings with that character.
2. Try to calculate the number of occurrences of a character in a substring in `O(1)` using partial sum.

## Approach

<!-- Describe your solution approach here -->

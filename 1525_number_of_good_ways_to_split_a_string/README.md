# 1525. Number of Good Ways to Split a String

- **Difficulty:** Medium
- **LeetCode:** [https://leetcode.com/problems/number-of-good-ways-to-split-a-string/](https://leetcode.com/problems/number-of-good-ways-to-split-a-string/)
- **Tags:** hash-table, string, dynamic-programming, bit-manipulation, prefix-sum

## Problem

You are given a string `s`.

A split is called **good** if you can split `s` into two non-empty strings `s_{left}` and `s_{right}` where their concatenation is equal to `s` (i.e., `s_{left} + s_{right} = s`) and the number of distinct letters in `s_{left}` and `s_{right}` is the same.

Return *the number of **good splits** you can make in `s`*.

**Example 1:**

```
**Input:** s = "aacaba"
**Output:** 2
**Explanation:** There are 5 ways to split "aacaba" and 2 of them are good.
("a", "acaba") Left string and right string contains 1 and 3 different letters respectively.
("aa", "caba") Left string and right string contains 1 and 3 different letters respectively.
("aac", "aba") Left string and right string contains 2 and 2 different letters respectively (good split).
("aaca", "ba") Left string and right string contains 2 and 2 different letters respectively (good split).
("aacab", "a") Left string and right string contains 3 and 1 different letters respectively.
```

**Example 2:**

```
**Input:** s = "abcd"
**Output:** 1
**Explanation:** Split the string as follows ("ab", "cd").
```

**Constraints:**

- `1 <= s.length <= 10^{5}`

	- `s` consists of only lowercase English letters.

### Hints

1. Use two HashMap to store the counts of distinct letters in the left and right substring divided by the current index.

## Approach

<!-- Describe your solution approach here -->

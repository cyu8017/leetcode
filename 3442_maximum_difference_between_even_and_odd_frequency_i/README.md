# 3442. Maximum Difference Between Even and Odd Frequency I

- **Difficulty:** Easy
- **LeetCode:** [https://leetcode.com/problems/maximum-difference-between-even-and-odd-frequency-i/](https://leetcode.com/problems/maximum-difference-between-even-and-odd-frequency-i/)
- **Tags:** hash-table, string, counting

## Problem

You are given a string `s` consisting of lowercase English letters.

Your task is to find the **maximum** difference `diff = freq(a_{1}) - freq(a_{2})` between the frequency of characters `a_{1}` and `a_{2}` in the string such that:

- `a_{1}` has an **odd frequency** in the string.

	- `a_{2}` has an **even frequency** in the string.

Return this **maximum** difference.

**Example 1:**

**Input:** s = "aaaaabbc"

**Output:** 3

**Explanation:**

- The character `'a'` has an **odd frequency** of `5`, and `'b'` has an **even frequency** of `2`.

	- The maximum difference is `5 - 2 = 3`.

**Example 2:**

**Input:** s = "abcabcab"

**Output:** 1

**Explanation:**

- The character `'a'` has an **odd frequency** of `3`, and `'c'` has an **even frequency** of 2.

	- The maximum difference is `3 - 2 = 1`.

**Constraints:**

- `3 <= s.length <= 100`

	- `s` consists only of lowercase English letters.

	- `s` contains at least one character with an odd frequency and one with an even frequency.

### Hints

1. Use a frequency map to identify the maximum odd and minimum even frequencies. Then, calculate their difference.

## Approach

<!-- Describe your solution approach here -->

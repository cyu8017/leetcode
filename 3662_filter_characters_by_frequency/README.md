# 3662. Filter Characters by Frequency

- **Difficulty:** Easy
- **LeetCode:** [https://leetcode.com/problems/filter-characters-by-frequency/](https://leetcode.com/problems/filter-characters-by-frequency/)
- **Premium:** Yes
- **Tags:** hash-table, string, counting

## Problem

You are given a string `s` consisting of lowercase English letters and an integer `k`.

Your task is to construct a new string that contains only those characters from `s` which appear **fewer** than `k` times in the entire string. The order of characters in the new string must be the **same** as their **order** in `s`.

Return the resulting string. If no characters qualify, return an empty string.

Note: **Every occurrence** of a character that occurs fewer than `k` times is kept.



**Example 1:**

**Input:** s = "aadbbcccca", k = 3

**Output:** "dbb"

**Explanation:**

Character frequencies in `s`:

	- `'a'` appears 3 times

	- `'d'` appears 1 time

	- `'b'` appears 2 times

	- `'c'` appears 4 times

Only `'d'` and `'b'` appear fewer than 3 times. Preserving their order, the result is `"dbb"`.

**Example 2:**

**Input:** s = "xyz", k = 2

**Output:** "xyz"

**Explanation:**

All characters (`'x'`, `'y'`, `'z'`) appear exactly once, which is fewer than 2. Thus the whole string is returned.



**Constraints:**

	- `1 <= s.length <= 100`

	- `s` consists of lowercase English letters.

	- `1 <= k <= s.length`

---
_Problem text from the [doocs/leetcode](https://github.com/doocs/leetcode) community mirror (LeetCode Premium)._

### Hints

1. Count the frequency of each character using a 26-entry array or a frequency map, then iterate through the string and append each character whose frequency is less than `k` to the result.

## Approach

<!-- Describe your solution approach here -->

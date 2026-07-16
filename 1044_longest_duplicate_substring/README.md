# 1044. Longest Duplicate Substring

- **Difficulty:** Hard
- **LeetCode:** [https://leetcode.com/problems/longest-duplicate-substring/](https://leetcode.com/problems/longest-duplicate-substring/)
- **Tags:** string, binary-search, sliding-window, rolling-hash, suffix-array, hash-function

## Problem

Given a string `s`, consider all *duplicated substrings*: (contiguous) substrings of s that occur 2 or more times. The occurrences may overlap.

Return **any** duplicated substring that has the longest possible length. If `s` does not have a duplicated substring, the answer is `""`.

**Example 1:**

```
**Input:** s = "banana"
**Output:** "ana"
```

**Example 2:**

```
**Input:** s = "abcd"
**Output:** ""
```

**Constraints:**

- `2 <= s.length <= 3 * 10^{4}`

	- `s` consists of lowercase English letters.

### Hints

1. Binary search for the length of the answer.  (If there's an answer of length 10, then there are answers of length 9, 8, 7, ...)
2. To check whether an answer of length K exists, we can use Rabin-Karp 's algorithm.

## Approach

<!-- Describe your solution approach here -->

# 1400. Construct K Palindrome Strings

- **Difficulty:** Medium
- **LeetCode:** [https://leetcode.com/problems/construct-k-palindrome-strings/](https://leetcode.com/problems/construct-k-palindrome-strings/)
- **Tags:** hash-table, string, greedy, counting

## Problem

Given a string `s` and an integer `k`, return `true` if you can use all the characters in `s` to construct **non-empty** `k` palindrome strings or `false` otherwise.

**Example 1:**

```
**Input:** s = "annabelle", k = 2
**Output:** true
**Explanation:** You can construct two palindromes using all characters in s.
Some possible constructions "anna" + "elble", "anbna" + "elle", "anellena" + "b"
```

**Example 2:**

```
**Input:** s = "leetcode", k = 3
**Output:** false
**Explanation:** It is impossible to construct 3 palindromes using all the characters of s.
```

**Example 3:**

```
**Input:** s = "true", k = 4
**Output:** true
**Explanation:** The only possible solution is to put each character in a separate string.
```

**Constraints:**

- `1 <= s.length <= 10^{5}`

	- `s` consists of lowercase English letters.

	- `1 <= k <= 10^{5}`

### Hints

1. If the s.length < k we cannot construct k strings from s and answer is false.
2. If the number of characters that have odd counts is > k then the minimum number of palindrome strings we can construct is > k and answer is false.
3. Otherwise you can construct exactly k palindrome strings and answer is true (why ?).

## Approach

<!-- Describe your solution approach here -->

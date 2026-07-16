# 1003. Check If Word Is Valid After Substitutions

- **Difficulty:** Medium
- **LeetCode:** [https://leetcode.com/problems/check-if-word-is-valid-after-substitutions/](https://leetcode.com/problems/check-if-word-is-valid-after-substitutions/)
- **Tags:** string, stack

## Problem

Given a string `s`, determine if it is **valid**.

A string `s` is **valid** if, starting with an empty string `t = ""`, you can **transform **`t`** into **`s` after performing the following operation **any number of times**:

- Insert string `"abc"` into any position in `t`. More formally, `t` becomes `t_{left} + "abc" + t_{right}`, where `t == t_{left} + t_{right}`. Note that `t_{left}` and `t_{right}` may be **empty**.

Return `true` *if *`s`* is a **valid** string, otherwise, return* `false`.

**Example 1:**

```
**Input:** s = "aabcbc"
**Output:** true
**Explanation:**
"" -> "abc" -> "aabcbc"
Thus, "aabcbc" is valid.
```

**Example 2:**

```
**Input:** s = "abcabcababcc"
**Output:** true
**Explanation:**
"" -> "abc" -> "abcabc" -> "abcabcabc" -> "abcabcababcc"
Thus, "abcabcababcc" is valid.
```

**Example 3:**

```
**Input:** s = "abccba"
**Output:** false
**Explanation:** It is impossible to get "abccba" using the operation.
```

**Constraints:**

- `1 <= s.length <= 2 * 10^{4}`

	- `s` consists of letters `'a'`, `'b'`, and `'c'`

## Approach

<!-- Describe your solution approach here -->

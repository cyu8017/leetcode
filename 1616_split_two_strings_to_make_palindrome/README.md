# 1616. Split Two Strings to Make Palindrome

- **Difficulty:** Medium
- **LeetCode:** [https://leetcode.com/problems/split-two-strings-to-make-palindrome/](https://leetcode.com/problems/split-two-strings-to-make-palindrome/)
- **Tags:** two-pointers, string

## Problem

You are given two strings `a` and `b` of the same length. Choose an index and split both strings **at the same index**, splitting `a` into two strings: `a_{prefix}` and `a_{suffix}` where `a = a_{prefix} + a_{suffix}`, and splitting `b` into two strings: `b_{prefix}` and `b_{suffix}` where `b = b_{prefix} + b_{suffix}`. Check if `a_{prefix} + b_{suffix}` or `b_{prefix} + a_{suffix}` forms a palindrome.

When you split a string `s` into `s_{prefix}` and `s_{suffix}`, either `s_{suffix}` or `s_{prefix}` is allowed to be empty. For example, if `s = "abc"`, then `"" + "abc"`, `"a" + "bc"`, `"ab" + "c"` , and `"abc" + ""` are valid splits.

Return `true`* if it is possible to form** a palindrome string, otherwise return *`false`.

**Notice** that `x + y` denotes the concatenation of strings `x` and `y`.

**Example 1:**

```
**Input:** a = "x", b = "y"
**Output:** true
**Explaination:** If either a or b are palindromes the answer is true since you can split in the following way:
a_{prefix} = "", a_{suffix} = "x"
b_{prefix} = "", b_{suffix} = "y"
Then, a_{prefix} + b_{suffix} = "" + "y" = "y", which is a palindrome.
```

**Example 2:**

```
**Input:** a = "xbdef", b = "xecab"
**Output:** false
```

**Example 3:**

```
**Input:** a = "ulacfd", b = "jizalu"
**Output:** true
**Explaination:** Split them at index 3:
a_{prefix} = "ula", a_{suffix} = "cfd"
b_{prefix} = "jiz", b_{suffix} = "alu"
Then, a_{prefix} + b_{suffix} = "ula" + "alu" = "ulaalu", which is a palindrome.
```

**Constraints:**

- `1 <= a.length, b.length <= 10^{5}`

	- `a.length == b.length`

	- `a` and `b` consist of lowercase English letters

### Hints

1. Try finding the largest prefix from a that matches a suffix in b
2. Try string matching

## Approach

<!-- Describe your solution approach here -->

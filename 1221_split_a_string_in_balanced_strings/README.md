# 1221. Split a String in Balanced Strings

- **Difficulty:** Easy
- **LeetCode:** [https://leetcode.com/problems/split-a-string-in-balanced-strings/](https://leetcode.com/problems/split-a-string-in-balanced-strings/)
- **Tags:** string, greedy, counting

## Problem

**Balanced** strings are those that have an equal quantity of `'L'` and `'R'` characters.

Given a **balanced** string `s`, split it into some number of substrings such that:

- Each substring is balanced.

Return *the **maximum** number of balanced strings you can obtain.*

**Example 1:**

```
**Input:** s = "RLRRLLRLRL"
**Output:** 4
**Explanation:** s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.
```

**Example 2:**

```
**Input:** s = "RLRRRLLRLL"
**Output:** 2
**Explanation:** s can be split into "RL", "RRRLLRLL", each substring contains same number of 'L' and 'R'.
Note that s cannot be split into "RL", "RR", "RL", "LR", "LL", because the 2^{nd} and 5^{th} substrings are not balanced.
```

**Example 3:**

```
**Input:** s = "LLLLRRRR"
**Output:** 1
**Explanation:** s can be split into "LLLLRRRR".
```

**Constraints:**

- `2 <= s.length <= 1000`

	- `s[i]` is either `'L'` or `'R'`.

	- `s` is a **balanced** string.

### Hints

1. Loop from left to right maintaining a balance variable when it gets an L increase it by one otherwise decrease it by one.
2. Whenever the balance variable reaches zero then we increase the answer by one.

## Approach

<!-- Describe your solution approach here -->

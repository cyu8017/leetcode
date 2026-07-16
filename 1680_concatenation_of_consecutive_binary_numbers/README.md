# 1680. Concatenation of Consecutive Binary Numbers

- **Difficulty:** Medium
- **LeetCode:** [https://leetcode.com/problems/concatenation-of-consecutive-binary-numbers/](https://leetcode.com/problems/concatenation-of-consecutive-binary-numbers/)
- **Tags:** math, bit-manipulation, simulation

## Problem

Given an integer `n`, return *the **decimal value** of the binary string formed by concatenating the binary representations of *`1`* to *`n`* in order, **modulo **`10^{9 }+ 7`.

**Example 1:**

```
**Input:** n = 1
**Output:** 1
**Explanation: **"1" in binary corresponds to the decimal value 1.
```

**Example 2:**

```
**Input:** n = 3
**Output:** 27
**Explanation: **In binary, 1, 2, and 3 corresponds to "1", "10", and "11".
After concatenating them, we have "11011", which corresponds to the decimal value 27.
```

**Example 3:**

```
**Input:** n = 12
**Output:** 505379714
**Explanation**: The concatenation results in "1101110010111011110001001101010111100".
The decimal value of that is 118505380540.
After modulo 10^{9} + 7, the result is 505379714.
```

**Constraints:**

- `1 <= n <= 10^{5}`

### Hints

1. Express the nth number value in a recursion formula and think about how we can do a fast evaluation.

## Approach

<!-- Describe your solution approach here -->

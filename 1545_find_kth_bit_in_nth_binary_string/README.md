# 1545. Find Kth Bit in Nth Binary String

- **Difficulty:** Medium
- **LeetCode:** [https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/](https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/)
- **Tags:** string, recursion, simulation

## Problem

Given two positive integers `n` and `k`, the binary string `S_{n}` is formed as follows:

- `S_{1} = "0"`

	- `S_{i} = S_{i - 1} + "1" + reverse(invert(S_{i - 1}))` for `i > 1`

Where `+` denotes the concatenation operation, `reverse(x)` returns the reversed string `x`, and `invert(x)` inverts all the bits in `x` (`0` changes to `1` and `1` changes to `0`).

For example, the first four strings in the above sequence are:

- `S_{1 }= "0"`

	- `S_{2 }= "0**1**1"`

	- `S_{3 }= "011**1**001"`

	- `S_{4} = "0111001**1**0110001"`

Return *the* `k^{th}` *bit* *in* `S_{n}`. It is guaranteed that `k` is valid for the given `n`.

**Example 1:**

```
**Input:** n = 3, k = 1
**Output:** "0"
**Explanation:** S_{3} is "**0**111001".
The 1^{st} bit is "0".
```

**Example 2:**

```
**Input:** n = 4, k = 11
**Output:** "1"
**Explanation:** S_{4} is "0111001101**1**0001".
The 11^{th} bit is "1".
```

**Constraints:**

- `1 <= n <= 20`

	- `1 <= k <= 2^{n} - 1`

### Hints

1. Since n is small, we can simply simulate the process of constructing S1 to Sn.

## Approach

<!-- Describe your solution approach here -->

# 3199. Count Triplets with Even XOR Set Bits I

- **Difficulty:** Easy
- **LeetCode:** [https://leetcode.com/problems/count-triplets-with-even-xor-set-bits-i/](https://leetcode.com/problems/count-triplets-with-even-xor-set-bits-i/)
- **Premium:** Yes
- **Tags:** array, bit-manipulation

## Problem

Given three integer arrays `a`, `b`, and `c`, return the number of triplets `(a[i], b[j], c[k])`, such that the bitwise `XOR` of the elements of each triplet has an **even** number of set bits.



**Example 1:**

**Input:** a = [1], b = [2], c = [3]

**Output:** 1

**Explanation:**

The only triplet is `(a[0], b[0], c[0])` and their `XOR` is: `1 XOR 2 XOR 3 = 00_{2}`.

**Example 2:**

**Input:** a = [1,1], b = [2,3], c = [1,5]

**Output:** 4

**Explanation:**

Consider these four triplets:

	- `(a[0], b[1], c[0])`: `1 XOR 3 XOR 1 = 011_{2}`

	- `(a[1], b[1], c[0])`: `1 XOR 3 XOR 1 = 011_{2}`

	- `(a[0], b[0], c[1])`: `1 XOR 2 XOR 5 = 110_{2}`

	- `(a[1], b[0], c[1])`: `1 XOR 2 XOR 5 = 110_{2}`



**Constraints:**

	- `1 <= a.length, b.length, c.length <= 100`

	- `0 <= a[i], b[i], c[i] <= 100`

---
_Problem text from the [doocs/leetcode](https://github.com/doocs/leetcode) community mirror (LeetCode Premium)._

### Hints

1. Iterate over all possible triplets and calculate its `XOR`.

## Approach

<!-- Describe your solution approach here -->

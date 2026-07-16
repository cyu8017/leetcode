# 1137. N-th Tribonacci Number

- **Difficulty:** Easy
- **LeetCode:** [https://leetcode.com/problems/n-th-tribonacci-number/](https://leetcode.com/problems/n-th-tribonacci-number/)
- **Tags:** math, dynamic-programming, memoization

## Problem

The Tribonacci sequence T_{n} is defined as follows:

T_{0} = 0, T_{1} = 1, T_{2} = 1, and T_{n+3} = T_{n} + T_{n+1} + T_{n+2} for n >= 0.

Given `n`, return the value of T_{n}.

**Example 1:**

```
**Input:** n = 4
**Output:** 4
**Explanation:**
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4
```

**Example 2:**

```
**Input:** n = 25
**Output:** 1389537
```

**Constraints:**

- `0 <= n <= 37`

	- The answer is guaranteed to fit within a 32-bit integer, ie. `answer <= 2^31 - 1`.

### Hints

1. Make an array F of length 38, and set F[0] = 0, F[1] = F[2] = 1.
2. Now write a loop where you set F[n+3] = F[n] + F[n+1] + F[n+2], and return F[n].

## Approach

<!-- Describe your solution approach here -->

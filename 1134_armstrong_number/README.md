# 1134. Armstrong Number

- **Difficulty:** Easy
- **LeetCode:** [https://leetcode.com/problems/armstrong-number/](https://leetcode.com/problems/armstrong-number/)
- **Premium:** Yes
- **Tags:** math

## Problem

Given an integer `n`, return `true` *if and only if it is an **Armstrong number***.

The `k`-digit number `n` is an Armstrong number if and only if the `k^{th}` power of each digit sums to `n`.



**Example 1:**

**Input:** n = 153
**Output:** true
**Explanation:** 153 is a 3-digit number, and 153 = 1^{3} + 5^{3} + 3^{3}.

**Example 2:**

**Input:** n = 123
**Output:** false
**Explanation:** 123 is a 3-digit number, and 123 != 1^{3} + 2^{3} + 3^{3} = 36.



**Constraints:**

	- `1 <= n <= 10^{8}`

---
_Problem text from the [doocs/leetcode](https://github.com/doocs/leetcode) community mirror (LeetCode Premium)._

### Hints

1. Check if the given k-digit number equals the sum of the k-th power of it's digits.
2. How to compute the sum of the k-th power of the digits of a number ? Can you divide the number into digits using division and modulus operations ?
3. You can find the least significant digit of a number by taking it modulus 10. And you can remove it by dividing the number by 10 (integer division). Once you have a digit, you can raise it to the power of k and add it to the sum.

## Approach

<!-- Describe your solution approach here -->

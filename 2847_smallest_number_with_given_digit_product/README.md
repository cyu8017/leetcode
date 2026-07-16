# 2847. Smallest Number With Given Digit Product

- **Difficulty:** Medium
- **LeetCode:** [https://leetcode.com/problems/smallest-number-with-given-digit-product/](https://leetcode.com/problems/smallest-number-with-given-digit-product/)
- **Premium:** Yes
- **Tags:** math, greedy

## Problem

Given a **positive** integer `n`, return *a string representing the **smallest positive** integer such that the product of its digits is equal to* `n`*, or *`"-1"`* if no such number exists*.



**Example 1:**

**Input:** n = 105
**Output:** "357"
**Explanation:** 3 * 5 * 7 = 105. It can be shown that 357 is the smallest number with a product of digits equal to 105. So the answer would be "357".

**Example 2:**

**Input:** n = 7
**Output:** "7"
**Explanation:** Since 7 has only one digit, its product of digits would be 7. We will show that 7 is the smallest number with a product of digits equal to 7. Since the product of numbers 1 to 6 is 1 to 6 respectively, so "7" would be the answer.

**Example 3:**

**Input:** n = 44
**Output:** "-1"
**Explanation:** It can be shown that there is no number such that its product of digits is equal to 44. So the answer would be "-1".



**Constraints:**

	- `1 <= n <= 10^{18}`

---
_Problem text from the [doocs/leetcode](https://github.com/doocs/leetcode) community mirror (LeetCode Premium)._

### Hints

1. Find the prime factors of `n`.
2. If there is a prime factor `p` such that `p >= 11`, the answer is `-1`. Since there are no digits whose products equal `p`.
3. Factors `5` and `7` should be included in the answer since their product with any number bigger than `1` is a 2-digit number.
4. For factors `2` and `3`, we group every three `2` into an `8` and every two `3` into a `9`.
5. For any leftover `2` or `3`, check all the possible combinations.

## Approach

<!-- Describe your solution approach here -->

# 1058. Minimize Rounding Error to Meet Target

- **Difficulty:** Medium
- **LeetCode:** [https://leetcode.com/problems/minimize-rounding-error-to-meet-target/](https://leetcode.com/problems/minimize-rounding-error-to-meet-target/)
- **Premium:** Yes
- **Tags:** array, math, string, greedy, sorting

## Problem

Given an array of `prices` `[p_{1},p_{2}...,p_{n}]` and a `target`, round each price `p_{i}` to `Round_{i}(p_{i})` so that the rounded array `[Round_{1}(p_{1}),Round_{2}(p_{2})...,Round_{n}(p_{n})]` sums to the given `target`. Each operation `Round_{i}(p_{i})` could be either `Floor(p_{i})` or `Ceil(p_{i})`.

Return the string `"-1"` if the rounded array is impossible to sum to `target`. Otherwise, return the smallest rounding error, which is defined as `Σ |Round_{i}(p_{i}) - (p_{i})|` for `i` from `1` to `n`, as a string with three places after the decimal.



**Example 1:**

**Input:** prices = ["0.700","2.800","4.900"], target = 8
**Output:** "1.000"
**Explanation:**
Use Floor, Ceil and Ceil operations to get (0.7 - 0) + (3 - 2.8) + (5 - 4.9) = 0.7 + 0.2 + 0.1 = 1.0 .

**Example 2:**

**Input:** prices = ["1.500","2.500","3.500"], target = 10
**Output:** "-1"
**Explanation:** It is impossible to meet the target.

**Example 3:**

**Input:** prices = ["1.500","2.500","3.500"], target = 9
**Output:** "1.500"



**Constraints:**

	- `1 <= prices.length <= 500`

	- Each string `prices[i]` represents a real number in the range `[0.0, 1000.0]` and has exactly 3 decimal places.

	- `0 <= target <= 10^{6}`

---
_Problem text from the [doocs/leetcode](https://github.com/doocs/leetcode) community mirror (LeetCode Premium)._

### Hints

1. If we have integer values in the array then we just need to subtract the target those integer values, so we reduced the problem.
2. Similarly if we have non integer values we have two options to put them flor(value) or ceil(value) = floor(value) + 1, so the idea is to just subtract floor(value).
3. Now the problem is different for each position we can sum just add 0 or 1 in order to sum the target, minimizing the deltas. This can be solved with DP.

## Approach

<!-- Describe your solution approach here -->

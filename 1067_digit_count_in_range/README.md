# 1067. Digit Count in Range

- **Difficulty:** Hard
- **LeetCode:** [https://leetcode.com/problems/digit-count-in-range/](https://leetcode.com/problems/digit-count-in-range/)
- **Premium:** Yes
- **Tags:** math, dynamic-programming

## Problem

Given a single-digit integer `d` and two integers `low` and `high`, return *the number of times that *`d`* occurs as a digit in all integers in the inclusive range *`[low, high]`.



**Example 1:**

**Input:** d = 1, low = 1, high = 13
**Output:** 6
**Explanation:** The digit d = 1 occurs 6 times in 1, 10, 11, 12, 13.
Note that the digit d = 1 occurs twice in the number 11.

**Example 2:**

**Input:** d = 3, low = 100, high = 250
**Output:** 35
**Explanation:** The digit d = 3 occurs 35 times in 103,113,123,130,131,...,238,239,243.



**Constraints:**

	- `0 <= d <= 9`

	- `1 <= low <= high <= 2 * 10^{8}`

---
_Problem text from the [doocs/leetcode](https://github.com/doocs/leetcode) community mirror (LeetCode Premium)._

### Hints

1. Define a function f(x) to get the requested sum from 1 to x. So the answer will be f(hi) - f(lo - 1)
2. In order to solve f(x) we need to do a DP over digits approach.

## Approach

<!-- Describe your solution approach here -->

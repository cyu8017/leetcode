# 0258. Add Digits

- **Difficulty:** Easy
- **LeetCode:** [https://leetcode.com/problems/add-digits/](https://leetcode.com/problems/add-digits/)
- **Tags:** math, simulation, number-theory

## Problem

Given an integer `num`, repeatedly add all its digits until the result has only one digit, and return it.

**Example 1:**

```
**Input:** num = 38
**Output:** 2
**Explanation:** The process is
38 --> 3 + 8 --> 11
11 --> 1 + 1 --> 2
Since 2 has only one digit, return it.
```

**Example 2:**

```
**Input:** num = 0
**Output:** 0
```

**Constraints:**

- `0 <= num <= 2^{31} - 1`

**Follow up:** Could you do it without any loop/recursion in `O(1)` runtime?

### Hints

1. A naive implementation of the above process is trivial. Could you come up with other methods?
2. What are all the possible results?
3. How do they occur, periodically or randomly?
4. You may find this [Wikipedia article](https://en.wikipedia.org/wiki/Digital_root) useful.

## Approach

<!-- Describe your solution approach here -->

# 1556. Thousand Separator

- **Difficulty:** Easy
- **LeetCode:** [https://leetcode.com/problems/thousand-separator/](https://leetcode.com/problems/thousand-separator/)
- **Tags:** string

## Problem

Given an integer `n`, add a dot (".") as the thousands separator and return it in string format.

**Example 1:**

```
**Input:** n = 987
**Output:** "987"
```

**Example 2:**

```
**Input:** n = 1234
**Output:** "1.234"
```

**Constraints:**

- `0 <= n <= 2^{31} - 1`

### Hints

1. Scan from the back of the integer and use dots to connect blocks with length 3 except the last block.

## Approach

<!-- Describe your solution approach here -->

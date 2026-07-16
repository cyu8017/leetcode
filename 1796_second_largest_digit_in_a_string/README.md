# 1796. Second Largest Digit in a String

- **Difficulty:** Easy
- **LeetCode:** [https://leetcode.com/problems/second-largest-digit-in-a-string/](https://leetcode.com/problems/second-largest-digit-in-a-string/)
- **Tags:** hash-table, string

## Problem

Given an alphanumeric string `s`, return *the **second largest** numerical digit that appears in *`s`*, or *`-1`* if it does not exist*.

An **alphanumeric** **string is a string consisting of lowercase English letters and digits.

**Example 1:**

```
**Input:** s = "dfa12321afd"
**Output:** 2
**Explanation:** The digits that appear in s are [1, 2, 3]. The second largest digit is 2.
```

**Example 2:**

```
**Input:** s = "abc1111"
**Output:** -1
**Explanation:** The digits that appear in s are [1]. There is no second largest digit.
```

**Constraints:**

- `1 <= s.length <= 500`

	- `s` consists of only lowercase English letters and digits.

### Hints

1. First of all, get the distinct characters since we are only interested in those
2. Let's note that there might not be any digits.

## Approach

<!-- Describe your solution approach here -->

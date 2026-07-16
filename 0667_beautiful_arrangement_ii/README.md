# 0667. Beautiful Arrangement II

- **Difficulty:** Medium
- **LeetCode:** [https://leetcode.com/problems/beautiful-arrangement-ii/](https://leetcode.com/problems/beautiful-arrangement-ii/)
- **Tags:** array, math

## Problem

Given two integers `n` and `k`, construct a list `answer` that contains `n` different positive integers ranging from `1` to `n` and obeys the following requirement:

- Suppose this list is `answer = [a_{1}, a_{2}, a_{3}, ... , a_{n}]`, then the list `[|a_{1} - a_{2}|, |a_{2} - a_{3}|, |a_{3} - a_{4}|, ... , |a_{n-1} - a_{n}|]` has exactly `k` distinct integers.

Return *the list* `answer`. If there multiple valid answers, return **any of them**.

**Example 1:**

```
**Input:** n = 3, k = 1
**Output:** [1,2,3]
Explanation: The [1,2,3] has three different positive integers ranging from 1 to 3, and the [1,1] has exactly 1 distinct integer: 1
```

**Example 2:**

```
**Input:** n = 3, k = 2
**Output:** [1,3,2]
Explanation: The [1,3,2] has three different positive integers ranging from 1 to 3, and the [2,1] has exactly 2 distinct integers: 1 and 2.
```

**Constraints:**

- `1 <= k < n <= 10^{4}`

## Approach

<!-- Describe your solution approach here -->

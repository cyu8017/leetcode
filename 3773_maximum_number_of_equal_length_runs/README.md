# 3773. Maximum Number of Equal Length Runs

- **Difficulty:** Medium
- **LeetCode:** [https://leetcode.com/problems/maximum-number-of-equal-length-runs/](https://leetcode.com/problems/maximum-number-of-equal-length-runs/)
- **Premium:** Yes
- **Tags:** hash-table, string, counting

## Problem

You are given a string `s` consisting of lowercase English letters.

A **run** in `s` is a **substring** of **equal** letters that cannot be extended further. For example, the runs in `"hello"` are `"h"`, `"e"`, `"ll"`, and `"o"`.

You can **select** runs that have the **same** length in `s`.

Return an integer denoting the **maximum** number of runs you can select in `s`.



**Example 1:**

**Input:** s = "hello"

**Output:** 3

**Explanation:**

The runs in `s` are `"h"`, `"e"`, `"ll"`, and `"o"`. You can select `"h"`, `"e"`, and `"o"` because they have the same length 1.

**Example 2:**

**Input:** s = "aaabaaa"

**Output:** 2

**Explanation:**

The runs in `s` are `"aaa"`, `"b"`, and `"aaa"`. You can select `"aaa"` and `"aaa"` because they have the same length 3.



**Constraints:**

	- `1 <= s.length <= 10^{5}`

	- `s` consists of lowercase English letters only.

---
_Problem text from the [doocs/leetcode](https://github.com/doocs/leetcode) community mirror (LeetCode Premium)._

### Hints

1. Split the string when adjacent characters are not equal, and use those to make the runs
2. Use a hashmap to group runs of the same length

## Approach

<!-- Describe your solution approach here -->

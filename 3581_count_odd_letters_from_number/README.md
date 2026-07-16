# 3581. Count Odd Letters from Number

- **Difficulty:** Easy
- **LeetCode:** [https://leetcode.com/problems/count-odd-letters-from-number/](https://leetcode.com/problems/count-odd-letters-from-number/)
- **Premium:** Yes
- **Tags:** hash-table, string, simulation, counting

## Problem

You are given an integer `n` perform the following steps:

	- Convert each digit of `n` into its *lowercase English word* (e.g., 4 → "four", 1 → "one").

	- **Concatenate** those words in the **original digit order** to form a string `s`.

Return the number of **distinct** characters in `s` that appear an **odd** number of times.



**Example 1:**

**Input:** n = 41

**Output:** 5

**Explanation:**

41 → `"fourone"`

Characters with odd frequencies: `'f'`, `'u'`, `'r'`, `'n'`, `'e'`. Thus, the answer is 5.

**Example 2:**

**Input:** n = 20

**Output:** 5

**Explanation:**

20 → `"twozero"`

Characters with odd frequencies: `'t'`, `'w'`, `'z'`, `'e'`, `'r'`. Thus, the answer is 5.



**Constraints:**

	- `1 <= n <= 10^{9}`

---
_Problem text from the [doocs/leetcode](https://github.com/doocs/leetcode) community mirror (LeetCode Premium)._

### Hints

1. Simulate as described

## Approach

<!-- Describe your solution approach here -->

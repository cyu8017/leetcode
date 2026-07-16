# 1180. Count Substrings with Only One Distinct Letter

- **Difficulty:** Easy
- **LeetCode:** [https://leetcode.com/problems/count-substrings-with-only-one-distinct-letter/](https://leetcode.com/problems/count-substrings-with-only-one-distinct-letter/)
- **Premium:** Yes
- **Tags:** math, string

## Problem

Given a string `s`, return *the number of substrings that have only **one distinct** letter*.



**Example 1:**

**Input:** s = "aaaba"
**Output:** 8
**Explanation: **The substrings with one distinct letter are "aaa", "aa", "a", "b".
"aaa" occurs 1 time.
"aa" occurs 2 times.
"a" occurs 4 times.
"b" occurs 1 time.
So the answer is 1 + 2 + 4 + 1 = 8.

**Example 2:**

**Input:** s = "aaaaaaaaaa"
**Output:** 55



**Constraints:**

	- `1 <= s.length <= 1000`

	- `s[i]` consists of only lowercase English letters.

---
_Problem text from the [doocs/leetcode](https://github.com/doocs/leetcode) community mirror (LeetCode Premium)._

### Hints

1. What if we divide the string into substrings containing only one distinct character with maximal lengths?
2. Now that you have sub-strings with only one distinct character, Try to come up with a formula that counts the number of its sub-strings.
3. Alternatively, Observe that the constraints are small so you can use brute force.

## Approach

<!-- Describe your solution approach here -->

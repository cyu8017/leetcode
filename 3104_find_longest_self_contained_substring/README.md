# 3104. Find Longest Self-Contained Substring

- **Difficulty:** Hard
- **LeetCode:** [https://leetcode.com/problems/find-longest-self-contained-substring/](https://leetcode.com/problems/find-longest-self-contained-substring/)
- **Premium:** Yes
- **Tags:** hash-table, string, sorting

## Problem

Given a string `s`, your task is to find the length of the **longest self-contained** substring of `s`.

A substring `t` of a string `s` is called **self-contained **if `t != s` and for every character in `t`, it doesn't exist in the *rest* of `s`.

Return the length of the *longest** **self-contained *substring of `s` if it exists, otherwise, return -1.



**Example 1:**

**Input:** s = "abba"

**Output:** 2

**Explanation:**

Let's check the substring `"bb"`. You can see that no other `"b"` is outside of this substring. Hence the answer is 2.

**Example 2:**

**Input:** s = "abab"

**Output:** -1

**Explanation:**

Every substring we choose does not satisfy the described property (there is some character which is inside and outside of that substring). So the answer would be -1.

**Example 3:**

**Input:** s = "abacd"

**Output:** 4

**Explanation:**

Let's check the substring `"abac"`. There is only one character outside of this substring and that is `"d"`. There is no `"d"` inside the chosen substring, so it satisfies the condition and the answer is 4.



**Constraints:**

	- `2 <= s.length <= 5 * 10^{4}`

	- `s` consists only of lowercase English letters.

---
_Problem text from the [doocs/leetcode](https://github.com/doocs/leetcode) community mirror (LeetCode Premium)._

### Hints

1. Fix the start index of the substring.
2. For some fixed index `start`, let's try to find some index `end` such that this substring satisfies the property and also `end` is as maximum as possible.
3. Write some recursive function `shrink(start, end)` that gives a substring. If the substring is valid, then return `end`. Otherwise, it reduces <`end` to reach some valid `end`.
4. For some `shrink(start, end)`, if the substring is not valid, it means there is some character that is both inside and outside of the substring. Now try to reduce `end` such that it does not contain that character anymore.
5. If you implement the `shrink(start, end)` function optimally, you'll achieve `O(n * 26 * 26)` by using partial sum.

## Approach

<!-- Describe your solution approach here -->

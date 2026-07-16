# 2083. Substrings That Begin and End With the Same Letter

- **Difficulty:** Medium
- **LeetCode:** [https://leetcode.com/problems/substrings-that-begin-and-end-with-the-same-letter/](https://leetcode.com/problems/substrings-that-begin-and-end-with-the-same-letter/)
- **Premium:** Yes
- **Tags:** hash-table, math, string, counting, prefix-sum

## Problem

You are given a **0-indexed** string `s` consisting of only lowercase English letters. Return *the number of **substrings** in *`s` *that begin and end with the **same** character.*

A **substring** is a contiguous non-empty sequence of characters within a string.



**Example 1:**

**Input:** s = "abcba"
**Output:** 7
**Explanation:**
The substrings of length 1 that start and end with the same letter are: "a", "b", "c", "b", and "a".
The substring of length 3 that starts and ends with the same letter is: "bcb".
The substring of length 5 that starts and ends with the same letter is: "abcba".

**Example 2:**

**Input:** s = "abacad"
**Output:** 9
**Explanation:**
The substrings of length 1 that start and end with the same letter are: "a", "b", "a", "c", "a", and "d".
The substrings of length 3 that start and end with the same letter are: "aba" and "aca".
The substring of length 5 that starts and ends with the same letter is: "abaca".

**Example 3:**

**Input:** s = "a"
**Output:** 1
**Explanation:**
The substring of length 1 that starts and ends with the same letter is: "a".



**Constraints:**

	- `1 <= s.length <= 10^{5}`

	- `s` consists only of lowercase English letters.

---
_Problem text from the [doocs/leetcode](https://github.com/doocs/leetcode) community mirror (LeetCode Premium)._

### Hints

1. In the string "abacad", the letter "a" appears 3 times. How many substrings begin with the first "a" and end with any "a"?
2. There are 3 substrings ("a", "aba", and "abaca"). How many substrings begin with the second "a" and end with any "a"? How about the third?
3. 2 substrings begin with the second "a" ("a", and "aca") and 1 substring begins with the third "a" ("a").
4. There is a total of 3 + 2 + 1 = 6 substrings that begin and end with "a".
5. If a character appears i times in the string, there are i * (i + 1) / 2 substrings that begin and end with that character.

## Approach

<!-- Describe your solution approach here -->

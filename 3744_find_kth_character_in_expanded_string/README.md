# 3744. Find Kth Character in Expanded String

- **Difficulty:** Medium
- **LeetCode:** [https://leetcode.com/problems/find-kth-character-in-expanded-string/](https://leetcode.com/problems/find-kth-character-in-expanded-string/)
- **Premium:** Yes
- **Tags:** string

## Problem

You are given a string `s` consisting of one or more words separated by single spaces. Each word in `s` consists of lowercase English letters.

We obtain the **expanded** string `t` from `s` as follows:

	- For each **word** in `s`, repeat its first character once, then its second character twice, and so on.

For example, if `s = "hello world"`, then `t = "heelllllllooooo woorrrllllddddd"`.

You are also given an integer `k`, representing a **valid** index of the string `t`.

Return the `k^{th}` character of the string `t`.



**Example 1:**

**Input:** s = "hello world", k = 0

**Output:** "h"

**Explanation:**

`t = "heelllllllooooo woorrrllllddddd"`. Therefore, the answer is `t[0] = "h"`.

**Example 2:**

**Input:** s = "hello world", k = 15

**Output:** " "

**Explanation:**

`t = "heelllllllooooo woorrrllllddddd"`. Therefore, the answer is `t[15] = " "`.



**Constraints:**

	- `1 <= s.length <= 10^{5}`

	- `s` contains only lowercase English letters and spaces `' '`.

	- `s` **does not contain** any leading or trailing spaces.

	- All the words in `s` are separated by a **single space**.

	- `0 <= k < t.length`. That is, `k` is a **valid** index of `t`.

---
_Problem text from the [doocs/leetcode](https://github.com/doocs/leetcode) community mirror (LeetCode Premium)._

### Hints

1. Use the index of a character in the word to calculate how many times it is repeated in `t`.
2. Reduce `k` by that repetition count as you iterate through the characters.
3. Handle spaces as single characters (cost 1) and reset the index counter for each new word.

## Approach

<!-- Describe your solution approach here -->

# 0616. Add Bold Tag in String

- **Difficulty:** Medium
- **LeetCode:** [https://leetcode.com/problems/add-bold-tag-in-string/](https://leetcode.com/problems/add-bold-tag-in-string/)
- **Premium:** Yes
- **Tags:** array, hash-table, string, trie, string-matching

## Problem

You are given a string `s` and an array of strings `words`.

You should add a closed pair of bold tag `` and `` to wrap the substrings in `s` that exist in `words`.

	- If two such substrings overlap, you should wrap them together with only one pair of closed bold-tag.

	- If two substrings wrapped by bold tags are consecutive, you should combine them.

Return `s` *after adding the bold tags*.



**Example 1:**

**Input:** s = "abcxyz123", words = ["abc","123"]
**Output:** "**abc**xyz**123**"
**Explanation:** The two strings of words are substrings of s as following: "abcxyz123".
We add ** before each substring and ** after each substring.

**Example 2:**

**Input:** s = "aaabbb", words = ["aa","b"]
**Output:** "**aaabbb**"
**Explanation:**
"aa" appears as a substring two times: "aaabbb" and "aaabbb".
"b" appears as a substring three times: "aaabbb", "aaabbb", and "aaabbb".
We add ** before each substring and ** after each substring: "**aa**a**b****b****b**".
Since the first two **'s overlap, we merge them: "aaa****b****b****b**".
Since now the four **'s are consecutive, we merge them: "aaabbb**".



**Constraints:**

	- `1 <= s.length <= 1000`

	- `0 <= words.length <= 100`

	- `1 <= words[i].length <= 1000`

	- `s` and `words[i]` consist of English letters and digits.

	- All the values of `words` are **unique**.



**Note:** This question is the same as 758. Bold Words in String.

---
_Problem text from the [doocs/leetcode](https://github.com/doocs/leetcode) community mirror (LeetCode Premium)._

## Approach

<!-- Describe your solution approach here -->

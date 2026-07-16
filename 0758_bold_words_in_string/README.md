# 0758. Bold Words in String

- **Difficulty:** Medium
- **LeetCode:** [https://leetcode.com/problems/bold-words-in-string/](https://leetcode.com/problems/bold-words-in-string/)
- **Premium:** Yes
- **Tags:** array, hash-table, string, trie, string-matching

## Problem

Given an array of keywords `words` and a string `s`, make all appearances of all keywords `words[i]` in `s` bold. Any letters between `` and `` tags become bold.

Return `s` *after adding the bold tags*. The returned string should use the least number of tags possible, and the tags should form a valid combination.



**Example 1:**

**Input:** words = ["ab","bc"], s = "aabcd"
**Output:** "a**abc**d"
**Explanation:** Note that returning `"aabcd"` would use more tags, so it is incorrect.

**Example 2:**

**Input:** words = ["ab","cb"], s = "aabcd"
**Output:** "a**ab**cd"



**Constraints:**

	- `1 <= s.length <= 500`

	- `0 <= words.length <= 50`

	- `1 <= words[i].length <= 10`

	- `s` and `words[i]` consist of lowercase English letters.



**Note:** This question is the same as 616. Add Bold Tag in String.

---
_Problem text from the [doocs/leetcode](https://github.com/doocs/leetcode) community mirror (LeetCode Premium)._

### Hints

1. First, determine which letters are bold and store that information in mask[i] = if i-th character is bold.
Then, insert the tags at the beginning and end of groups.  The start of a group is if and only if (mask[i] and (i == 0 or not mask[i-1])), and the end of a group is similar.

## Approach

<!-- Describe your solution approach here -->

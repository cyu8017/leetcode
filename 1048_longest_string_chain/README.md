# 1048. Longest String Chain

- **Difficulty:** Medium
- **LeetCode:** [https://leetcode.com/problems/longest-string-chain/](https://leetcode.com/problems/longest-string-chain/)
- **Tags:** array, hash-table, two-pointers, string, dynamic-programming, sorting

## Problem

You are given an array of `words` where each word consists of lowercase English letters.

`word_{A}` is a **predecessor** of `word_{B}` if and only if we can insert **exactly one** letter anywhere in `word_{A}` **without changing the order of the other characters** to make it equal to `word_{B}`.

- For example, `"abc"` is a **predecessor** of `"abac"`, while `"cba"` is not a **predecessor** of `"bcad"`.

A **word chain** *is a sequence of words `[word_{1}, word_{2}, ..., word_{k}]` with `k >= 1`, where `word_{1}` is a **predecessor** of `word_{2}`, `word_{2}` is a **predecessor** of `word_{3}`, and so on. A single word is trivially a **word chain** with `k == 1`.

Return *the **length** of the **longest possible word chain** with words chosen from the given list of *`words`.

**Example 1:**

```
**Input:** words = ["a","b","ba","bca","bda","bdca"]
**Output:** 4
**Explanation**: One of the longest word chains is ["a","ba","bda","bdca"].
```

**Example 2:**

```
**Input:** words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]
**Output:** 5
**Explanation:** All the words can be put in a word chain ["xb", "xbc", "cxbc", "pcxbc", "pcxbcf"].
```

**Example 3:**

```
**Input:** words = ["abcd","dbqca"]
**Output:** 1
**Explanation:** The trivial word chain ["abcd"] is one of the longest word chains.
["abcd","dbqca"] is not a valid word chain because the ordering of the letters is changed.
```

**Constraints:**

- `1 <= words.length <= 1000`

	- `1 <= words[i].length <= 16`

	- `words[i]` only consists of lowercase English letters.

### Hints

1. Instead of adding a character, try deleting a character to form a chain in reverse.
2. For each word in order of length, for each word2 which is word with one character removed, length[word2] = max(length[word2], length[word] + 1).

## Approach

<!-- Describe your solution approach here -->

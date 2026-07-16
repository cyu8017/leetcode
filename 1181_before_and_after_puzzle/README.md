# 1181. Before and After Puzzle

- **Difficulty:** Medium
- **LeetCode:** [https://leetcode.com/problems/before-and-after-puzzle/](https://leetcode.com/problems/before-and-after-puzzle/)
- **Premium:** Yes
- **Tags:** array, hash-table, string, sorting

## Problem

Given a list of `phrases`, generate a list of Before and After puzzles.

A *phrase* is a string that consists of lowercase English letters and spaces only. No space appears in the start or the end of a phrase. There are no consecutive spaces in a phrase.

*Before and After puzzles* are phrases that are formed by merging two phrases where the **last word of the first phrase** is the same as the **first word of the second phrase**. Note that only the *last word of the first phrase* and the *first word of the second phrase* are merged in this process.

Return the Before and After puzzles that can be formed by every two phrases `phrases[i]` and `phrases[j]` where `i != j`. Note that the order of matching two phrases matters, we want to consider both orders.

You should return a list of **distinct** strings **sorted lexicographically**, after removing all *duplicate* phrases in the generated Before and After puzzles.



**Example 1:**

**Input:** phrases = ["writing code","code rocks"]

**Output:** ["writing code rocks"]

**Example 2:**

**Input:** phrases = ["mission statement","a quick bite to eat","a chip off the old block","chocolate bar","mission impossible","a man on a mission","block party","eat my words","bar of soap"]

**Output:** ["a chip off the old block party","a man on a mission impossible","a man on a mission statement","a quick bite to eat my words","chocolate bar of soap"]

**Example 3:**

**Input:** phrases = ["a","b","a"]

**Output:** ["a"]

**Example 4:**

**Input:** phrases = ["ab ba","ba ab","ab ba"]

**Output:** ["ab ba ab","ba ab ba"]



**Constraints:**

	- `1 <= phrases.length <= 100`

	- `1 <= phrases[i].length <= 100`

---
_Problem text from the [doocs/leetcode](https://github.com/doocs/leetcode) community mirror (LeetCode Premium)._

### Hints

1. What if you check every pair of strings (bruteforce)?
2. For every two strings, check if they can form a puzzle by comparing their last and first words.

## Approach

<!-- Describe your solution approach here -->

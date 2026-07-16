# 1100. Find K-Length Substrings With No Repeated Characters

- **Difficulty:** Medium
- **LeetCode:** [https://leetcode.com/problems/find-k-length-substrings-with-no-repeated-characters/](https://leetcode.com/problems/find-k-length-substrings-with-no-repeated-characters/)
- **Premium:** Yes
- **Tags:** hash-table, string, sliding-window

## Problem

Given a string `s` and an integer `k`, return *the number of substrings in *`s`* of length *`k`* with no repeated characters*.



**Example 1:**

**Input:** s = "havefunonleetcode", k = 5
**Output:** 6
**Explanation:** There are 6 substrings they are: 'havef','avefu','vefun','efuno','etcod','tcode'.

**Example 2:**

**Input:** s = "home", k = 5
**Output:** 0
**Explanation:** Notice k can be larger than the length of s. In this case, it is not possible to find any substring.



**Constraints:**

	- `1 <= s.length <= 10^{4}`

	- `s` consists of lowercase English letters.

	- `1 <= k <= 10^{4}`

---
_Problem text from the [doocs/leetcode](https://github.com/doocs/leetcode) community mirror (LeetCode Premium)._

### Hints

1. How to check efficiently each K-length substring?
2. First store the first leftmost K-length substring in a hashTable or array of frequencies.
3. Then iterate through the rest of characters and erase the first element and add the next element from the right. If in the hashTable we have K different character we add 1 to the counter. After that return as answer the counter.

## Approach

<!-- Describe your solution approach here -->

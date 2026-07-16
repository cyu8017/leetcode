# 3557. Find Maximum Number of Non Intersecting Substrings

- **Difficulty:** Medium
- **LeetCode:** [https://leetcode.com/problems/find-maximum-number-of-non-intersecting-substrings/](https://leetcode.com/problems/find-maximum-number-of-non-intersecting-substrings/)
- **Tags:** hash-table, string, dynamic-programming, greedy

## Problem

You are given a string `word`.

Return the **maximum** number of non-intersecting **substrings** of word that are at **least** four characters long and start and end with the same letter.

**Example 1:**

**Input:** word = "abcdeafdef"

**Output:** 2

**Explanation:**

The two substrings are `"abcdea"` and `"fdef"`.

**Example 2:**

**Input:** word = "bcdaaaab"

**Output:** 1

**Explanation:**

The only substring is `"aaaa"`. Note that we cannot **also** choose `"bcdaaaab"` since it intersects with the other substring.

**Constraints:**

- `1 <= word.length <= 2 * 10^{5}`

	- `word` consists only of lowercase English letters.

### Hints

1. Can we solve the problem using Dynamic Programming?
2. For each character `c`, store all occurrence indices in order
3. At each position `i`, let `j` be the first index of `word[i]`; if `i - j >= 3`, we can form substring `[j, i]`
4. For each index, also store the maximum for **any** substring ending before that index in the dp.

## Approach

<!-- Describe your solution approach here -->

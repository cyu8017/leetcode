# 0266. Palindrome Permutation

- **Difficulty:** Easy
- **LeetCode:** [https://leetcode.com/problems/palindrome-permutation/](https://leetcode.com/problems/palindrome-permutation/)
- **Premium:** Yes
- **Tags:** hash-table, string, bit-manipulation

## Problem

Given a string `s`, return `true` *if a permutation of the string could form a ****palindrome**** and *`false`* otherwise*.



**Example 1:**

**Input:** s = "code"
**Output:** false

**Example 2:**

**Input:** s = "aab"
**Output:** true

**Example 3:**

**Input:** s = "carerac"
**Output:** true



**Constraints:**

	- `1 <= s.length <= 5000`

	- `s` consists of only lowercase English letters.

---
_Problem text from the [doocs/leetcode](https://github.com/doocs/leetcode) community mirror (LeetCode Premium)._

### Hints

1. Consider the palindromes of odd vs even length. What difference do you notice?
2. Count the frequency of each character.
3. If each character occurs even number of times, then it must be a palindrome. How about character which occurs odd number of times?

## Approach

<!-- Describe your solution approach here -->

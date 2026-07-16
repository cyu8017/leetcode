# 2381. Shifting Letters II

- **Difficulty:** Medium
- **LeetCode:** [https://leetcode.com/problems/shifting-letters-ii/](https://leetcode.com/problems/shifting-letters-ii/)
- **Tags:** array, string, prefix-sum

## Problem

You are given a string `s` of lowercase English letters and a 2D integer array `shifts` where `shifts[i] = [start_{i}, end_{i}, direction_{i}]`. For every `i`, **shift** the characters in `s` from the index `start_{i}` to the index `end_{i}` (**inclusive**) forward if `direction_{i} = 1`, or shift the characters backward if `direction_{i} = 0`.

Shifting a character **forward** means replacing it with the **next** letter in the alphabet (wrapping around so that `'z'` becomes `'a'`). Similarly, shifting a character **backward** means replacing it with the **previous** letter in the alphabet (wrapping around so that `'a'` becomes `'z'`).

Return *the final string after all such shifts to *`s`* are applied*.

**Example 1:**

```
**Input:** s = "abc", shifts = [[0,1,0],[1,2,1],[0,2,1]]
**Output:** "ace"
**Explanation:** Firstly, shift the characters from index 0 to index 1 backward. Now s = "zac".
Secondly, shift the characters from index 1 to index 2 forward. Now s = "zbd".
Finally, shift the characters from index 0 to index 2 forward. Now s = "ace".
```

**Example 2:**

```
**Input:** s = "dztz", shifts = [[0,0,0],[1,1,1]]
**Output:** "catz"
**Explanation:** Firstly, shift the characters from index 0 to index 0 backward. Now s = "cztz".
Finally, shift the characters from index 1 to index 1 forward. Now s = "catz".
```

**Constraints:**

- `1 <= s.length, shifts.length <= 5 * 10^{4}`

	- `shifts[i].length == 3`

	- `0 <= start_{i} <= end_{i} < s.length`

	- `0 <= direction_{i} <= 1`

	- `s` consists of lowercase English letters.

### Hints

1. Instead of shifting every character in each shift, could you keep track of which characters are shifted and by how much across all shifts?
2. Try marking the start and ends of each shift, then perform a prefix sum of the shifts.

## Approach

<!-- Describe your solution approach here -->

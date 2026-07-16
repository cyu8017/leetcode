# 1427. Perform String Shifts

- **Difficulty:** Easy
- **LeetCode:** [https://leetcode.com/problems/perform-string-shifts/](https://leetcode.com/problems/perform-string-shifts/)
- **Premium:** Yes
- **Tags:** array, math, string

## Problem

You are given a string `s` containing lowercase English letters, and a matrix `shift`, where `shift[i] = [direction_{i}, amount_{i}]`:

	- `direction_{i}` can be `0` (for left shift) or `1` (for right shift).

	- `amount_{i}` is the amount by which string `s` is to be shifted.

	- A left shift by 1 means remove the first character of `s` and append it to the end.

	- Similarly, a right shift by 1 means remove the last character of `s` and add it to the beginning.

Return the final string after all operations.



**Example 1:**

**Input:** s = "abc", shift = [[0,1],[1,2]]
**Output:** "cab"
**Explanation:**
[0,1] means shift to left by 1. "abc" -> "bca"
[1,2] means shift to right by 2. "bca" -> "cab"

**Example 2:**

**Input:** s = "abcdefg", shift = [[1,1],[1,1],[0,2],[1,3]]
**Output:** "efgabcd"
**Explanation:**
[1,1] means shift to right by 1. "abcdefg" -> "gabcdef"
[1,1] means shift to right by 1. "gabcdef" -> "fgabcde"
[0,2] means shift to left by 2. "fgabcde" -> "abcdefg"
[1,3] means shift to right by 3. "abcdefg" -> "efgabcd"



**Constraints:**

	- `1 <= s.length <= 100`

	- `s` only contains lower case English letters.

	- `1 <= shift.length <= 100`

	- `shift[i].length == 2`

	- `direction_{i}`_{ }is either `0` or `1`.

	- `0 <= amount_{i} <= 100`

---
_Problem text from the [doocs/leetcode](https://github.com/doocs/leetcode) community mirror (LeetCode Premium)._

### Hints

1. Intuitively performing all shift operations is acceptable due to the constraints.
2. You may notice that left shift cancels the right shift, so count the total left shift times (may be negative if the final result is right shift), and perform it once.

## Approach

<!-- Describe your solution approach here -->

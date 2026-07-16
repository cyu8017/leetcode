# 1153. String Transforms Into Another String

- **Difficulty:** Hard
- **LeetCode:** [https://leetcode.com/problems/string-transforms-into-another-string/](https://leetcode.com/problems/string-transforms-into-another-string/)
- **Premium:** Yes
- **Tags:** hash-table, string, graph-theory

## Problem

Given two strings `str1` and `str2` of the same length, determine whether you can transform `str1` into `str2` by doing **zero or more** *conversions*.

In one conversion you can convert **all** occurrences of one character in `str1` to **any** other lowercase English character.

Return `true` if and only if you can transform `str1` into `str2`.



**Example 1:**

**Input:** str1 = "aabcc", str2 = "ccdee"
**Output:** true
**Explanation: **Convert 'c' to 'e' then 'b' to 'd' then 'a' to 'c'. Note that the order of conversions matter.

**Example 2:**

**Input:** str1 = "leetcode", str2 = "codeleet"
**Output:** false
**Explanation: **There is no way to transform str1 to str2.



**Constraints:**

	- `1 <= str1.length == str2.length <= 10^{4}`

	- `str1` and `str2` contain only lowercase English letters.

---
_Problem text from the [doocs/leetcode](https://github.com/doocs/leetcode) community mirror (LeetCode Premium)._

### Hints

1. Model the problem as a graph problem. Add an edge from one character to another if you need to convert between them.
2. What if one character needs to be converted into more than one character?
3. There would be no solution. Thus, every node can have at most one outgoing edge.
4. How to process a linked list?
5. How to process a cycle?
6. What if there is a character with no outgoing edge? You can use it to break all cycles!

## Approach

<!-- Describe your solution approach here -->

# 2796. Repeat String

- **Difficulty:** Easy
- **LeetCode:** [https://leetcode.com/problems/repeat-string/](https://leetcode.com/problems/repeat-string/)
- **Premium:** Yes

## Problem

Write code that enhances all strings such that you can call the `string.replicate(x)` method on any string and it will return repeated string `x` times.

Try to implement it without using the built-in method `string.repeat`.



**Example 1:**

**Input:** str = "hello", times = 2
**Output:** "hellohello"
**Explanation:** "hello" is repeated 2 times

**Example 2:**

**Input:** str = "code", times = 3
**Output:** "codecodecode"
**Explanation:** "code" is repeated 3 times

**Example 3:**

**Input:** str = "js", times = 1
**Output:** "js"
**Explanation:** "js" is repeated 1 time



**Constraints:**

	- `1 <= times <= 10^{5}`

	- `1 <= str.length <= 1000`



**Follow up:** Let's assume, for the sake of simplifying analysis, that concatenating strings is a constant time operation `O(1)`. With this assumption in mind, can you write an algorithm with a runtime complexity of `O(log n)`?

---
_Problem text from the [doocs/leetcode](https://github.com/doocs/leetcode) community mirror (LeetCode Premium)._

## Approach

<!-- Describe your solution approach here -->

# 2690. Infinite Method Object

- **Difficulty:** Easy
- **LeetCode:** [https://leetcode.com/problems/infinite-method-object/](https://leetcode.com/problems/infinite-method-object/)
- **Premium:** Yes

## Problem

Write a function that returns an **infinite-method**** object**.

An **infinite-method**** object** is defined as an object that allows you to call any method and it will always return the name of the method.

For example, if you execute `obj.abc123()`, it will return `"abc123"`.



**Example 1:**

**Input:** method = "abc123"
**Output:** "abc123"
**Explanation:**
const obj = createInfiniteObject();
obj['abc123'](); // "abc123"
The returned string should always match the method name.

**Example 2:**

**Input:** method = ".-qw73n|^2It"
**Output:** ".-qw73n|^2It"
**Explanation:** The returned string should always match the method name.



**Constraints:**

	- `0 <= method.length <= 1000`

---
_Problem text from the [doocs/leetcode](https://github.com/doocs/leetcode) community mirror (LeetCode Premium)._

### Hints

1. Javascript has the concept of Proxy. That concept is critical to this problem.
2. Override all "get" for the object. Return a function instead.
3. That function should return the "prop", i.e. the method name.

## Approach

<!-- Describe your solution approach here -->

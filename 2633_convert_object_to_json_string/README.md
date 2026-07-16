# 2633. Convert Object to JSON String

- **Difficulty:** Medium
- **LeetCode:** [https://leetcode.com/problems/convert-object-to-json-string/](https://leetcode.com/problems/convert-object-to-json-string/)
- **Premium:** Yes

## Problem

Given a value, return a valid JSON string of that value. The value can be a string, number, array, object, boolean, or null. The returned string should not include extra spaces. The order of keys should be the same as the order returned by `Object.keys()`.

Please solve it without using the built-in `JSON.stringify` method.



**Example 1:**

**Input:** object = {"y":1,"x":2}
**Output:** {"y":1,"x":2}
**Explanation:**
Return the JSON representation.
Note that the order of keys should be the same as the order returned by Object.keys().

**Example 2:**

**Input:** object = {"a":"str","b":-12,"c":true,"d":null}
**Output:** {"a":"str","b":-12,"c":true,"d":null}
**Explanation:**
The primitives of JSON are strings, numbers, booleans, and null.

**Example 3:**

**Input:** object = {"key":{"a":1,"b":[{},null,"Hello"]}}
**Output:** {"key":{"a":1,"b":[{},null,"Hello"]}}
**Explanation:**
Objects and arrays can include other objects and arrays.

**Example 4:**

**Input:** object = true
**Output:** true
**Explanation:**
Primitive types are valid inputs.



**Constraints:**

	- `value` is a valid JSON value

	- `1 <= JSON.stringify(object).length <= 10^{5}`

	- `maxNestingLevel <= 1000`

	- all strings contain only alphanumeric characters

---
_Problem text from the [doocs/leetcode](https://github.com/doocs/leetcode) community mirror (LeetCode Premium)._

### Hints

1. Consider the 4 possibilities. The object could be an array, an object, a string, or another type.
2. Think about the problem recursively. If you know how to convert any sub-data into a string, how could you use it to convert the entire data into a string?
3. If the data is a string, it's just the value surrounded by double quotes. If the data is another type, its just String(data). If the data is an array, it's the recursively stringified value of each item separated by commas. If the data is an object, it's a series of key-value pairs where each value is the recursively stringified value.

## Approach

<!-- Describe your solution approach here -->

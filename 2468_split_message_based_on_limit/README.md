# 2468. Split Message Based on Limit

- **Difficulty:** Hard
- **LeetCode:** [https://leetcode.com/problems/split-message-based-on-limit/](https://leetcode.com/problems/split-message-based-on-limit/)
- **Tags:** string, enumeration

## Problem

You are given a string, `message`, and a positive integer, `limit`.

You must **split** `message` into one or more **parts** based on `limit`. Each resulting part should have the suffix `""`, where `"b"` is to be **replaced** with the total number of parts and `"a"` is to be **replaced** with the index of the part, starting from `1` and going up to `b`. Additionally, the length of each resulting part (including its suffix) should be **equal** to `limit`, except for the last part whose length can be **at most** `limit`.

The resulting parts should be formed such that when their suffixes are removed and they are all concatenated **in order**, they should be equal to `message`. Also, the result should contain as few parts as possible.

Return* the parts *`message`* would be split into as an array of strings*. If it is impossible to split `message` as required, return* an empty array*.

**Example 1:**

```
**Input:** message = "this is really a very awesome message", limit = 9
**Output:** ["thi","s i","s r","eal","ly ","a v","ery"," aw","eso","me"," m","es","sa","ge"]
**Explanation:**
The first 9 parts take 3 characters each from the beginning of message.
The next 5 parts take 2 characters each to finish splitting message.
In this example, each part, including the last, has length 9.
It can be shown it is not possible to split message into less than 14 parts.
```

**Example 2:**

```
**Input:** message = "short message", limit = 15
**Output:** ["short mess","age"]
**Explanation:**
Under the given constraints, the string can be split into two parts:
- The first part comprises of the first 10 characters, and has a length 15.
- The next part comprises of the last 3 characters, and has a length 8.
```

**Constraints:**

- `1 <= message.length <= 10^{4}`

	- `message` consists only of lowercase English letters and `' '`.

	- `1 <= limit <= 10^{4}`

### Hints

1. Could you solve the problem if you knew how many digits the total number of parts has?
2. Try all possible lengths of the total number of parts, and see if the string can be split such that the total number of parts has that length.
3. Binary search can be used for each part length to find the precise number of parts needed.

## Approach

<!-- Describe your solution approach here -->

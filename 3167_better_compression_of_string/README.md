# 3167. Better Compression of String

- **Difficulty:** Medium
- **LeetCode:** [https://leetcode.com/problems/better-compression-of-string/](https://leetcode.com/problems/better-compression-of-string/)
- **Premium:** Yes
- **Tags:** hash-table, string, sorting, counting

## Problem

You are given a string `compressed` representing a compressed version of a string. The format is a character followed by its frequency. For example, `"a3b1a1c2"` is a compressed version of the string `"aaabacc"`.

We seek a **better compression** with the following conditions:

	- Each character should appear **only once** in the compressed version.

	- The characters should be in **alphabetical order**.

Return the *better compression* of `compressed`.

**Note:** In the better version of compression, the order of letters may change, which is acceptable.



**Example 1:**

**Input:** compressed = "a3c9b2c1"

**Output:** "a3b2c10"

**Explanation:**

Characters "a" and "b" appear only once in the input, but "c" appears twice, once with a size of 9 and once with a size of 1.

Hence, in the resulting string, it should have a size of 10.

**Example 2:**

**Input:** compressed = "c2b3a1"

**Output:** "a1b3c2"

**Example 3:**

**Input:** compressed = "a2b4c1"

**Output:** "a2b4c1"



**Constraints:**

	- `1 <= compressed.length <= 6 * 10^{4}`

	- `compressed` consists only of lowercase English letters and digits.

	- `compressed` is a valid compression, i.e., each character is followed by its frequency.

	- Frequencies are in the range `[1, 10^{4}]` and have no leading zeroes.

---
_Problem text from the [doocs/leetcode](https://github.com/doocs/leetcode) community mirror (LeetCode Premium)._

### Hints

1. This is an implementation problem.
2. Try to extract each character with its corresponding frequency.
3. Sum the frequencies for a single character.
4. Sort characters and append them to a string in alphabetical order.

## Approach

<!-- Describe your solution approach here -->

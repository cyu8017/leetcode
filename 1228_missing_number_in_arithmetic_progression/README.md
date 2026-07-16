# 1228. Missing Number In Arithmetic Progression

- **Difficulty:** Easy
- **LeetCode:** [https://leetcode.com/problems/missing-number-in-arithmetic-progression/](https://leetcode.com/problems/missing-number-in-arithmetic-progression/)
- **Premium:** Yes
- **Tags:** array, math

## Problem

In some array `arr`, the values were in arithmetic progression: the values `arr[i + 1] - arr[i]` are all equal for every `0 <= i < arr.length - 1`.

A value from `arr` was removed that **was not the first or last value in the array**.

Given `arr`, return *the removed value*.



**Example 1:**

**Input:** arr = [5,7,11,13]
**Output:** 9
**Explanation:** The previous array was [5,7,**9**,11,13].

**Example 2:**

**Input:** arr = [15,13,12]
**Output:** 14
**Explanation:** The previous array was [15,**14**,13,12].



**Constraints:**

	- `3 <= arr.length <= 1000`

	- `0 <= arr[i] <= 10^{5}`

	- The given array is **guaranteed** to be a valid array.

---
_Problem text from the [doocs/leetcode](https://github.com/doocs/leetcode) community mirror (LeetCode Premium)._

### Hints

1. Assume the sequence is increasing, what if we find the largest consecutive difference?
2. Is the missing element in the middle of the segment with the largest consecutive difference?
3. For decreasing sequences, just reverse the array and do a similar process.

## Approach

<!-- Describe your solution approach here -->

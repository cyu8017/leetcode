# 2505. Bitwise OR of All Subsequence Sums

- **Difficulty:** Medium
- **LeetCode:** [https://leetcode.com/problems/bitwise-or-of-all-subsequence-sums/](https://leetcode.com/problems/bitwise-or-of-all-subsequence-sums/)
- **Premium:** Yes
- **Tags:** array, math, bit-manipulation, brainteaser, prefix-sum

## Problem

Given an integer array `nums`, return *the value of the bitwise ***OR*** of the sum of all possible **subsequences** in the array*.

A **subsequence** is a sequence that can be derived from another sequence by removing zero or more elements without changing the order of the remaining elements.



**Example 1:**

**Input:** nums = [2,1,0,3]
**Output:** 7
**Explanation:** All possible subsequence sums that we can have are: 0, 1, 2, 3, 4, 5, 6.
And we have 0 OR 1 OR 2 OR 3 OR 4 OR 5 OR 6 = 7, so we return 7.

**Example 2:**

**Input:** nums = [0,0,0]
**Output:** 0
**Explanation:** 0 is the only possible subsequence sum we can have, so we return 0.



**Constraints:**

	- `1 <= nums.length <= 10^{5}`

	- `0 <= nums[i] <= 10^{9}`

---
_Problem text from the [doocs/leetcode](https://github.com/doocs/leetcode) community mirror (LeetCode Premium)._

### Hints

1. Think of each bit separately, i.e. try to figure out if `i^{th}` bit is set in the answer.
2. `i^{th}` bit is set in the answer if it's set in one of the array elements or it can be made using some of them.
3. Try to sum up lower bits and make higher bits.

## Approach

<!-- Describe your solution approach here -->

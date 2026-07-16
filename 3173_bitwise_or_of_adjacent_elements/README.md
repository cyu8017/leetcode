# 3173. Bitwise OR of Adjacent Elements

- **Difficulty:** Easy
- **LeetCode:** [https://leetcode.com/problems/bitwise-or-of-adjacent-elements/](https://leetcode.com/problems/bitwise-or-of-adjacent-elements/)
- **Premium:** Yes
- **Tags:** array, bit-manipulation

## Problem

Given an array `nums` of length `n`, return an array `answer` of length `n - 1` such that `answer[i] = nums[i] | nums[i + 1]` where `|` is the bitwise `OR` operation.



**Example 1:**

**Input:** nums = [1,3,7,15]

**Output:** [3,7,15]

**Example 2:**

**Input:** nums = [8,4,2]

**Output:** [12,6]

**Example 3:**

**Input:** nums = [5,4,9,11]

**Output:** [5,13,11]



**Constraints:**

	- `2 <= nums.length <= 100`

	- `0 <= nums[i] <= 100`

---
_Problem text from the [doocs/leetcode](https://github.com/doocs/leetcode) community mirror (LeetCode Premium)._

### Hints

1. Iterate over array and calculate each element of the resulting array using `|` operation.

## Approach

<!-- Describe your solution approach here -->

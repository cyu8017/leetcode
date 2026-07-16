# 1133. Largest Unique Number

- **Difficulty:** Easy
- **LeetCode:** [https://leetcode.com/problems/largest-unique-number/](https://leetcode.com/problems/largest-unique-number/)
- **Premium:** Yes
- **Tags:** array, hash-table, sorting

## Problem

Given an integer array `nums`, return *the largest integer that only occurs once*. If no integer occurs once, return `-1`.



**Example 1:**

**Input:** nums = [5,7,3,9,4,9,8,3,1]
**Output:** 8
**Explanation:** The maximum integer in the array is 9 but it is repeated. The number 8 occurs only once, so it is the answer.

**Example 2:**

**Input:** nums = [9,9,8,8]
**Output:** -1
**Explanation:** There is no number that occurs only once.



**Constraints:**

	- `1 <= nums.length <= 2000`

	- `0 <= nums[i] <= 1000`

---
_Problem text from the [doocs/leetcode](https://github.com/doocs/leetcode) community mirror (LeetCode Premium)._

### Hints

1. Find the number of occurrences of each value.
2. Use an array or a hash table to do that.
3. Look for the largest value with number of occurrences = 1.

## Approach

<!-- Describe your solution approach here -->

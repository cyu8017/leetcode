# 1426. Counting Elements

- **Difficulty:** Easy
- **LeetCode:** [https://leetcode.com/problems/counting-elements/](https://leetcode.com/problems/counting-elements/)
- **Premium:** Yes
- **Tags:** array, hash-table

## Problem

Given an integer array `arr`, count how many elements `x` there are, such that `x + 1` is also in `arr`. If there are duplicates in `arr`, count them separately.



**Example 1:**

**Input:** arr = [1,2,3]
**Output:** 2
**Explanation:** 1 and 2 are counted cause 2 and 3 are in arr.

**Example 2:**

**Input:** arr = [1,1,3,3,5,5,7,7]
**Output:** 0
**Explanation:** No numbers are counted, cause there is no 2, 4, 6, or 8 in arr.



**Constraints:**

	- `1 <= arr.length <= 1000`

	- `0 <= arr[i] <= 1000`

---
_Problem text from the [doocs/leetcode](https://github.com/doocs/leetcode) community mirror (LeetCode Premium)._

### Hints

1. Use hashset to store all elements.
2. Loop again to count all valid elements.

## Approach

<!-- Describe your solution approach here -->

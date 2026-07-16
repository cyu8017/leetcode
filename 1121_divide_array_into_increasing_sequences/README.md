# 1121. Divide Array Into Increasing Sequences

- **Difficulty:** Hard
- **LeetCode:** [https://leetcode.com/problems/divide-array-into-increasing-sequences/](https://leetcode.com/problems/divide-array-into-increasing-sequences/)
- **Premium:** Yes
- **Tags:** array, counting

## Problem

Given an integer array `nums` sorted in non-decreasing order and an integer `k`, return `true`* if this array can be divided into one or more disjoint increasing subsequences of length at least *`k`*, or *`false`* otherwise*.



**Example 1:**

**Input:** nums = [1,2,2,3,3,4,4], k = 3
**Output:** true
**Explanation:** The array can be divided into two subsequences [1,2,3,4] and [2,3,4] with lengths at least 3 each.

**Example 2:**

**Input:** nums = [5,6,6,7,8], k = 3
**Output:** false
**Explanation:** There is no way to divide the array using the conditions required.



**Constraints:**

	- `1 <= k <= nums.length <= 10^{5}`

	- `1 <= nums[i] <= 10^{5}`

	- `nums` is sorted in non-decreasing order.

---
_Problem text from the [doocs/leetcode](https://github.com/doocs/leetcode) community mirror (LeetCode Premium)._

### Hints

1. Think in the frequency of the numbers and how this affects the number of sequences needed.
2. What is the minimum number of sequences we need to form? Considering frequency of the numbers.
3. Think about the least number of sequences to maximize the lengths.
4. The number of sequences needed is equal to the maximum frequency of an element.
5. How to put the other elements into sequences ? Think in a greedy approach.

## Approach

<!-- Describe your solution approach here -->

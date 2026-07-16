# 1060. Missing Element in Sorted Array

- **Difficulty:** Medium
- **LeetCode:** [https://leetcode.com/problems/missing-element-in-sorted-array/](https://leetcode.com/problems/missing-element-in-sorted-array/)
- **Premium:** Yes
- **Tags:** array, binary-search

## Problem

Given an integer array `nums` which is sorted in **ascending order** and all of its elements are **unique** and given also an integer `k`, return the `k^{th}` missing number starting from the leftmost number of the array.



**Example 1:**

**Input:** nums = [4,7,9,10], k = 1
**Output:** 5
**Explanation:** The first missing number is 5.

**Example 2:**

**Input:** nums = [4,7,9,10], k = 3
**Output:** 8
**Explanation:** The missing numbers are [5,6,8,...], hence the third missing number is 8.

**Example 3:**

**Input:** nums = [1,2,4], k = 3
**Output:** 6
**Explanation:** The missing numbers are [3,5,6,7,...], hence the third missing number is 6.



**Constraints:**

	- `1 <= nums.length <= 5 * 10^{4}`

	- `1 <= nums[i] <= 10^{7}`

	- `nums` is sorted in **ascending order,** and all the elements are **unique**.

	- `1 <= k <= 10^{8}`



**Follow up:** Can you find a logarithmic time complexity (i.e., `O(log(n))`) solution?

---
_Problem text from the [doocs/leetcode](https://github.com/doocs/leetcode) community mirror (LeetCode Premium)._

### Hints

1. First define a function f(x) that counts the number of missing elements until x.
2. Then use binary search with the given function f(x) to find the kth missing element.

## Approach

<!-- Describe your solution approach here -->

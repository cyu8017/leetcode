# 2098. Subsequence of Size K With the Largest Even Sum

- **Difficulty:** Medium
- **LeetCode:** [https://leetcode.com/problems/subsequence-of-size-k-with-the-largest-even-sum/](https://leetcode.com/problems/subsequence-of-size-k-with-the-largest-even-sum/)
- **Premium:** Yes
- **Tags:** array, greedy, sorting

## Problem

You are given an integer array `nums` and an integer `k`. Find the **largest even sum** of any subsequence of `nums` that has a length of `k`.

Return *this sum, or *`-1`* if such a sum does not exist*.

A **subsequence** is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.



**Example 1:**

**Input:** nums = [4,1,5,3,1], k = 3
**Output:** 12
**Explanation:**
The subsequence with the largest possible even sum is [4,5,3]. It has a sum of 4 + 5 + 3 = 12.

**Example 2:**

**Input:** nums = [4,6,2], k = 3
**Output:** 12
**Explanation:**
The subsequence with the largest possible even sum is [4,6,2]. It has a sum of 4 + 6 + 2 = 12.

**Example 3:**

**Input:** nums = [1,3,5], k = 1
**Output:** -1
**Explanation:**
No subsequence of nums with length 1 has an even sum.



**Constraints:**

	- `1 <= nums.length <= 10^{5}`

	- `0 <= nums[i] <= 10^{5}`

	- `1 <= k <= nums.length`

---
_Problem text from the [doocs/leetcode](https://github.com/doocs/leetcode) community mirror (LeetCode Premium)._

### Hints

1. Is the sum of two even numbers even or odd? How about two odd numbers? One odd number and one even number?
2. If there is an even number of odd numbers, the sum will be even and vice versa.
3. Create an integer array to store all the even numbers in nums and another array to store all the odd numbers in nums. Sort both arrays.

## Approach

<!-- Describe your solution approach here -->

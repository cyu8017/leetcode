# 1150. Check If a Number Is Majority Element in a Sorted Array

- **Difficulty:** Easy
- **LeetCode:** [https://leetcode.com/problems/check-if-a-number-is-majority-element-in-a-sorted-array/](https://leetcode.com/problems/check-if-a-number-is-majority-element-in-a-sorted-array/)
- **Premium:** Yes
- **Tags:** array, binary-search

## Problem

Given an integer array `nums` sorted in non-decreasing order and an integer `target`, return `true` *if* `target` *is a **majority** element, or *`false`* otherwise*.

A **majority** element in an array `nums` is an element that appears more than `nums.length / 2` times in the array.



**Example 1:**

**Input:** nums = [2,4,5,5,5,5,5,6,6], target = 5
**Output:** true
**Explanation:** The value 5 appears 5 times and the length of the array is 9.
Thus, 5 is a majority element because 5 > 9/2 is true.

**Example 2:**

**Input:** nums = [10,100,101,101], target = 101
**Output:** false
**Explanation:** The value 101 appears 2 times and the length of the array is 4.
Thus, 101 is not a majority element because 2 > 4/2 is false.



**Constraints:**

	- `1 <= nums.length <= 1000`

	- `1 <= nums[i], target <= 10^{9}`

	- `nums` is sorted in non-decreasing order.

---
_Problem text from the [doocs/leetcode](https://github.com/doocs/leetcode) community mirror (LeetCode Premium)._

### Hints

1. How to check if a given number target is a majority element?.
2. Find the frequency of target and compare it to the length of the array.
3. You can find the frequency of an element using Binary Search since the array is sorted.
4. Using Binary Search, find the first and last occurrences of A. Then just calculate the difference between the indexes of these occurrences.

## Approach

<!-- Describe your solution approach here -->

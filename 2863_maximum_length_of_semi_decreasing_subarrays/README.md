# 2863. Maximum Length of Semi-Decreasing Subarrays

- **Difficulty:** Medium
- **LeetCode:** [https://leetcode.com/problems/maximum-length-of-semi-decreasing-subarrays/](https://leetcode.com/problems/maximum-length-of-semi-decreasing-subarrays/)
- **Premium:** Yes
- **Tags:** array, stack, sorting, monotonic-stack

## Problem

You are given an integer array `nums`.

Return *the length of the **longest semi-decreasing** subarray of *`nums`*, and *`0`* if there are no such subarrays.*

	- A **subarray** is a contiguous non-empty sequence of elements within an array.

	- A non-empty array is **semi-decreasing** if its first element is **strictly greater** than its last element.



**Example 1:**

**Input:** nums = [7,6,5,4,3,2,1,6,10,11]
**Output:** 8
**Explanation:** Take the subarray [7,6,5,4,3,2,1,6].
The first element is 7 and the last one is 6 so the condition is met.
Hence, the answer would be the length of the subarray or 8.
It can be shown that there aren't any subarrays with the given condition with a length greater than 8.

**Example 2:**

**Input:** nums = [57,55,50,60,61,58,63,59,64,60,63]
**Output:** 6
**Explanation:** Take the subarray [61,58,63,59,64,60].
The first element is 61 and the last one is 60 so the condition is met.
Hence, the answer would be the length of the subarray or 6.
It can be shown that there aren't any subarrays with the given condition with a length greater than 6.

**Example 3:**

**Input:** nums = [1,2,3,4]
**Output:** 0
**Explanation:** Since there are no semi-decreasing subarrays in the given array, the answer is 0.



**Constraints:**

	- `1 <= nums.length <= 10^{5}`

	- `-10^{9} <= nums[i] <= 10^{9}`

---
_Problem text from the [doocs/leetcode](https://github.com/doocs/leetcode) community mirror (LeetCode Premium)._

### Hints

1. First, solve the problem assuming `nums` contains distinct values.
2. Make a new array with each element being the pair `(nums[i], i)` for every `i` and call it `num_ind`.
3. Sort `num_ind` in decreasing order.
4. Iterate over `num_ind` and store a variable that represents the minimum index (i.e. min of `num_ind[i].second`) that has been iterated until now. Call it `min_index`
5. Now if you are currently on pair `(nums[x], x)`, then `ans = max(ans, min_index - x)`.
6. Now try to remove the first assumption.

## Approach

<!-- Describe your solution approach here -->

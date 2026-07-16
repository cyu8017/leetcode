# 2263. Make Array Non-decreasing or Non-increasing

- **Difficulty:** Hard
- **LeetCode:** [https://leetcode.com/problems/make-array-non-decreasing-or-non-increasing/](https://leetcode.com/problems/make-array-non-decreasing-or-non-increasing/)
- **Premium:** Yes
- **Tags:** array, dynamic-programming, greedy, heap-(priority-queue)

## Problem

You are given a **0-indexed** integer array `nums`. In one operation, you can:

	- Choose an index `i` in the range `0 <= i < nums.length`

	- Set `nums[i]` to `nums[i] + 1` **or** `nums[i] - 1`

Return *the **minimum** number of operations to make *`nums`* **non-decreasing** or **non-increasing**.*



**Example 1:**

**Input:** nums = [3,2,4,5,0]
**Output:** 4
**Explanation:**
One possible way to turn nums into non-increasing order is to:
- Add 1 to nums[1] once so that it becomes 3.
- Subtract 1 from nums[2] once so it becomes 3.
- Subtract 1 from nums[3] twice so it becomes 3.
After doing the 4 operations, nums becomes [3,3,3,3,0] which is in non-increasing order.
Note that it is also possible to turn nums into [4,4,4,4,0] in 4 operations.
It can be proven that 4 is the minimum number of operations needed.

**Example 2:**

**Input:** nums = [2,2,3,4]
**Output:** 0
**Explanation:** nums is already in non-decreasing order, so no operations are needed and we return 0.

**Example 3:**

**Input:** nums = [0]
**Output:** 0
**Explanation:** nums is already in non-decreasing order, so no operations are needed and we return 0.



**Constraints:**

	- `1 <= nums.length <= 1000`

	- `0 <= nums[i] <= 1000`



**Follow up:** Can you solve it in `O(n*log(n))` time complexity?

---
_Problem text from the [doocs/leetcode](https://github.com/doocs/leetcode) community mirror (LeetCode Premium)._

### Hints

1. To find the minimum cost to make nums non-decreasing, use a max heap that contains all of the elements that you have seen so far.
2. If the largest number in the heap is greater than the current number, calculate the cost to make the two numbers equal. Then, in the heap, replace the largest number with the current number.
3. Now that we have found the minimum cost to make nums non-decreasing, we can set every nums[i] to -nums[i] and do the same process to find the minimum cost to make nums non-increasing.

## Approach

<!-- Describe your solution approach here -->

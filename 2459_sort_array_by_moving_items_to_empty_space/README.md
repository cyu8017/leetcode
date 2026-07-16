# 2459. Sort Array by Moving Items to Empty Space

- **Difficulty:** Hard
- **LeetCode:** [https://leetcode.com/problems/sort-array-by-moving-items-to-empty-space/](https://leetcode.com/problems/sort-array-by-moving-items-to-empty-space/)
- **Premium:** Yes
- **Tags:** array, hash-table, sorting

## Problem

You are given an integer array `nums` of size `n` containing **each** element from `0` to `n - 1` (**inclusive**). Each of the elements from `1` to `n - 1` represents an item, and the element `0` represents an empty space.

In one operation, you can move **any** item to the empty space. `nums` is considered to be sorted if the numbers of all the items are in **ascending** order and the empty space is either at the beginning or at the end of the array.

For example, if `n = 4`, `nums` is sorted if:

	- `nums = [0,1,2,3]` or

	- `nums = [1,2,3,0]`

...and considered to be unsorted otherwise.

Return *the **minimum** number of operations needed to sort *`nums`.



**Example 1:**

**Input:** nums = [4,2,0,3,1]
**Output:** 3
**Explanation:**
- Move item 2 to the empty space. Now, nums = [4,0,2,3,1].
- Move item 1 to the empty space. Now, nums = [4,1,2,3,0].
- Move item 4 to the empty space. Now, nums = [0,1,2,3,4].
It can be proven that 3 is the minimum number of operations needed.

**Example 2:**

**Input:** nums = [1,2,3,4,0]
**Output:** 0
**Explanation:** nums is already sorted so return 0.

**Example 3:**

**Input:** nums = [1,0,2,4,3]
**Output:** 2
**Explanation:**
- Move item 2 to the empty space. Now, nums = [1,2,0,4,3].
- Move item 3 to the empty space. Now, nums = [1,2,3,4,0].
It can be proven that 2 is the minimum number of operations needed.



**Constraints:**

	- `n == nums.length`

	- `2 <= n <= 10^{5}`

	- `0 <= nums[i] < n`

	- All the values of `nums` are **unique**.

---
_Problem text from the [doocs/leetcode](https://github.com/doocs/leetcode) community mirror (LeetCode Premium)._

### Hints

1. There are two possibilities for nums to be sorted. Find the minimum number of operations needed for the first possibility, then find the minimum number of operations needed for the second possibility. The answer is the minimum out of the two.
2. If the empty space is not at its ending position, then you can move the item that should be where the empty space is to the empty space.
3. If the empty space is at its ending position, then you need to move an out-of-place item to the empty space.

## Approach

<!-- Describe your solution approach here -->

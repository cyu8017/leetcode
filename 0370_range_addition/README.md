# 0370. Range Addition

- **Difficulty:** Medium
- **LeetCode:** [https://leetcode.com/problems/range-addition/](https://leetcode.com/problems/range-addition/)
- **Premium:** Yes
- **Tags:** array, prefix-sum

## Problem

You are given an integer `length` and an array `updates` where `updates[i] = [startIdx_{i}, endIdx_{i}, inc_{i}]`.

You have an array `arr` of length `length` with all zeros, and you have some operation to apply on `arr`. In the `i^{th}` operation, you should increment all the elements `arr[startIdx_{i}], arr[startIdx_{i} + 1], ..., arr[endIdx_{i}]` by `inc_{i}`.

Return `arr` *after applying all the* `updates`.



**Example 1:**

**Input:** length = 5, updates = [[1,3,2],[2,4,3],[0,2,-2]]
**Output:** [-2,0,3,5,3]

**Example 2:**

**Input:** length = 10, updates = [[2,4,6],[5,6,8],[1,9,-4]]
**Output:** [0,-4,2,2,2,4,4,-4,-4,-4]



**Constraints:**

	- `1 <= length <= 10^{5}`

	- `0 <= updates.length <= 10^{4}`

	- `0 <= startIdx_{i} <= endIdx_{i} < length`

	- `-1000 <= inc_{i} <= 1000`

---
_Problem text from the [doocs/leetcode](https://github.com/doocs/leetcode) community mirror (LeetCode Premium)._

### Hints

1. Thinking of using advanced data structures? You are thinking it too complicated.
2. For each update operation, do you really need to update all elements between i and j?
3. Update only the first and end element is sufficient.
4. The optimal time complexity is O(**k** + **n**) and uses O(1) extra space.

## Approach

<!-- Describe your solution approach here -->

# 2046. Sort Linked List Already Sorted Using Absolute Values

- **Difficulty:** Medium
- **LeetCode:** [https://leetcode.com/problems/sort-linked-list-already-sorted-using-absolute-values/](https://leetcode.com/problems/sort-linked-list-already-sorted-using-absolute-values/)
- **Premium:** Yes
- **Tags:** linked-list, two-pointers, sorting

## Problem

Given the `head` of a singly linked list that is sorted in **non-decreasing** order using the **absolute values** of its nodes, return *the list sorted in **non-decreasing** order using the **actual values** of its nodes*.



**Example 1:**

**Input:** head = [0,2,-5,5,10,-10]
**Output:** [-10,-5,0,2,5,10]
**Explanation:**
The list sorted in non-descending order using the absolute values of the nodes is [0,2,-5,5,10,-10].
The list sorted in non-descending order using the actual values is [-10,-5,0,2,5,10].

**Example 2:**

**Input:** head = [0,1,2]
**Output:** [0,1,2]
**Explanation:**
The linked list is already sorted in non-decreasing order.

**Example 3:**

**Input:** head = [1]
**Output:** [1]
**Explanation:**
The linked list is already sorted in non-decreasing order.



**Constraints:**

	- The number of nodes in the list is the range `[1, 10^{5}]`.

	- `-5000 <= Node.val <= 5000`

	- `head` is sorted in non-decreasing order using the absolute value of its nodes.



**Follow up:**

	- Can you think of a solution with `O(n)` time complexity?

---
_Problem text from the [doocs/leetcode](https://github.com/doocs/leetcode) community mirror (LeetCode Premium)._

### Hints

1. The nodes with positive values are already in the correct order.
2. Nodes with negative values need to be moved to the front.
3. Nodes with negative values are in reversed order.

## Approach

<!-- Describe your solution approach here -->

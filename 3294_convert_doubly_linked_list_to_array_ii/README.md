# 3294. Convert Doubly Linked List to Array II

- **Difficulty:** Medium
- **LeetCode:** [https://leetcode.com/problems/convert-doubly-linked-list-to-array-ii/](https://leetcode.com/problems/convert-doubly-linked-list-to-array-ii/)
- **Premium:** Yes
- **Tags:** array, linked-list, doubly-linked-list

## Problem

You are given an **arbitrary** `node` from a **doubly linked list**, which contains nodes that have a next pointer and a previous pointer.

Return an integer array which contains the elements of the linked list **in order**.



**Example 1:**

**Input:** head = [1,2,3,4,5], node = 5

**Output:** [1,2,3,4,5]

**Example 2:**

**Input:** head = [4,5,6,7,8], node = 8

**Output:** [4,5,6,7,8]



**Constraints:**

	- The number of nodes in the given list is in the range `[1, 500]`.

	- `1 <= Node.val <= 1000`

	- All nodes have unique `Node.val`.

---
_Problem text from the [doocs/leetcode](https://github.com/doocs/leetcode) community mirror (LeetCode Premium)._

### Hints

1. Use the pointer to the previous node to reach the `head` node.

## Approach

<!-- Describe your solution approach here -->

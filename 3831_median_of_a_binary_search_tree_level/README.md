# 3831. Median of a Binary Search Tree Level

- **Difficulty:** Medium
- **LeetCode:** [https://leetcode.com/problems/median-of-a-binary-search-tree-level/](https://leetcode.com/problems/median-of-a-binary-search-tree-level/)
- **Premium:** Yes
- **Tags:** tree, depth-first-search, breadth-first-search, binary-search-tree, binary-tree

## Problem

You are given the `root` of a **Binary Search Tree (BST)** and an integer `level`.

The root node is at level 0. Each level represents the distance from the root.

Return the **median value** of all node values present at the given `level`. If the level does not exist or contains no nodes, return -1.

The **median** is defined as the middle element after sorting the values at that level in **non-decreasing** order. If the number of values at that level is even, return the **upper** median (the larger of the two middle elements after sorting).



**Example 1:**

**Input:** root = [4,null,5,null,7], level = 2

**Output:** 7

**Explanation:**

The nodes at `level = 2` are `[7]`. The median value is 7.

**Example 2:**

**Input:** root = [6,3,8], level = 1

**Output:** 8

**Explanation:**

The nodes at `level = 1` are `[3, 8]`. There are two possible median values, so the larger one 8 is the answer.

**Example 3:**

**​​​​​​​​​​​​​​**

**Input:** root = [2,1], level = 2

**Output:** -1

**Explanation:**

There is no node present at `level = 2`​​​​​​​, so the answer is -1.



**Constraints:**

	- The number of nodes in the tree is in the range `[1, 2 * 10^{5}]`.

	- `1 <= Node.val <= 10^{6}`

	- `0 <= level <= 2 * 10^{​​​​​​​5}`

---
_Problem text from the [doocs/leetcode](https://github.com/doocs/leetcode) community mirror (LeetCode Premium)._

### Hints

1. Use DFS or BFS to gather the node values at `level`.
2. Sort the values at that level; if the list is empty, return -1, otherwise return the upper median.

## Approach

<!-- Describe your solution approach here -->

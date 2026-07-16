# 1602. Find Nearest Right Node in Binary Tree

- **Difficulty:** Medium
- **LeetCode:** [https://leetcode.com/problems/find-nearest-right-node-in-binary-tree/](https://leetcode.com/problems/find-nearest-right-node-in-binary-tree/)
- **Premium:** Yes
- **Tags:** tree, breadth-first-search, binary-tree

## Problem

Given the `root` of a binary tree and a node `u` in the tree, return *the **nearest** node on the **same level** that is to the **right** of* `u`*, or return* `null` *if *`u` *is the rightmost node in its level*.



**Example 1:**

**Input:** root = [1,2,3,null,4,5,6], u = 4
**Output:** 5
**Explanation:** The nearest node on the same level to the right of node 4 is node 5.

**Example 2:**

**Input:** root = [3,null,4,2], u = 2
**Output:** null
**Explanation:** There are no nodes to the right of 2.



**Constraints:**

	- The number of nodes in the tree is in the range `[1, 10^{5}]`.

	- `1 <= Node.val <= 10^{5}`

	- All values in the tree are **distinct**.

	- `u` is a node in the binary tree rooted at `root`.

---
_Problem text from the [doocs/leetcode](https://github.com/doocs/leetcode) community mirror (LeetCode Premium)._

### Hints

1. Use BFS, traverse the tree level by level and always push the left node first
2. When you reach the target node, mark  a boolean variable true
3. If you meet another node in the same level after marking the boolean true, return this node.
4. If you did not meet new nodes in the same level and started traversing a new level, return Null

## Approach

<!-- Describe your solution approach here -->

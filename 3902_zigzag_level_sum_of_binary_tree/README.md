# 3902. Zigzag Level Sum of Binary Tree

- **Difficulty:** Medium
- **LeetCode:** [https://leetcode.com/problems/zigzag-level-sum-of-binary-tree/](https://leetcode.com/problems/zigzag-level-sum-of-binary-tree/)
- **Premium:** Yes
- **Tags:** tree, breadth-first-search, binary-tree

## Problem

You are given the `root` of a **binary tree**.

Traverse the tree level by level using a zigzag pattern:

	- At **odd**-numbered levels (1-indexed), traverse nodes from **left to right**.

	- At **even**-numbered levels, traverse nodes from **right to left**.

While traversing a level in the specified direction, process nodes in order and **stop** immediately before the first node that violates the condition:

	- At **odd** levels: the node does not have a **left** child.

	- At **even** levels: the node does not have a **right** child.

Only the nodes processed before this stopping condition contribute to the level sum.

Return an integer array `ans` where `ans[i]` is the **sum** of the node values that are processed at level `i + 1`.



**Example 1:**

**Input:** root = [5,2,8,1,null,9,6]

**Output:** [5,8,0]

**Explanation:**

​​​​​​​

	- At level 1, nodes are processed left to right. Node 5 is included, thus `ans[0] = 5`.

	- At level 2, nodes are processed right to left. Node 8 is included, but node 2 lacks a right child, so processing stops, thus `ans[1] = 8`.

	- At level 3, nodes are processed left to right. The first node 1 lacks a left child, so no nodes are included, and `ans[2] = 0`.

	- Thus, `ans = [5, 8, 0]`.

**Example 2:**

**Input:** root = [1,2,3,4,5,null,7]

**Output:** [1,5,0]

**Explanation:**

	- At level 1, nodes are processed left to right. Node 1 is included, thus `ans[0] = 1`.

	- At level 2, nodes are processed right to left. Nodes 3 and 2 are included since both have right children, thus `ans[1] = 3 + 2 = 5`.

	- At level 3, nodes are processed left to right. The first node 4 lacks a left child, so no nodes are included, and `ans[2] = 0`.

	- Thus, `ans = [1, 5, 0]`.



**Constraints:**

	- The number of nodes in the tree is in the range `[1, 10^{5}]`.

	- `-10^{5} <= Node.val <= 10^{5}`

---
_Problem text from the [doocs/leetcode](https://github.com/doocs/leetcode) community mirror (LeetCode Premium)._

### Hints

1. Use level-order traversal (`BFS`) to process the tree level by level
2. Maintain a list (or queue) of nodes for the current level
3. Alternate traversal direction using a flag (odd level vs even level)

## Approach

<!-- Describe your solution approach here -->

# 1676. Lowest Common Ancestor of a Binary Tree IV

- **Difficulty:** Medium
- **LeetCode:** [https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iv/](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iv/)
- **Premium:** Yes
- **Tags:** hash-table, tree, depth-first-search, binary-tree

## Problem

Given the `root` of a binary tree and an array of `TreeNode` objects `nodes`, return *the lowest common ancestor (LCA) of **all the nodes** in *`nodes`. All the nodes will exist in the tree, and all values of the tree's nodes are **unique**.

Extending the **definition of LCA on Wikipedia**: "The lowest common ancestor of `n` nodes `p_{1}`, `p_{2}`, ..., `p_{n}` in a binary tree `T` is the lowest node that has every `p_{i}` as a **descendant** (where we allow **a node to be a descendant of itself**) for every valid `i`". A **descendant** of a node `x` is a node `y` that is on the path from node `x` to some leaf node.



**Example 1:**

**Input:** root = [3,5,1,6,2,0,8,null,null,7,4], nodes = [4,7]
**Output:** 2
**Explanation:** The lowest common ancestor of nodes 4 and 7 is node 2.

**Example 2:**

**Input:** root = [3,5,1,6,2,0,8,null,null,7,4], nodes = [1]
**Output:** 1
**Explanation:** The lowest common ancestor of a single node is the node itself.

**Example 3:**

**Input:** root = [3,5,1,6,2,0,8,null,null,7,4], nodes = [7,6,2,4]
**Output:** 5
**Explanation:** The lowest common ancestor of the nodes 7, 6, 2, and 4 is node 5.



**Constraints:**

	- The number of nodes in the tree is in the range `[1, 10^{4}]`.

	- `-10^{9} <= Node.val <= 10^{9}`

	- All `Node.val` are **unique**.

	- All `nodes[i]` will exist in the tree.

	- All `nodes[i]` are distinct.

---
_Problem text from the [doocs/leetcode](https://github.com/doocs/leetcode) community mirror (LeetCode Premium)._

### Hints

1. Starting from the root, traverse the left and the right subtrees, checking if one of the nodes exist there.
2. If one of the subtrees doesn't contain any given node, the LCA can be the node returned from the other subtree
3. If both subtrees contain nodes, the LCA node is the current node.

## Approach

<!-- Describe your solution approach here -->

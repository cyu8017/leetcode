# 2196. Create Binary Tree From Descriptions

- **Difficulty:** Medium
- **LeetCode:** [https://leetcode.com/problems/create-binary-tree-from-descriptions/](https://leetcode.com/problems/create-binary-tree-from-descriptions/)
- **Tags:** array, hash-table, tree, binary-tree

## Problem

You are given a 2D integer array `descriptions` where `descriptions[i] = [parent_{i}, child_{i}, isLeft_{i}]` indicates that `parent_{i}` is the **parent** of `child_{i}` in a **binary** tree of **unique** values. Furthermore,

- If `isLeft_{i} == 1`, then `child_{i}` is the left child of `parent_{i}`.

	- If `isLeft_{i} == 0`, then `child_{i}` is the right child of `parent_{i}`.

Construct the binary tree described by `descriptions` and return *its **root**.

The test cases will be generated such that the binary tree is **valid**.

**Example 1:**

```
**Input:** descriptions = [[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]]
**Output:** [50,20,80,15,17,19]
**Explanation:** The root node is the node with value 50 since it has no parent.
The resulting binary tree is shown in the diagram.
```

**Example 2:**

```
**Input:** descriptions = [[1,2,1],[2,3,0],[3,4,1]]
**Output:** [1,2,null,null,3,4]
**Explanation:** The root node is the node with value 1 since it has no parent.
The resulting binary tree is shown in the diagram.
```

**Constraints:**

- `1 <= descriptions.length <= 10^{4}`

	- `descriptions[i].length == 3`

	- `1 <= parent_{i}, child_{i} <= 10^{5}`

	- `0 <= isLeft_{i} <= 1`

	- The binary tree described by `descriptions` is valid.

### Hints

1. Could you represent and store the descriptions more efficiently?
2. Could you find the root node?
3. The node that is not a child in any of the descriptions is the root node.

## Approach

<!-- Describe your solution approach here -->

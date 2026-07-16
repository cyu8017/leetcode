# 1273. Delete Tree Nodes

- **Difficulty:** Medium
- **LeetCode:** [https://leetcode.com/problems/delete-tree-nodes/](https://leetcode.com/problems/delete-tree-nodes/)
- **Premium:** Yes
- **Tags:** array, tree, depth-first-search, breadth-first-search

## Problem

A tree rooted at node 0 is given as follows:

	- The number of nodes is `nodes`;

	- The value of the `i^{th}` node is `value[i]`;

	- The parent of the `i^{th}` node is `parent[i]`.

Remove every subtree whose sum of values of nodes is zero.

Return *the number of the remaining nodes in the tree*.



**Example 1:**

**Input:** nodes = 7, parent = [-1,0,0,1,2,2,2], value = [1,-2,4,0,-2,-1,-1]
**Output:** 2

**Example 2:**

**Input:** nodes = 7, parent = [-1,0,0,1,2,2,2], value = [1,-2,4,0,-2,-1,-2]
**Output:** 6



**Constraints:**

	- `1 <= nodes <= 10^{4}`

	- `parent.length == nodes`

	- `0 <= parent[i] <= nodes - 1`

	- `parent[0] == -1` which indicates that `0` is the root.

	- `value.length == nodes`

	- `-10^{5} <= value[i] <= 10^{5}`

	- The given input is **guaranteed** to represent a **valid tree**.

---
_Problem text from the [doocs/leetcode](https://github.com/doocs/leetcode) community mirror (LeetCode Premium)._

### Hints

1. Traverse the tree using depth first search.
2. Find for every node the sum of values of its sub-tree.
3. Traverse the tree again from the root and return once you reach a node with zero sum of values in its sub-tree.

## Approach

<!-- Describe your solution approach here -->

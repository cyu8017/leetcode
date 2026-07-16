# 3157. Find the Level of Tree with Minimum Sum

- **Difficulty:** Medium
- **LeetCode:** [https://leetcode.com/problems/find-the-level-of-tree-with-minimum-sum/](https://leetcode.com/problems/find-the-level-of-tree-with-minimum-sum/)
- **Premium:** Yes
- **Tags:** tree, depth-first-search, breadth-first-search, binary-tree

## Problem

Given the root of a binary tree `root` where each node has a value, return the level of the tree that has the **minimum** sum of values among all the levels (in case of a tie, return the **lowest** level).

**Note** that the root of the tree is at level 1 and the level of any other node is its distance from the root + 1.



**Example 1:**

**Input:** root = [50,6,2,30,80,7]

**Output:** 2

**Explanation:**

**Example 2:**

**Input:** root = [36,17,10,null,null,24]

**Output:** 3

**Explanation:**

**Example 3:**

**Input:** root = [5,null,5,null,5]

**Output:** 1

**Explanation:**



**Constraints:**

	- The number of nodes in the tree is in the range `[1, 10^{5}]`.

	- `1 <= Node.val <= 10^{9}`

---
_Problem text from the [doocs/leetcode](https://github.com/doocs/leetcode) community mirror (LeetCode Premium)._

### Hints

1. Run a DFS on the tree and update an array sum where sum[i] is the sum for level i.
2. The answer is the first minimum element of sum.

## Approach

<!-- Describe your solution approach here -->

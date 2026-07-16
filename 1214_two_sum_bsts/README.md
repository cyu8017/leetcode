# 1214. Two Sum BSTs

- **Difficulty:** Medium
- **LeetCode:** [https://leetcode.com/problems/two-sum-bsts/](https://leetcode.com/problems/two-sum-bsts/)
- **Premium:** Yes
- **Tags:** two-pointers, binary-search, stack, tree, depth-first-search, binary-search-tree, binary-tree

## Problem

Given the roots of two binary search trees, `root1` and `root2`, return `true` if and only if there is a node in the first tree and a node in the second tree whose values sum up to a given integer `target`.



**Example 1:**

**Input:** root1 = [2,1,4], root2 = [1,0,3], target = 5
**Output:** true
**Explanation: **2 and 3 sum up to 5.

**Example 2:**

**Input:** root1 = [0,-10,10], root2 = [5,1,7,0,2], target = 18
**Output:** false



**Constraints:**

	- The number of nodes in each tree is in the range `[1, 5000]`.

	- `-10^{9} <= Node.val, target <= 10^{9}`

---
_Problem text from the [doocs/leetcode](https://github.com/doocs/leetcode) community mirror (LeetCode Premium)._

### Hints

1. How can you reduce this problem to the classical Two Sum problem?
2. Do an in-order traversal of each tree to convert them to sorted arrays.
3. Solve the classical Two Sum problem.

## Approach

<!-- Describe your solution approach here -->

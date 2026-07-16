# 0272. Closest Binary Search Tree Value II

- **Difficulty:** Hard
- **LeetCode:** [https://leetcode.com/problems/closest-binary-search-tree-value-ii/](https://leetcode.com/problems/closest-binary-search-tree-value-ii/)
- **Premium:** Yes
- **Tags:** two-pointers, stack, tree, depth-first-search, binary-search-tree, heap-(priority-queue), binary-tree

## Problem

Given the `root` of a binary search tree, a `target` value, and an integer `k`, return *the *`k`* values in the BST that are closest to the* `target`. You may return the answer in **any order**.

You are **guaranteed** to have only one unique set of `k` values in the BST that are closest to the `target`.



**Example 1:**

**Input:** root = [4,2,5,1,3], target = 3.714286, k = 2
**Output:** [4,3]

**Example 2:**

**Input:** root = [1], target = 0.000000, k = 1
**Output:** [1]



**Constraints:**

	- The number of nodes in the tree is `n`.

	- `1 <= k <= n <= 10^{4}`.

	- `0 <= Node.val <= 10^{9}`

	- `-10^{9} <= target <= 10^{9}`



**Follow up:** Assume that the BST is balanced. Could you solve it in less than `O(n)` runtime (where `n = total nodes`)?

---
_Problem text from the [doocs/leetcode](https://github.com/doocs/leetcode) community mirror (LeetCode Premium)._

### Hints

1. Consider implement these two helper functions:
- `getPredecessor(N)`, which returns the next smaller node to N.

- `getSuccessor(N)`, which returns the next larger node to N.
2. Try to assume that each node has a parent pointer, it makes the problem much easier.
3. Without parent pointer we just need to keep track of the path from the root to the current node using a stack.
4. You would need two stacks to track the path in finding predecessor and successor node separately.

## Approach

<!-- Describe your solution approach here -->

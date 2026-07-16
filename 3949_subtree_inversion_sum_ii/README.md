# 3949. Subtree Inversion Sum II

- **Difficulty:** Hard
- **LeetCode:** [https://leetcode.com/problems/subtree-inversion-sum-ii/](https://leetcode.com/problems/subtree-inversion-sum-ii/)
- **Premium:** Yes
- **Tags:** array, dynamic-programming, tree, depth-first-search

## Problem

You are given an undirected tree rooted at node 0, with `n` nodes numbered from 0 to `n - 1`. The tree is represented by a 2D integer array `edges` of length `n - 1`, where `edges[i] = [u_{i}, v_{i}]` indicates an edge between nodes `u_{i}` and `v_{i}`.

You are also given an integer array `nums` of length `n`, where `nums[i]` represents the value at node `i`, and an integer `k`.

You may perform **inversion operations** on a subset of nodes subject to the following rules:


	**Subtree Inversion Operation:**



    	When you invert a node, every value in the subtree rooted at that node is multiplied by -1.








    **Distance Constraint on Inversions:**



    	You may only invert a node if it is “sufficiently far” from any other inverted node.




    	If you invert two nodes `a` and `b`, the **distance** (the number of edges on the unique path between them) must be **at least** `k`.







Return the **maximum** possible **sum** of the tree’s node values after applying **inversion operations**.



**Example 1:**

**Input:** edges = [[0,1],[0,2],[0,3],[1,4],[1,5]], nums = [1,0,-10,3,4,5], k = 2

**Output:** 23

**Explanation:**

After inverting the subtree rooted at node 2, the maximum sum becomes `1 + 0 + 10 + 3 + 4 + 5 = 23`.

**Example 2:**

**Input:** edges = [[0,1],[1,2]], nums = [5,-10,-10], k = 1

**Output:** 25

**Explanation:**

****

After inverting the subtree rooted at node 1, the maximum sum becomes `5 + 10 + 10 = 25`.

**Example 3:**

**Input:** edges = [[0,1],[0,2]], nums = [1,-5,-6], k = 2

**Output:** 12

**Explanation:**

	- After inverting the subtrees rooted at nodes 1 and 2, `nums = [1, 5, 6]`.

	- This is valid because nodes 1 and 2 are two edges apart (`1 → 0` and `0 → 2`), which is at least `k`.

	- The maximum sum is `1 + 5 + 6 = 12`.

**Example 4:**

**Input:** edges = [[0,1],[0,2]], nums = [1,-5,-6], k = 3

**Output:** 10

**Explanation:**

	- After inverting the subtree rooted at nodes 0, `nums = [-1, 5, 6]`.

	- The maximum sum is `(-1) + 5 + 6 = 10`.

	- Note that we cannot invert nodes 1 and 2 because their distance is `2 < k = 3`.



**Constraints:**

	- `nums.length == n`

	- `edges.length == n - 1`

	- `2 <= n <= 5 * 10^{4}`

	- `edges[i].length == 2`

	- `0 <= edges[i][0], edges[i][1] < n`

	- `-4 * 10^{4} <= nums[i] <= 4 * 10^{4}`

	- `1 <= k <= 50`

	- It is guaranteed that `edges` forms a tree.

---
_Problem text from the [doocs/leetcode](https://github.com/doocs/leetcode) community mirror (LeetCode Premium)._

### Hints

1. Root the tree at 0. Do not track only inverted ancestors; the constraint is between any two inverted nodes, including nodes in different child subtrees.
2. Use DP by distance. Let `mx[u][d]` and `mn[u][d]` be the maximum/minimum possible subtree sum of `u`, assuming every inverted node inside this subtree is at distance at least `d` from `u`. Cap distances at `k`.
3. When merging child subtrees, if one inverted node is in one child at distance `a` from that child, and another is in a different child at distance `b`, their distance through `u` is `a + b + 2`, so it must be at least `k`.
4. Store both max and min because inverting `u` negates the whole subtree. So the best value after inverting `u` comes from negating the minimum compatible child sum, and the worst comes from negating the maximum compatible child sum.

## Approach

<!-- Describe your solution approach here -->

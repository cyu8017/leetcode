# 2378. Choose Edges to Maximize Score in a Tree

- **Difficulty:** Medium
- **LeetCode:** [https://leetcode.com/problems/choose-edges-to-maximize-score-in-a-tree/](https://leetcode.com/problems/choose-edges-to-maximize-score-in-a-tree/)
- **Premium:** Yes
- **Tags:** dynamic-programming, tree, depth-first-search

## Problem

You are given a **weighted** tree consisting of `n` nodes numbered from `0` to `n - 1`.

The tree is **rooted** at node `0` and represented with a **2D** array `edges` of size `n` where `edges[i] = [par_{i}, weight_{i}]` indicates that node `par_{i}` is the **parent** of node `i`, and the edge between them has a weight equal to `weight_{i}`. Since the root does **not** have a parent, you have `edges[0] = [-1, -1]`.

Choose some edges from the tree such that no two chosen edges are **adjacent** and the **sum** of the weights of the chosen edges is maximized.

Return *the **maximum** sum of the chosen edges*.

**Note**:

	- You are allowed to **not** choose any edges in the tree, the sum of weights in this case will be `0`.

	- Two edges `Edge_{1}` and `Edge_{2}` in the tree are **adjacent** if they have a **common** node.


		- In other words, they are adjacent if `Edge_{1}` connects nodes `a` and `b` and `Edge_{2}` connects nodes `b` and `c`.







**Example 1:**

**Input:** edges = [[-1,-1],[0,5],[0,10],[2,6],[2,4]]
**Output:** 11
**Explanation:** The above diagram shows the edges that we have to choose colored in red.
The total score is 5 + 6 = 11.
It can be shown that no better score can be obtained.

**Example 2:**

**Input:** edges = [[-1,-1],[0,5],[0,-6],[0,7]]
**Output:** 7
**Explanation:** We choose the edge with weight 7.
Note that we cannot choose more than one edge because all edges are adjacent to each other.



**Constraints:**

	- `n == edges.length`

	- `1 <= n <= 10^{5}`

	- `edges[i].length == 2`

	- `par_{0} == weight_{0} == -1`

	- `0 <= par_{i} <= n - 1` for all `i >= 1`.

	- `par_{i} != i`

	- `-10^{6} <= weight_{i} <= 10^{6}` for all `i >= 1`.

	- `edges` represents a valid tree.

---
_Problem text from the [doocs/leetcode](https://github.com/doocs/leetcode) community mirror (LeetCode Premium)._

### Hints

1. Use dynamic programming to recursively solve the problem for smaller subtrees.
2. You can ignore the edges with negative weights.
3. The states of the dp are the following: the root of the subtree you are at, and a boolean variable that will tell you if you have chosen the edge that connects that node and its parent.
4. What are the transitions of this dp?

## Approach

<!-- Describe your solution approach here -->

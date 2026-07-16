# 3930. Power Update After K-th Largest Insertion II

- **Difficulty:** Hard
- **LeetCode:** [https://leetcode.com/problems/power-update-after-k-th-largest-insertion-ii/](https://leetcode.com/problems/power-update-after-k-th-largest-insertion-ii/)
- **Premium:** Yes
- **Tags:** array, hash-table, math, segment-tree, sorting

## Problem

You are given an integer array `nums` and an integer `p`.

You are also given a 2D integer array `queries`, where each `queries[i] = [val_{i}, k_{i}]`.

For each query:

	- Insert `val_{i}` into `nums`.

	- Let `x` be the `k_{i}^{th}` **largest** element in the current `nums`.

	- **Update** `p` to `p^{x} % (10^{9} + 7)`.

Return an array `ans` where the `ans[i]` represents the value of `p` after processing the `i^{th}` query.



**Example 1:**

**Input:** nums = [2], p = 4, queries = [[3,1],[1,2]]

**Output:** [64,4096]

**Explanation:**



			`i`
			`val_{i}`
			Current

			`nums`
			`k_{i}`
			`k_{i}^{th}`

			largest
			p
			New `p = p^{k} % (10^{9} + 7)`




			0
			3
			[2, 3]
			1
			3
			4
			4^{3} % (10^{9} + 7) = 64


			1
			1
			[2, 3, 1]
			2
			2
			64
			64^{2} % (10^{9} + 7) = 4096



Thus, `ans = [64, 4096]`.

**Example 2:**

**Input:** nums = [7,5], p = 6, queries = [[4,3],[7,2]]

**Output:** [1296,220296870]

**Explanation:**



			`i`
			`val_{i}`
			Current​​​​​​​

			`nums`
			`k_{i}`
			`k_{i}^{th}`

			largest
			`p`
			New `p = p^{k} % (10^{9} + 7)`




			0
			4
			[7, 5, 4]
			3
			4
			6
			6^{4} % (10^{9} + 7) = 1296


			1
			7
			[7, 5, 4, 7]
			2
			7
			1296
			1296^{7} % (10^{9} + 7) = 220296870



Thus, `ans = [1296, 220296870]`



**Constraints:**

	- `1 <= nums.length <= 2 * 10^{4}`

	- `1 <= nums[i] <= 10^{9}`

	- `​​​​​​​1 <= p <= 10^{9}`

	- `1 <= queries.length <= 2 * 10^{4}`

	- `^{​​​​​​​}1 <= val_{i} <= 10^{9}`

	- `1 <= k_{i} <= n + i + 1`​​​​​​​

---
_Problem text from the [doocs/leetcode](https://github.com/doocs/leetcode) community mirror (LeetCode Premium)._

### Hints

1. Convert `k^{th}` largest into rank `size - k + 1` in increasing order.
2. Use coordinate compression + Fenwick tree to find that ranked value efficiently.
3. Update `p` with fast modular exponentiation.

## Approach

<!-- Describe your solution approach here -->

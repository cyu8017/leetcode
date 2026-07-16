# 3935. Power Update After K-th Largest Insertion I

- **Difficulty:** Medium
- **LeetCode:** [https://leetcode.com/problems/power-update-after-k-th-largest-insertion-i/](https://leetcode.com/problems/power-update-after-k-th-largest-insertion-i/)
- **Premium:** Yes
- **Tags:** array, hash-table, math, segment-tree, sorting, heap-(priority-queue)

## Problem

You are given an integer array `nums` and an integer `p`.

You are also given a 2D integer array `queries`, where each `queries[i] = [val_{i}, k_{i}]` and the difference between **consecutive** `k_{i}` values is always **less** than 10.

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

	- `1 <= nums.length <= 2 × 10^{4}`

	- `1 <= nums[i] <= 10^{6}`

	- `​​​​​​​1 <= p <= 10^{6}`

	- `1 <= queries.length <= 2 × 10^{4}`

	- `^{​​​​​​​}1 <= val_{i} <= 10^{6}`

	- `1 <= k_{i} <= n + i + 1`

	- `|k_{i} - k_{i - 1}| < 10` for `i > 0`

---
_Problem text from the [doocs/leetcode](https://github.com/doocs/leetcode) community mirror (LeetCode Premium)._

### Hints

1. Keep the largest `k` elements separately. The answer is the smallest among them.
2. After inserting a value, rebalance the two sets/heaps so the “top `k`” side has exactly `k` elements. Since `abs(k_{i} - k_{i-1}) < 10`, only a few elements move each query.
3. Update `p` with fast modular exponentiation.

## Approach

<!-- Describe your solution approach here -->

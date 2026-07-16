# 3958. Minimum Cost to Split into Ones II

- **Difficulty:** Medium
- **LeetCode:** [https://leetcode.com/problems/minimum-cost-to-split-into-ones-ii/](https://leetcode.com/problems/minimum-cost-to-split-into-ones-ii/)
- **Premium:** Yes
- **Tags:** math

## Problem

You are given an integer `n`.

In one operation, you may split an integer `x` into two positive integers `a` and `b` such that `a + b = x`.

The cost of this operation is `a * b`.

Return the **minimum** total cost required to split the integer `n` into `n` ones.



**Example 1:**

**Input:** n = 3

**Output:** 3

**Explanation:**

One optimal set of operations is:



			`x`
			`a`
			`b`
			`a + b`
			`a * b`
			Cost


			3
			1
			2
			3
			2
			2


			2
			1
			1
			2
			1
			1



Thus, the minimum total cost is `2 + 1 = 3`.

**Example 2:**

**Input:** n = 4

**Output:** 6

**Explanation:​​​​​​​**

One optimal set of operations is:



			`x`
			`a`
			`b`
			`a + b`
			`a * b`
			Cost


			4
			2
			2
			4
			4
			4


			2
			1
			1
			2
			1
			1



Thus, the minimum total cost is `4 + 1 + 1 = 6`.



**Constraints:**

	- `1 <= n <= 5 * 10^{7}`

---
_Problem text from the [doocs/leetcode](https://github.com/doocs/leetcode) community mirror (LeetCode Premium)._

### Hints

1. Let `f(x)` be the minimum total cost to split `x` into ones.
2. If you split `x` into `a` and `b`, then `f(x) = a * b + f(a) + f(b)`.
3. Look for an invariant: the total cost may depend only on the final set of pieces, not on the order of splits.

## Approach

<!-- Describe your solution approach here -->

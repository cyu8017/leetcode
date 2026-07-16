# 0465. Optimal Account Balancing

- **Difficulty:** Hard
- **LeetCode:** [https://leetcode.com/problems/optimal-account-balancing/](https://leetcode.com/problems/optimal-account-balancing/)
- **Premium:** Yes
- **Tags:** array, dynamic-programming, backtracking, bit-manipulation, bitmask

## Problem

You are given an array of transactions `transactions` where `transactions[i] = [from_{i}, to_{i}, amount_{i}]` indicates that the person with `ID = from_{i}` gave `amount_{i} $` to the person with `ID = to_{i}`.

Return *the minimum number of transactions required to settle the debt*.



**Example 1:**

**Input:** transactions = [[0,1,10],[2,0,5]]
**Output:** 2
**Explanation:**
Person #0 gave person #1 $10.
Person #2 gave person #0 $5.
Two transactions are needed. One way to settle the debt is person #1 pays person #0 and #2 $5 each.

**Example 2:**

**Input:** transactions = [[0,1,10],[1,0,1],[1,2,5],[2,0,5]]
**Output:** 1
**Explanation:**
Person #0 gave person #1 $10.
Person #1 gave person #0 $1.
Person #1 gave person #2 $5.
Person #2 gave person #0 $5.
Therefore, person #1 only need to give person #0 $4, and all debt is settled.



**Constraints:**

	- `1 <= transactions.length <= 8`

	- `transactions[i].length == 3`

	- `0 <= from_{i}, to_{i} < 12`

	- `from_{i} != to_{i}`

	- `1 <= amount_{i} <= 100`

---
_Problem text from the [doocs/leetcode](https://github.com/doocs/leetcode) community mirror (LeetCode Premium)._

## Approach

<!-- Describe your solution approach here -->

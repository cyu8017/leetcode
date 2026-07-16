# 3711. Maximum Transactions Without Negative Balance

- **Difficulty:** Medium
- **LeetCode:** [https://leetcode.com/problems/maximum-transactions-without-negative-balance/](https://leetcode.com/problems/maximum-transactions-without-negative-balance/)
- **Premium:** Yes
- **Tags:** array, greedy, heap-(priority-queue)

## Problem

You are given an integer array `transactions`, where `transactions[i]` represents the amount of the `i^{th}` transaction:

	- A positive value means money is **received**.

	- A negative value means money is **sent**.

The account starts with a balance of 0, and the balance **must never become negative**. Transactions must be considered in the given order, but you are allowed to skip some transactions.

Return an integer denoting the **maximum number of transactions** that can be performed without the balance ever going negative.



**Example 1:**

**Input:** transactions = [2,-5,3,-1,-2]

**Output:** 4

**Explanation:**

One optimal sequence is `[2, 3, -1, -2]`, balance: `0 → 2 → 5 → 4 → 2`.

**Example 2:**

**Input:** transactions = [-1,-2,-3]

**Output:** 0

**Explanation:**

All transactions are negative. Including any would make the balance negative.

**Example 3:**

**Input:** transactions = [3,-2,3,-2,1,-1]

**Output:** 6

**Explanation:**

All transactions can be taken in order, balance: `0 → 3 → 1 → 4 → 2 → 3 → 2`.



**Constraints:**

	- `1 <= transactions.length <= 10^{5}`

	- `-10^{9} <= transactions[i] <= 10^{9}`

---
_Problem text from the [doocs/leetcode](https://github.com/doocs/leetcode) community mirror (LeetCode Premium)._

### Hints

1. Scan the list left to right, keeping a running `balance` and a container `accepted` that tracks the sizes of negative transactions you have taken.
2. Always take nonnegative transactions; they increase `balance` and the total count.
3. If a negative `t` can be paid (`balance + t >= 0`), accept it and record its absolute value in `accepted`.
4. If a negative would make the balance go below zero, but you previously accepted a larger negative, replace that larger one with the current smaller one (restore balance, swap in the smaller): this trade increases the number of transactions you can keep.

## Approach

<!-- Describe your solution approach here -->

# LeetCode 2412 - Minimum Money Required Before Transactions
# https://leetcode.com/problems/minimum-money-required-before-transactions/

from typing import List


class Solution:
    def minimumMoney(self, transactions: List[List[int]]) -> int:
        total_loss = max_cashback = max_cost = 0
        for cost, cashback in transactions:
            if cost > cashback:
                total_loss += cost - cashback
                max_cashback = max(max_cashback, cashback)
            else:
                max_cost = max(max_cost, cost)
        return max(total_loss + max_cashback, total_loss + max_cost)

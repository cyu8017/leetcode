# LeetCode 0465 - Optimal Account Balancing
# https://leetcode.com/problems/optimal-account-balancing/


class Solution:
    def minTransfers(self, transactions: list[list[int]]) -> int:
        balances: dict[int, int] = {}
        for source, target, amount in transactions:
            balances[source] = balances.get(source, 0) - amount
            balances[target] = balances.get(target, 0) + amount
        debts = [balance for balance in balances.values() if balance]

        def dfs(index: int) -> int:
            while index < len(debts) and debts[index] == 0:
                index += 1
            if index == len(debts):
                return 0
            best = len(debts)
            for next_index in range(index + 1, len(debts)):
                if debts[index] * debts[next_index] < 0:
                    debts[next_index] += debts[index]
                    best = min(best, 1 + dfs(index + 1))
                    debts[next_index] -= debts[index]
            return best

        return dfs(0)

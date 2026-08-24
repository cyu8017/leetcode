# LeetCode 3562 - Maximum Profit from Trading Stocks with Discounts
# https://leetcode.com/problems/maximum-profit-from-trading-stocks-with-discounts/

from typing import List


class Solution:
    def maxProfit(
        self,
        n: int,
        present: List[int],
        future: List[int],
        hierarchy: List[List[int]],
        budget: int,
    ) -> int:
        g = [[] for _ in range(n + 1)]
        for e in hierarchy:
            g[e[0]].append(e[1])

        def dfs(u: int) -> List[List[int]]:
            nxt = [[0, 0] for _ in range(budget + 1)]
            for v in g[u]:
                fv = dfs(v)
                for j in range(budget, -1, -1):
                    for jv in range(j + 1):
                        for pre in range(2):
                            nxt[j][pre] = max(nxt[j][pre], nxt[j - jv][pre] + fv[jv][pre])
            f = [[0, 0] for _ in range(budget + 1)]
            price = future[u - 1]
            for j in range(budget + 1):
                for pre in range(2):
                    cost = present[u - 1] // (pre + 1)
                    if j >= cost:
                        buy_profit = nxt[j - cost][1] + (price - cost)
                        f[j][pre] = max(nxt[j][0], buy_profit)
                    else:
                        f[j][pre] = nxt[j][0]
            return f

        return dfs(1)[budget][0]

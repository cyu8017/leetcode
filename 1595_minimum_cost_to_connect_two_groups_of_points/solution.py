from typing import List

class Solution:
    def connectTwoGroups(self, cost: List[List[int]]) -> int:
        m, n = len(cost), len(cost[0])
        full, inf = 1 << n, 10**9
        dp = [inf] * full
        dp[0] = 0
        for row in cost:
            nxt = [inf] * full
            for mask in range(full):
                for j, value in enumerate(row):
                    new_mask = mask | (1 << j)
                    nxt[new_mask] = min(nxt[new_mask], dp[mask] + value, nxt[mask] + value)
            dp = nxt
        minimum = [min(cost[i][j] for i in range(m)) for j in range(n)]
        return min(dp[mask] + sum(minimum[j] for j in range(n) if not mask >> j & 1) for mask in range(full))

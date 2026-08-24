# LeetCode 3429 - Paint House IV
# https://leetcode.com/problems/paint-house-iv/

from typing import List


class Solution:
    def minCost(self, n: int, cost: List[List[int]]) -> int:
        inf = 10**18
        m = n // 2
        dp = [[0] * 3 for _ in range(3)]
        for a in range(3):
            for b in range(3):
                dp[a][b] = inf if a == b else cost[0][a] + cost[n - 1][b]
        for i in range(1, m):
            ndp = [[inf] * 3 for _ in range(3)]
            for pa in range(3):
                for pb in range(3):
                    if dp[pa][pb] >= inf:
                        continue
                    for a in range(3):
                        if a == pa:
                            continue
                        for b in range(3):
                            if b == pb or a == b:
                                continue
                            v = dp[pa][pb] + cost[i][a] + cost[n - 1 - i][b]
                            if v < ndp[a][b]:
                                ndp[a][b] = v
            dp = ndp
        ans = inf
        for a in range(3):
            for b in range(3):
                if dp[a][b] < ans:
                    ans = dp[a][b]
        return ans

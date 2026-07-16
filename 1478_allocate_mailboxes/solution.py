from typing import List, Optional

class Solution:
    def minDistance(self, houses: List[int], k: int) -> int:
        houses.sort()
        n = len(houses)
        cost = [[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(i, n):
                mid = houses[(i+j)//2]
                cost[i][j] = sum(abs(houses[t]-mid) for t in range(i, j+1))
        dp = [0] + [10**15]*n
        for _ in range(k):
            ndp = [0] + [10**15]*n
            for j in range(1, n+1):
                ndp[j] = min(dp[i] + cost[i][j-1] for i in range(j))
            dp = ndp
        return dp[n]

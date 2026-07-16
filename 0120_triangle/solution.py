from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp=triangle[-1][:]
        for row in reversed(triangle[:-1]):
            for i, value in enumerate(row): dp[i]=value+min(dp[i], dp[i+1])
        return dp[0]

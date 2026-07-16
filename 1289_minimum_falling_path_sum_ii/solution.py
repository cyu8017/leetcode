from typing import List

class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        dp = grid[0][:]
        for row in grid[1:]:
            first = min(range(len(dp)), key=dp.__getitem__)
            second_value = min(dp[i] for i in range(len(dp)) if i != first) if len(dp) > 1 else 0
            dp = [value + (second_value if i == first else dp[first]) for i, value in enumerate(row)]
        return min(dp)

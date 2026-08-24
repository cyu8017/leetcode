# LeetCode 2209 - Minimum White Tiles After Covering With Carpets
# https://leetcode.com/problems/minimum-white-tiles-after-covering-with-carpets/
class Solution:
    def minimumWhiteTiles(self, floor: str, numCarpets: int, carpetLen: int) -> int:
        n = len(floor)
        INF = 1 << 30
        dp = [[INF] * (n + 1) for _ in range(numCarpets + 1)]
        dp[0][0] = 0
        for j in range(1, (n) + 1):
            dp[0][j] = dp[0][j - 1] + (1 if floor[j - 1] == "1" else 0)
        for c in range(1, (numCarpets) + 1):
            dp[c][0] = 0
            for j in range(1, (n) + 1):
                dp[c][j] = dp[c][j - 1] + (1 if floor[j - 1] == "1" else 0)
                start = max(0, j - carpetLen)
                dp[c][j] = min(dp[c][j], dp[c - 1][start])
        return dp[numCarpets][n]

# LeetCode 1000 - Minimum Cost to Merge Stones
# https://leetcode.com/problems/minimum-cost-to-merge-stones/

class Solution:
    def mergeStones(self, stones: list[int], k: int) -> int:
        n = len(stones)
        if (n - 1) % (k - 1):
            return -1
        prefix = [0]
        for x in stones:
            prefix.append(prefix[-1] + x)
        dp = [[0] * n for _ in range(n)]
        for length in range(k, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                dp[i][j] = min(dp[i][m] + dp[m + 1][j] for m in range(i, j, k - 1))
                if (length - 1) % (k - 1) == 0:
                    dp[i][j] += prefix[j + 1] - prefix[i]
        return dp[0][n - 1]

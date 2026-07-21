from typing import List

class Solution:
    def minSpaceWastedKResizing(self, nums: List[int], k: int) -> int:
        n = len(nums)
        INF = 10**18
        waste = [[0] * n for _ in range(n)]
        for i in range(n):
            mx = total = 0
            for j in range(i, n):
                mx = max(mx, nums[j])
                total += nums[j]
                waste[i][j] = mx * (j - i + 1) - total

        # dp[i][j] = min waste for nums[:i] using j segments (j-1 resizes)
        segments = k + 1
        dp = [[INF] * (segments + 1) for _ in range(n + 1)]
        dp[0][0] = 0
        for i in range(1, n + 1):
            for s in range(1, min(segments, i) + 1):
                for p in range(s - 1, i):
                    dp[i][s] = min(dp[i][s], dp[p][s - 1] + waste[p][i - 1])
        return min(dp[n][s] for s in range(1, segments + 1))

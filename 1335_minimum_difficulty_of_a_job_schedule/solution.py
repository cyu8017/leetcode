# LeetCode 1335 - Minimum Difficulty Of A Job Schedule

from typing import List

class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        if n < d:
            return -1
        dp = [10**9] * n
        hardest = 0
        for i, value in enumerate(jobDifficulty):
            hardest = max(hardest, value)
            dp[i] = hardest
        for day in range(1, d):
            nxt = [10**9] * n
            for end in range(day, n):
                hardest = 0
                for start in range(end, day - 1, -1):
                    hardest = max(hardest, jobDifficulty[start])
                    nxt[end] = min(nxt[end], dp[start - 1] + hardest)
            dp = nxt
        return dp[-1]

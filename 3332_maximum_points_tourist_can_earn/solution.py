# LeetCode 3332 - Maximum Points Tourist Can Earn
# https://leetcode.com/problems/maximum-points-tourist-can-earn/

from typing import List


class Solution:
    def maxScore(self, n: int, k: int, stayScore: List[List[int]], travelScore: List[List[int]]) -> int:
        dp = [0] * n
        for day in range(k):
            ndp = [-(1 << 30)] * n
            for dest in range(n):
                best = -(1 << 30)
                for src in range(n):
                    val = dp[src]
                    if src == dest:
                        val += stayScore[day][dest]
                    else:
                        val += travelScore[src][dest]
                    if val > best:
                        best = val
                ndp[dest] = best
            dp = ndp
        ans = dp[0]
        for i in range(1, n):
            if dp[i] > ans:
                ans = dp[i]
        return ans

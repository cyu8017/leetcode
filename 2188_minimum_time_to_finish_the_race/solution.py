# LeetCode 2188 - Minimum Time to Finish the Race
# https://leetcode.com/problems/minimum-time-to-finish-the-race/

from typing import List
class Solution:
    def minimumFinishTime(self, tires: List[List[int]], changeTime: int, numLaps: int) -> int:
        INF = 1 << 30
        minTime = [INF] * (20)
        for tire in tires:
            f = tire[0]
            r = tire[1]
            t = f
            lap = f
            x = 1
            while x < 20 and t < minTime[x]:
                minTime[x] = t
                lap *= r
                if lap > changeTime + f:
                    break
                t += lap
                x += 1
        dp = [INF] * (numLaps + 1)
        dp[0] = -changeTime
        for i in range(1, (numLaps) + 1):
            j = 1
            while j <= i and j < 20:
                dp[i] = min(dp[i], dp[i - j] + changeTime + minTime[j])
                j += 1
        return dp[numLaps]

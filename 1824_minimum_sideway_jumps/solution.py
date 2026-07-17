# LeetCode 1824 - Minimum Sideway Jumps
# https://leetcode.com/problems/minimum-sideway-jumps/

from typing import List


class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        inf = float("inf")
        dp = [1, 0, 1]

        for obs in obstacles:
            blocked = [obs == lane + 1 for lane in range(3)]
            ndp = [inf, inf, inf]
            for lane in range(3):
                if blocked[lane]:
                    continue
                for other in range(3):
                    if blocked[other] or dp[other] == inf:
                        continue
                    ndp[lane] = min(ndp[lane], dp[other] + (lane != other))
            dp = ndp

        return min(dp)

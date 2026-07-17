# LeetCode 1883 - Minimum Skips to Arrive at Meeting On Time
# https://leetcode.com/problems/minimum-skips-to-arrive-at-meeting-on-time/

from typing import List


class Solution:
    def minSkips(self, dist: List[int], speed: int, hoursBefore: int) -> int:
        limit = hoursBefore * speed
        dp = [float("inf")] * (len(dist) + 1)
        dp[0] = 0

        for road in dist:
            nxt = [float("inf")] * (len(dist) + 1)
            for skips in range(len(dist)):
                if dp[skips] == float("inf"):
                    continue
                nxt[skips] = min(
                    nxt[skips],
                    ((dp[skips] + road + speed - 1) // speed) * speed,
                )
                nxt[skips + 1] = min(nxt[skips + 1], dp[skips] + road)
            dp = nxt

        for skips, total in enumerate(dp):
            if total <= limit:
                return skips
        return -1

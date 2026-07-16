# LeetCode 0568 - Maximum Vacation Days
# https://leetcode.com/problems/maximum-vacation-days/

from typing import List


class Solution:
    def maxVacationDays(self, flights: List[List[int]], days: List[List[int]]) -> int:
        cities = len(flights)
        weeks = len(days[0])
        neg = -10**9

        dp = [neg] * cities
        dp[0] = 0

        for week in range(weeks):
            nxt = [neg] * cities
            for city in range(cities):
                if dp[city] == neg:
                    continue
                for dest in range(cities):
                    if dest == city or flights[city][dest]:
                        nxt[dest] = max(nxt[dest], dp[city] + days[dest][week])
            dp = nxt

        return max(dp)

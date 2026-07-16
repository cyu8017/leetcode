# LeetCode 0502 - IPO
# https://leetcode.com/problems/ipo/

import heapq


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: list[int], capital: list[int]) -> int:
        projects = sorted(zip(capital, profits))
        available: list[int] = []
        index = 0
        for _ in range(k):
            while index < len(projects) and projects[index][0] <= w:
                heapq.heappush(available, -projects[index][1])
                index += 1
            if not available:
                break
            w -= heapq.heappop(available)
        return w

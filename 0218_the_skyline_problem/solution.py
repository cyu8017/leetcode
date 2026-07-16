# LeetCode 0218 - The Skyline Problem
# https://leetcode.com/problems/the-skyline-problem/

import heapq
from typing import List


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        events: list[tuple[int, int, int]] = []
        for left, right, height in buildings:
            events.append((left, -height, right))
            events.append((right, 0, 0))
        events.sort()

        result: list[list[int]] = []
        live: list[tuple[int, int]] = [(0, float("inf"))]
        for x, neg_h, end in events:
            while live[0][1] <= x:
                heapq.heappop(live)
            if neg_h:
                heapq.heappush(live, (neg_h, end))
            height = -live[0][0]
            if not result or result[-1][1] != height:
                result.append([x, height])
        return result

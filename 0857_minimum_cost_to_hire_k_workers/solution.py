# LeetCode 0857 - Minimum Cost to Hire K Workers
# https://leetcode.com/problems/minimum-cost-to-hire-k-workers/

import heapq


class Solution:
    def mincostToHireWorkers(self, quality: list[int], wage: list[int], k: int) -> float:
        workers = sorted((w / q, q) for q, w in zip(quality, wage))
        heap: list[int] = []
        total_q = 0
        ans = float("inf")
        for ratio, q in workers:
            heapq.heappush(heap, -q)
            total_q += q
            if len(heap) > k:
                total_q += heapq.heappop(heap)
            if len(heap) == k:
                ans = min(ans, total_q * ratio)
        return ans

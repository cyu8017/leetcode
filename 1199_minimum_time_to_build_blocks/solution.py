# LeetCode 1199 - Minimum Time to Build Blocks
# https://leetcode.com/problems/minimum-time-to-build-blocks/

import heapq


class Solution:
    def minBuildTime(self, blocks: list[int], split: int) -> int:
        heap = blocks[:]
        heapq.heapify(heap)
        while len(heap) > 1:
            heapq.heappop(heap)
            heapq.heappush(heap, heapq.heappop(heap) + split)
        return heap[0]

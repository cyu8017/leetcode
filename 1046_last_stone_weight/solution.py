# LeetCode 1046 - Last Stone Weight
# https://leetcode.com/problems/last-stone-weight/

import heapq


class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        heap = [-x for x in stones]
        heapq.heapify(heap)
        while len(heap) > 1:
            a = -heapq.heappop(heap)
            b = -heapq.heappop(heap)
            if a != b:
                heapq.heappush(heap, -(a - b))
        return -heap[0] if heap else 0

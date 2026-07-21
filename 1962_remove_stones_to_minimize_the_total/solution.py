import heapq
from typing import List

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = [-p for p in piles]
        heapq.heapify(heap)
        for _ in range(k):
            x = -heapq.heappop(heap)
            heapq.heappush(heap, -(x - x // 2))
        return -sum(heap)

# LeetCode 0767 - Reorganize String
# https://leetcode.com/problems/reorganize-string/

import heapq
from collections import Counter


class Solution:
    def reorganizeString(self, s: str) -> str:
        heap = [(-count, ch) for ch, count in Counter(s).items()]
        heapq.heapify(heap)
        if -heap[0][0] > (len(s) + 1) // 2:
            return ""

        result: list[str] = []
        while len(heap) >= 2:
            c1, a = heapq.heappop(heap)
            c2, b = heapq.heappop(heap)
            result.extend((a, b))
            if c1 + 1:
                heapq.heappush(heap, (c1 + 1, a))
            if c2 + 1:
                heapq.heappush(heap, (c2 + 1, b))
        if heap:
            result.append(heap[0][1])
        return "".join(result)

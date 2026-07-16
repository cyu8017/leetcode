from heapq import heappop, heappush
from typing import List


class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        heap = []
        day = eaten = 0
        n = len(apples)
        while day < n or heap:
            if day < n and apples[day]:
                heappush(heap, (day + days[day], apples[day]))
            while heap and heap[0][0] <= day:
                heappop(heap)
            if heap:
                expire, count = heappop(heap)
                eaten += 1
                if count > 1:
                    heappush(heap, (expire, count - 1))
            day += 1
        return eaten

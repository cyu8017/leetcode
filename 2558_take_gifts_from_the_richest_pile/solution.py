# LeetCode 2558 - Take Gifts From the Richest Pile
# https://leetcode.com/problems/take-gifts-from-the-richest-pile/

import heapq
import math
from typing import List


class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        h = [-g for g in gifts]
        heapq.heapify(h)
        for _ in range(k):
            x = -heapq.heappop(h)
            heapq.heappush(h, -int(math.sqrt(x)))
        return -sum(h)

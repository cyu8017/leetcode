# LeetCode 2530 - Maximal Score After Applying K Operations
# https://leetcode.com/problems/maximal-score-after-applying-k-operations/

import heapq
from typing import List


class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        pq = [-x for x in nums]
        heapq.heapify(pq)
        ans = 0
        for _ in range(k):
            x = -heapq.heappop(pq)
            ans += x
            heapq.heappush(pq, -((x + 2) // 3))
        return ans

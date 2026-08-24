# LeetCode 2233 - Maximum Product After K Increments
# https://leetcode.com/problems/maximum-product-after-k-increments/

import heapq
from typing import List


class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        MOD = 1000000007
        h = nums[:]
        heapq.heapify(h)
        for _ in range(k):
            x = heapq.heappop(h)
            heapq.heappush(h, x + 1)
        ans = 1
        for x in h:
            ans = ans * x % MOD
        return ans

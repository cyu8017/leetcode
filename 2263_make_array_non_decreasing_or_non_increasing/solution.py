# LeetCode 2263 - Make Array Non-decreasing or Non-increasing
# https://leetcode.com/problems/make-array-non-decreasing-or-non-increasing/

import heapq
from typing import List


class Solution:
    def convertArray(self, nums: List[int]) -> int:
        def cost(arr: List[int]) -> int:
            h = []
            ans = 0
            for x in arr:
                if h and -h[0] > x:
                    t = -heapq.heappop(h)
                    ans += t - x
                    heapq.heappush(h, -x)
                heapq.heappush(h, -x)
            return ans

        return min(cost(nums), cost(list(reversed(nums))))

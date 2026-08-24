# LeetCode 2599 - Make the Prefix Sum Non-negative
# https://leetcode.com/problems/make-the-prefix-sum-non-negative/

import heapq
from typing import List


class Solution:
    def makePrefSumNonNegative(self, nums: List[int]) -> int:
        h = []
        s = 0
        ans = 0
        for x in nums:
            s += x
            if x < 0:
                heapq.heappush(h, x)
            if s < 0:
                worst = heapq.heappop(h)
                s -= worst
                ans += 1
        return ans

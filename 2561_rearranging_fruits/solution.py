# LeetCode 2561 - Rearranging Fruits
# https://leetcode.com/problems/rearranging-fruits/

from typing import List


class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        freq = {}
        mn = float("inf")
        for x in basket1:
            freq[x] = freq.get(x, 0) + 1
            mn = min(mn, x)
        for x in basket2:
            freq[x] = freq.get(x, 0) - 1
            mn = min(mn, x)
        extra = []
        for k, v in freq.items():
            if v % 2 != 0:
                return -1
            for _ in range(abs(v) // 2):
                extra.append(k)
        extra.sort()
        ans = 0
        for i in range(len(extra) // 2):
            ans += min(extra[i], 2 * mn)
        return ans

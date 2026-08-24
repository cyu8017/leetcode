# LeetCode 2921 - Maximum Profitable Triplets With Increasing Prices II
# https://leetcode.com/problems/maximum-profitable-triplets-with-increasing-prices-ii/

from typing import List


class Solution:
    def maxProfit(self, prices: List[int], profits: List[int]) -> int:
        n = len(prices)
        ans = -1
        bit = [0] * 5002

        def update(i: int, val: int) -> None:
            while i < len(bit):
                if val > bit[i]:
                    bit[i] = val
                i += i & -i

        def query(i: int) -> int:
            best = -1
            while i > 0:
                if bit[i] > best:
                    best = bit[i]
                i -= i & -i
            return best

        max_left = [0] * n
        for j in range(n):
            max_left[j] = query(prices[j] - 1)
            update(prices[j], profits[j])
        for j in range(n):
            best_r = -1
            for k in range(j + 1, n):
                if prices[k] > prices[j] and profits[k] > best_r:
                    best_r = profits[k]
            if max_left[j] >= 0 and best_r >= 0:
                cand = max_left[j] + profits[j] + best_r
                if cand > ans:
                    ans = cand
        return ans

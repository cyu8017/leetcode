# LeetCode 2907 - Maximum Profitable Triplets With Increasing Prices I
# https://leetcode.com/problems/maximum-profitable-triplets-with-increasing-prices-i/

from typing import List


class Solution:
    def maxProfit(self, prices: List[int], profits: List[int]) -> int:
        n = len(prices)
        ans = -1
        for j in range(n):
            best_l = -1
            best_r = -1
            for i in range(j):
                if prices[i] < prices[j] and profits[i] > best_l:
                    best_l = profits[i]
            for k in range(j + 1, n):
                if prices[k] > prices[j] and profits[k] > best_r:
                    best_r = profits[k]
            if best_l >= 0 and best_r >= 0:
                cand = best_l + profits[j] + best_r
                if cand > ans:
                    ans = cand
        return ans

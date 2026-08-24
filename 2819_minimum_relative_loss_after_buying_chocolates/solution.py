# LeetCode 2819 - Minimum Relative Loss After Buying Chocolates
# https://leetcode.com/problems/minimum-relative-loss-after-buying-chocolates/

from typing import List


class Solution:
    def minimumRelativeLosses(self, prices: List[int], queries: List[List[int]]) -> List[int]:
        prices = sorted(prices)
        n = len(prices)
        ans = [0] * len(queries)
        for qi, (kk, m) in enumerate(queries):
            losses = [0] * n
            for i in range(n):
                if prices[i] <= kk:
                    losses[i] = prices[i]
                else:
                    losses[i] = 2 * kk - prices[i]
            losses.sort()
            total = 0
            for i in range(m):
                total += losses[i]
            ans[qi] = total
        return ans

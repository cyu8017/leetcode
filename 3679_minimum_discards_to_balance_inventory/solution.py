# LeetCode 3679 - Minimum Discards to Balance Inventory
# https://leetcode.com/problems/minimum-discards-to-balance-inventory/

from typing import List


class Solution:
    def minArrivalsToDiscard(self, arrivals: List[int], w: int, m: int) -> int:
        cnt = {}
        n = len(arrivals)
        marked = [0] * n
        ans = 0
        for i in range(n):
            x = arrivals[i]
            if i >= w:
                cnt[arrivals[i - w]] = cnt.get(arrivals[i - w], 0) - marked[i - w]
            if cnt.get(x, 0) >= m:
                ans += 1
            else:
                marked[i] = 1
                cnt[x] = cnt.get(x, 0) + 1
        return ans

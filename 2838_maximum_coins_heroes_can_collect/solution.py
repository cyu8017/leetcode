# LeetCode 2838 - Maximum Coins Heroes Can Collect
# https://leetcode.com/problems/maximum-coins-heroes-can-collect/

from typing import List


class Solution:
    def maximumCoins(self, heroes: List[int], monsters: List[int], coins: List[int]) -> List[int]:
        n = len(monsters)
        idx = list(range(n))
        idx.sort(key=lambda i: monsters[i])
        pref = [0] * (n + 1)
        ms = [0] * n
        for i in range(n):
            ms[i] = monsters[idx[i]]
            pref[i + 1] = pref[i] + coins[idx[i]]

        def upper_bound(a: List[int], x: int) -> int:
            lo, hi = 0, len(a)
            while lo < hi:
                mid = (lo + hi) >> 1
                if a[mid] <= x:
                    lo = mid + 1
                else:
                    hi = mid
            return lo

        return [pref[upper_bound(ms, h)] for h in heroes]

# LeetCode 3413 - Maximum Coins From K Consecutive Bags
# https://leetcode.com/problems/maximum-coins-from-k-consecutive-bags/

from typing import List


class Solution:
    def maximumCoins(self, coins: List[List[int]], k: int) -> int:
        coins = sorted(coins, key=lambda a: a[0])
        ans = 0
        n = len(coins)
        for i in range(n):
            s = 0
            start = coins[i][0]
            end = start + k - 1
            j = i
            while j < n and coins[j][0] <= end:
                l = coins[j][0]
                r = coins[j][1]
                if r > end:
                    r = end
                if l < start:
                    l = start
                if l <= r:
                    s += (r - l + 1) * coins[j][2]
                j += 1
            if s > ans:
                ans = s
        for i in range(n):
            s = 0
            end = coins[i][1]
            start = end - k + 1
            for j in range(i + 1):
                l = coins[j][0]
                r = coins[j][1]
                if l < start:
                    l = start
                if r > end:
                    r = end
                if l <= r:
                    s += (r - l + 1) * coins[j][2]
            if s > ans:
                ans = s
        return ans

# LeetCode 2931 - Maximum Spending After Buying Items
# https://leetcode.com/problems/maximum-spending-after-buying-items/

from typing import List


class Solution:
    def maxSpending(self, values: List[List[int]]) -> int:
        m, n = len(values), len(values[0])
        idx = [n - 1] * m
        ans = 0
        day = 1
        total = m * n
        for _ in range(total):
            best_i = -1
            best_v = 10**18
            for i in range(m):
                if idx[i] >= 0 and values[i][idx[i]] < best_v:
                    best_v = values[i][idx[i]]
                    best_i = i
            ans += best_v * day
            idx[best_i] -= 1
            day += 1
        return ans

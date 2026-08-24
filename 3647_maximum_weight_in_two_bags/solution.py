# LeetCode 3647 - Maximum Weight in Two Bags
# https://leetcode.com/problems/maximum-weight-in-two-bags/

from typing import List


class Solution:
    def maxWeight(self, weights: List[int], w1: int, w2: int) -> int:
        f = [[0] * (w2 + 1) for _ in range(w1 + 1)]
        for x in weights:
            for j in range(w1, -1, -1):
                for k in range(w2, -1, -1):
                    if x <= j:
                        f[j][k] = max(f[j][k], f[j - x][k] + x)
                    if x <= k:
                        f[j][k] = max(f[j][k], f[j][k - x] + x)
        return f[w1][w2]

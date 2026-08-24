# LeetCode 2836 - Maximize Value of Function in a Ball Passing Game
# https://leetcode.com/problems/maximize-value-of-function-in-a-ball-passing-game/

from typing import List


class Solution:
    def getMaxFunctionValue(self, receiver: List[int], k: int) -> int:
        n = len(receiver)
        LOG = 36
        up = [[0] * n for _ in range(LOG)]
        sm = [[0] * n for _ in range(LOG)]
        for i in range(n):
            up[0][i] = receiver[i]
            sm[0][i] = receiver[i]
        for j in range(1, LOG):
            for i in range(n):
                mid = up[j - 1][i]
                up[j][i] = up[j - 1][mid]
                sm[j][i] = sm[j - 1][i] + sm[j - 1][mid]
        ans = 0
        for i in range(n):
            cur = i
            total = i
            kk = k
            for j in range(LOG):
                if kk & (1 << j):
                    total += sm[j][cur]
                    cur = up[j][cur]
            if total > ans:
                ans = total
        return ans

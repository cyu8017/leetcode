# LeetCode 3693 - Climbing Stairs II
# https://leetcode.com/problems/climbing-stairs-ii/

from typing import List


class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        inf = 10**9
        f = [inf] * (n + 1)
        f[0] = 0
        for i in range(1, n + 1):
            x = costs[i - 1]
            for j in range(max(0, i - 3), i):
                f[i] = min(f[i], f[j] + x + (i - j) * (i - j))
        return f[n]

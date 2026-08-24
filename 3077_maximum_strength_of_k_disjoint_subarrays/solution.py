# LeetCode 3077 - Maximum Strength of K Disjoint Subarrays
# https://leetcode.com/problems/maximum-strength-of-k-disjoint-subarrays/

from typing import List


class Solution:
    def maximumStrength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        INF = -(1 << 53) // 2
        f = [[[INF, INF] for _ in range(k + 1)] for _ in range(n + 1)]
        f[0][0][0] = 0
        for i in range(1, n + 1):
            x = nums[i - 1]
            for j in range(k + 1):
                sign = 1 if (j & 1) != 0 else -1
                val = sign * x * (k - j + 1)
                f[i][j][0] = max(f[i - 1][j][0], f[i - 1][j][1])
                f[i][j][1] = max(f[i][j][1], f[i - 1][j][1] + val)
                if j > 0:
                    t = max(f[i - 1][j - 1][0], f[i - 1][j - 1][1]) + val
                    f[i][j][1] = max(f[i][j][1], t)
        return max(f[n][k][0], f[n][k][1])

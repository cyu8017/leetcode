# LeetCode 3743 - Maximize Cyclic Partition Score
# https://leetcode.com/problems/maximize-cyclic-partition-score/

from typing import List


class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        a = nums + nums
        if k > n:
            k = n
        best = 0
        NEG = -(10**18)
        for start in range(n):
            seg = a[start:start + n]
            dp = [[NEG] * (k + 1) for _ in range(n + 1)]
            dp[0][0] = 0
            for i in range(1, n + 1):
                for j in range(1, min(k, i) + 1):
                    mx = NEG
                    for t in range(i, j - 1, -1):
                        if seg[t - 1] > mx:
                            mx = seg[t - 1]
                        if dp[t - 1][j - 1] > NEG:
                            cand = dp[t - 1][j - 1] + mx
                            if cand > dp[i][j]:
                                dp[i][j] = cand
            if dp[n][k] > best:
                best = dp[n][k]
        return best

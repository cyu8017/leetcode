# LeetCode 3290 - Maximum Multiplication Score
# https://leetcode.com/problems/maximum-multiplication-score/

from typing import List


class Solution:
    def maxScore(self, a: List[int], b: List[int]) -> int:
        neg = -(1 << 62)
        dp = [0, neg, neg, neg, neg]
        for x in b:
            for k in range(4, 0, -1):
                if dp[k - 1] == neg:
                    continue
                v = dp[k - 1] + a[k - 1] * x
                if v > dp[k]:
                    dp[k] = v
        return dp[4]

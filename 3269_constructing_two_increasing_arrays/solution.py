# LeetCode 3269 - Constructing Two Increasing Arrays
# https://leetcode.com/problems/constructing-two-increasing-arrays/

from typing import List


class Solution:
    def minLargest(self, nums1: List[int], nums2: List[int]) -> int:
        n, m = len(nums1), len(nums2)
        inf = 1000000000
        dp = [[inf] * (m + 1) for _ in range(n + 1)]
        dp[0][0] = 0
        for i in range(n + 1):
            for j in range(m + 1):
                if dp[i][j] == inf:
                    continue
                prev = dp[i][j]
                if i < n:
                    need = prev + 1
                    if nums1[i] == 0:
                        if need % 2 != 0:
                            need += 1
                    else:
                        if need % 2 == 0:
                            need += 1
                    if need < dp[i + 1][j]:
                        dp[i + 1][j] = need
                if j < m:
                    need = prev + 1
                    if nums2[j] == 0:
                        if need % 2 != 0:
                            need += 1
                    else:
                        if need % 2 == 0:
                            need += 1
                    if need < dp[i][j + 1]:
                        dp[i][j + 1] = need
        return dp[n][m]

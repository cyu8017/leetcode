# LeetCode 2809 - Minimum Time to Make Array Sum At Most x
# https://leetcode.com/problems/minimum-time-to-make-array-sum-at-most-x/

from typing import List


class Solution:
    def minimumTime(self, nums1: List[int], nums2: List[int], x: int) -> int:
        n = len(nums1)
        arr = [[nums1[i], nums2[i]] for i in range(n)]
        sum1 = sum(nums1)
        sum2 = sum(nums2)
        arr.sort(key=lambda p: p[1])
        dp = [0] * (n + 1)
        for i in range(n):
            for j in range(i + 1, 0, -1):
                dp[j] = max(dp[j], dp[j - 1] + arr[i][0] + j * arr[i][1])
        for t in range(n + 1):
            if sum1 + sum2 * t - dp[t] <= x:
                return t
        return -1

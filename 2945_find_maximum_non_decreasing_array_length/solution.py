# LeetCode 2945 - Find Maximum Non-decreasing Array Length
# https://leetcode.com/problems/find-maximum-non-decreasing-array-length/

from typing import List


class Solution:
    def findMaximumLength(self, nums: List[int]) -> int:
        n = len(nums)
        pref = [0] * (n + 1)
        last = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + nums[i]
        dp = [0] * (n + 1)
        dq = [[0, 0]]
        for i in range(1, n + 1):
            while len(dq) > 1 and dq[1][1] <= pref[i]:
                dq.pop(0)
            j = dq[0][0]
            dp[i] = dp[j] + 1
            last[i] = pref[i] - pref[j]
            val = pref[i] + last[i]
            while dq and dq[-1][1] >= val:
                dq.pop()
            dq.append([i, val])
        return dp[n]

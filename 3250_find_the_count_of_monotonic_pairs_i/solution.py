# LeetCode 3250 - Find the Count of Monotonic Pairs I
# https://leetcode.com/problems/find-the-count-of-monotonic-pairs-i/

from typing import List


class Solution:
    def countOfPairs(self, nums: List[int]) -> int:
        mod = 1000000007
        n = len(nums)
        dp = [0] * 51
        for a in range(nums[0] + 1):
            dp[a] = 1
        for i in range(1, n):
            ndp = [0] * 51
            pref = [0] * 52
            for a in range(51):
                pref[a + 1] = (pref[a] + dp[a]) % mod
            for a2 in range(nums[i] + 1):
                b2 = nums[i] - a2
                maxA1 = a2
                lim = nums[i - 1] - b2
                if lim < maxA1:
                    maxA1 = lim
                if maxA1 < 0:
                    continue
                if maxA1 > 50:
                    maxA1 = 50
                ndp[a2] = pref[maxA1 + 1]
            dp = ndp
        ans = 0
        for v in dp:
            ans = (ans + v) % mod
        return ans

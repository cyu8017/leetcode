# LeetCode 3251 - Find the Count of Monotonic Pairs II
# https://leetcode.com/problems/find-the-count-of-monotonic-pairs-ii/

from typing import List


class Solution:
    def countOfPairs(self, nums: List[int]) -> int:
        mod = 1000000007
        n = len(nums)
        maxV = 0
        for v in nums:
            maxV = max(maxV, v)
        dp = [0] * (maxV + 1)
        for a in range(nums[0] + 1):
            dp[a] = 1
        for i in range(1, n):
            ndp = [0] * (maxV + 1)
            pref = [0] * (maxV + 2)
            for a in range(maxV + 1):
                pref[a + 1] = (pref[a] + dp[a]) % mod
            for a2 in range(nums[i] + 1):
                b2 = nums[i] - a2
                maxA1 = a2
                lim = nums[i - 1] - b2
                if lim < maxA1:
                    maxA1 = lim
                if maxA1 < 0:
                    continue
                if maxA1 > maxV:
                    maxA1 = maxV
                ndp[a2] = pref[maxA1 + 1]
            dp = ndp
        ans = 0
        for v in dp:
            ans = (ans + v) % mod
        return ans

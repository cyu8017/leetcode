# LeetCode 2172 - Maximum AND Sum of Array
# https://leetcode.com/problems/maximum-and-sum-of-array/

from typing import List
class Solution:
    def maximumANDSum(self, nums: List[int], numSlots: int) -> int:
        n = len(nums)
        slots = numSlots
        maxMask = 1
        for i in range(slots):
            maxMask *= 3
        dp = [0] * (maxMask)
        for mask in range(maxMask):
            cnt = 0
            x = mask
            while x > 0:
                cnt += x % 3
                x = x // 3
            if cnt >= n:
                continue
            v = nums[cnt]
            bas = 1
            for s in range(1, (slots) + 1):
                occ = mask // bas % 3
                if occ < 2:
                    nm = mask + bas
                    dp[nm] = max(dp[nm], dp[mask] + (v & s))
                bas *= 3
        best = 0
        for v in dp:
            best = max(best, v)
        return best

# LeetCode 2143 - Choose Numbers From Two Arrays in Range
# https://leetcode.com/problems/choose-numbers-from-two-arrays-in-range/

from typing import List
class Solution:
    def countSubranges(self, nums1: List[int], nums2: List[int]) -> int:
        MOD = 1000000007
        n = len(nums1)
        ans = 0
        dp = {}
        for i in range(n):
            ndp = {}
            ndp[nums1[i]] = ((ndp.get(nums1[i]) or 0) + 1) % MOD
            ndp[-nums2[i]] = ((ndp.get(-nums2[i]) or 0) + 1) % MOD
            for diff, cnt in dp.items():
                ndp[diff + nums1[i]] = ((ndp.get(diff + nums1[i]) or 0) + cnt) % MOD
                ndp[diff - nums2[i]] = ((ndp.get(diff - nums2[i]) or 0) + cnt) % MOD
            dp = ndp
            ans = (ans + (dp.get(0) or 0)) % MOD
        return ans

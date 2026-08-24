# LeetCode 2681 - Power of Heroes
# https://leetcode.com/problems/power-of-heroes/

from typing import List


class Solution:
    def sumOfPower(self, nums: List[int]) -> int:
        MOD = 1000000007
        nums = sorted(nums)
        ans, s = 0, 0
        for x in nums:
            ans = (ans + ((s + x) % MOD) * x % MOD * x) % MOD
            s = (s * 2 + x) % MOD
        return ans

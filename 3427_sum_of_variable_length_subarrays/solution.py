# LeetCode 3427 - Sum of Variable Length Subarrays
# https://leetcode.com/problems/sum-of-variable-length-subarrays/

from typing import List


class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        n = len(nums)
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + nums[i]
        ans = 0
        for i in range(n):
            start = i - nums[i]
            if start < 0:
                start = 0
            ans += pref[i + 1] - pref[start]
        return ans

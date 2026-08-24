# LeetCode 2871 - Split Array Into Maximum Number of Subarrays
# https://leetcode.com/problems/split-array-into-maximum-number-of-subarrays/

from typing import List


class Solution:
    def maxSubarrays(self, nums: List[int]) -> int:
        ans = 0
        cur = -1
        for v in nums:
            if cur == -1:
                cur = v
            else:
                cur &= v
            if cur == 0:
                ans += 1
                cur = -1
        return 1 if ans == 0 else ans

# LeetCode 2419 - Longest Subarray With Maximum Bitwise AND
# https://leetcode.com/problems/longest-subarray-with-maximum-bitwise-and/

from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        mx = nums[0]
        for x in nums:
            if x > mx:
                mx = x
        ans = cur = 0
        for x in nums:
            if x == mx:
                cur += 1
                ans = max(ans, cur)
            else:
                cur = 0
        return ans

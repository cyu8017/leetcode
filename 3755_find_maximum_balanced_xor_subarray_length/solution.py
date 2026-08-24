# LeetCode 3755 - Find Maximum Balanced XOR Subarray Length
# https://leetcode.com/problems/find-maximum-balanced-xor-subarray-length/

from typing import List


class Solution:
    def maxBalancedSubarray(self, nums: List[int]) -> int:
        d = {}
        a = 0
        b = len(nums)
        ans = 0
        d[b] = -1
        for i, x in enumerate(nums):
            a ^= x
            if x % 2 == 0:
                b += 1
            else:
                b -= 1
            key = (a << 32) | (b & 0xFFFFFFFF)
            if key in d:
                ans = max(ans, i - d[key])
            else:
                d[key] = i
        return ans

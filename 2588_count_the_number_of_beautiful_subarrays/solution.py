# LeetCode 2588 - Count the Number of Beautiful Subarrays
# https://leetcode.com/problems/count-the-number-of-beautiful-subarrays/

from typing import List


class Solution:
    def beautifulSubarrays(self, nums: List[int]) -> int:
        freq = {0: 1}
        xorv = 0
        ans = 0
        for x in nums:
            xorv ^= x
            ans += freq.get(xorv, 0)
            freq[xorv] = freq.get(xorv, 0) + 1
        return ans

# LeetCode 0260 - Single Number III
# https://leetcode.com/problems/single-number-iii/

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor_all = 0
        for num in nums:
            xor_all ^= num
        diff = xor_all & -xor_all
        first = second = 0
        for num in nums:
            if num & diff:
                first ^= num
            else:
                second ^= num
        return [first, second]

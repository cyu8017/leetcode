# LeetCode 2980 - Check if Bitwise OR Has Trailing Zeros
# https://leetcode.com/problems/check-if-bitwise-or-has-trailing-zeros/

from typing import List


class Solution:
    def hasTrailingZeros(self, nums: List[int]) -> bool:
        even = 0
        for v in nums:
            if v % 2 == 0:
                even += 1
                if even >= 2:
                    return True
        return False

# LeetCode 2317 - Maximum XOR After Operations
# https://leetcode.com/problems/maximum-xor-after-operations/

from typing import List


class Solution:
    def maximumXOR(self, nums: List[int]) -> int:
        ans = 0
        for x in nums:
            ans |= x
        return ans

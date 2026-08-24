# LeetCode 3513 - Number of Unique XOR Triplets I
# https://leetcode.com/problems/number-of-unique-xor-triplets-i/

from typing import List


class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return n
        x = n
        length = 0
        while x != 0:
            length += 1
            x >>= 1
        return 1 << length

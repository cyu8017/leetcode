# LeetCode 0421 - Maximum XOR of Two Numbers in an Array
# https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/

from typing import List


class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        maximum = max(nums)
        max_bit = maximum.bit_length()
        root: dict[int, dict] = {}
        best = 0

        for number in nums:
            node = root
            for bit in range(max_bit - 1, -1, -1):
                current = (number >> bit) & 1
                if current not in node:
                    node[current] = {}
                node = node[current]

        for number in nums:
            node = root
            candidate = 0
            for bit in range(max_bit - 1, -1, -1):
                current = (number >> bit) & 1
                target = 1 - current
                if target in node:
                    candidate |= 1 << bit
                    node = node[target]
                else:
                    node = node[current]
            best = max(best, candidate)

        return best

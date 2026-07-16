# LeetCode 0717 - 1-bit and 2-bit Characters
# https://leetcode.com/problems/1-bit-and-2-bit-characters/

from typing import List


class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        i = 0
        n = len(bits)
        while i < n - 1:
            i += 2 if bits[i] == 1 else 1
        return i == n - 1

# LeetCode 2683 - Neighboring Bitwise XOR
# https://leetcode.com/problems/neighboring-bitwise-xor/

from typing import List


class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        x = 0
        for v in derived:
            x ^= v
        return x == 0

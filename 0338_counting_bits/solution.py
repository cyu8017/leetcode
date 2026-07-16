# LeetCode 0338 - Counting Bits
# https://leetcode.com/problems/counting-bits/

from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        result = [0] * (n + 1)
        for index in range(1, n + 1):
            result[index] = result[index & (index - 1)] + 1
        return result

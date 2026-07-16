# LeetCode 0393 - UTF-8 Validation
# https://leetcode.com/problems/utf-8-validation/

from typing import List


class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        remaining = 0

        for byte in data:
            byte &= 0xFF
            if remaining == 0:
                if byte >> 7 == 0b0:
                    continue
                if byte >> 5 == 0b110:
                    remaining = 1
                elif byte >> 4 == 0b1110:
                    remaining = 2
                elif byte >> 3 == 0b11110:
                    remaining = 3
                else:
                    return False
            else:
                if byte >> 6 != 0b10:
                    return False
                remaining -= 1

        return remaining == 0

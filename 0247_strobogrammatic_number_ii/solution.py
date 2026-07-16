# LeetCode 0247 - Strobogrammatic Number II
# https://leetcode.com/problems/strobogrammatic-number-ii/

from typing import List


class Solution:
    PAIRS = [("0", "0"), ("1", "1"), ("6", "9"), ("8", "8"), ("9", "6")]

    def findStrobogrammatic(self, n: int) -> List[str]:
        def build(left: int, right: int) -> list[str]:
            if left > right:
                return [""]
            if left == right:
                return ["0", "1", "8"]
            result: list[str] = []
            for start, end in self.PAIRS:
                if left == 0 and start == "0":
                    continue
                for middle in build(left + 1, right - 1):
                    result.append(start + middle + end)
            return result

        return build(0, n - 1)

# LeetCode 0248 - Strobogrammatic Number III
# https://leetcode.com/problems/strobogrammatic-number-iii/


class Solution:
    PAIRS = [("0", "0"), ("1", "1"), ("6", "9"), ("8", "8"), ("9", "6")]

    def strobogrammaticInRange(self, low: str, high: str) -> int:
        count = 0
        for length in range(len(low), len(high) + 1):
            for value in self._build(0, length - 1):
                if int(low) <= int(value) <= int(high):
                    count += 1
        return count

    def _build(self, left: int, right: int) -> list[str]:
        if left > right:
            return [""]
        if left == right:
            return ["0", "1", "8"]
        result: list[str] = []
        for start, end in self.PAIRS:
            if left == 0 and start == "0":
                continue
            for middle in self._build(left + 1, right - 1):
                result.append(start + middle + end)
        return result

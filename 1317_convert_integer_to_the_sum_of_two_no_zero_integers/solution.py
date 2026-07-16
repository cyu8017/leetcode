# LeetCode 1317 - Convert Integer To The Sum Of Two No Zero Integers

from typing import List

class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        def valid(value):
            return "0" not in str(value)
        for first in range(1, n):
            if valid(first) and valid(n - first):
                return [first, n - first]
        return []

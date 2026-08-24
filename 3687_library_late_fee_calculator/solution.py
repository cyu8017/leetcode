# LeetCode 3687 - Library Late Fee Calculator
# https://leetcode.com/problems/library-late-fee-calculator/

from typing import List


class Solution:
    def lateFee(self, daysLate: List[int]) -> int:
        def fee(x: int) -> int:
            if x == 1:
                return 1
            if x > 5:
                return 3 * x
            return 2 * x

        return sum(fee(x) for x in daysLate)

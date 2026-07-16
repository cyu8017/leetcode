from typing import List


class Solution:
    def maxSumAfterOperation(self, nums: List[int]) -> int:
        no_square = 0
        one_square = 0
        best = -10 ** 18
        for value in nums:
            one_square = max(one_square + value, no_square + value * value, value * value)
            no_square = max(no_square + value, value)
            best = max(best, one_square)
        return best

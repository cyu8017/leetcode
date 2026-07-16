from typing import List


class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        prefix = 0
        low = high = 0
        for value in nums:
            prefix += value
            low = min(low, prefix)
            high = max(high, prefix)
        return high - low

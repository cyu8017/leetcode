class Solution:
    def minStartValue(self, nums):
        prefix = lowest = 0
        for value in nums:
            prefix += value
            lowest = min(lowest, prefix)
        return 1 - lowest

from typing import List

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return sum(len(str(value)) % 2 == 0 for value in nums)

from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        return sum(x.bit_count() for x in nums) + max((x.bit_length() - 1 for x in nums), default=0)

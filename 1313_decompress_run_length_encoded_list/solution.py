# LeetCode 1313 - Decompress Run Length Encoded List

from typing import List

class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        return [value for i in range(0, len(nums), 2) for value in [nums[i + 1]] * nums[i]]

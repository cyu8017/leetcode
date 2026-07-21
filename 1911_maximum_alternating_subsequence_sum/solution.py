from typing import List

class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        even = odd = 0
        for x in nums:
            even, odd = max(even, odd + x), max(odd, even - x)
        return even

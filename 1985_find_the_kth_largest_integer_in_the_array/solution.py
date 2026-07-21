from typing import List

class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        return sorted(nums, key=lambda x: (len(x), x), reverse=True)[k - 1]

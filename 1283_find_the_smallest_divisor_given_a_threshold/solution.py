from typing import List

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        lo, hi = 1, max(nums)
        while lo < hi:
            mid = (lo + hi) // 2
            if sum((x + mid - 1) // mid for x in nums) <= threshold:
                hi = mid
            else:
                lo = mid + 1
        return lo

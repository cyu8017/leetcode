from typing import List

class Solution:
    def kthSmallestSubarraySum(self, nums: List[int], k: int) -> int:
        def count(limit: int) -> int:
            total = left = ans = 0
            for right, value in enumerate(nums):
                total += value
                while total > limit:
                    total -= nums[left]
                    left += 1
                ans += right - left + 1
            return ans

        lo, hi = min(nums), sum(nums)
        while lo < hi:
            mid = (lo + hi) // 2
            if count(mid) >= k:
                hi = mid
            else:
                lo = mid + 1
        return lo

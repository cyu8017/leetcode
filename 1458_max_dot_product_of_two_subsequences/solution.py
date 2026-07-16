from typing import List, Optional

class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums2)
        dp = [float("-inf")] * (n + 1)
        for a in nums1:
            prev = dp[:]
            for j, b in enumerate(nums2, 1):
                product = a * b
                dp[j] = max(dp[j-1], prev[j], product, product + max(0, prev[j-1]))
        return int(dp[n])

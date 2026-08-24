# LeetCode 3584 - Maximum Product of First and Last Elements of a Subsequence
# https://leetcode.com/problems/maximum-product-of-first-and-last-elements-of-a-subsequence/

from typing import List


class Solution:
    def maximumProduct(self, nums: List[int], m: int) -> int:
        ans = -(10**18)
        mx = -(10**18)
        mi = 10**18
        for i in range(m - 1, len(nums)):
            x = nums[i]
            y = nums[i - m + 1]
            mi = min(mi, y)
            mx = max(mx, y)
            ans = max(ans, max(x * mi, x * mx))
        return ans

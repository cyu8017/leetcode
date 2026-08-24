# LeetCode 2892 - Minimizing Array After Replacing Pairs With Their Product
# https://leetcode.com/problems/minimizing-array-after-replacing-pairs-with-their-product/

from typing import List


class Solution:
    def minArrayLength(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        ans = 1
        prod = nums[0]
        for i in range(1, len(nums)):
            if prod <= k and nums[i] <= k and (nums[i] == 0 or prod <= k // nums[i]):
                prod *= nums[i]
            else:
                ans += 1
                prod = nums[i]
        return ans

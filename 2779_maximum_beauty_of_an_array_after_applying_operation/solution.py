# LeetCode 2779 - Maximum Beauty of an Array After Applying Operation
# https://leetcode.com/problems/maximum-beauty-of-an-array-after-applying-operation/

from typing import List


class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = 0
        left = 0
        for right in range(len(nums)):
            while nums[right] - nums[left] > 2 * k:
                left += 1
            ans = max(ans, right - left + 1)
        return ans

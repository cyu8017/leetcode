# LeetCode 2149 - Rearrange Array Elements by Sign
# https://leetcode.com/problems/rearrange-array-elements-by-sign/

from typing import List
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        ans = [None] * (len(nums))
        pos = 0
        neg = 1
        for x in nums:
            if x > 0:
                ans[pos] = x
                pos += 2
            else:
                ans[neg] = x
                neg += 2
        return ans

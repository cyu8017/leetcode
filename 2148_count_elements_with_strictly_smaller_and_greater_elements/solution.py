# LeetCode 2148 - Count Elements With Strictly Smaller and Greater Elements
# https://leetcode.com/problems/count-elements-with-strictly-smaller-and-greater-elements/

from typing import List
class Solution:
    def countElements(self, nums: List[int]) -> int:
        mn = nums[0]
        mx = nums[0]
        for x in nums:
            mn = min(mn, x)
            mx = max(mx, x)
        ans = 0
        for x in nums:
            if x > mn and x < mx:
                ans += 1
        return ans

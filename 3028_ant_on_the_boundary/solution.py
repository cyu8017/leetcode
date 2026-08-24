# LeetCode 3028 - Ant on the Boundary
# https://leetcode.com/problems/ant-on-the-boundary/

from typing import List


class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        s = 0
        ans = 0
        for x in nums:
            s += x
            if s == 0:
                ans += 1
        return ans

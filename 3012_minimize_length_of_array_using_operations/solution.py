# LeetCode 3012 - Minimize Length of Array Using Operations
# https://leetcode.com/problems/minimize-length-of-array-using-operations/

from typing import List


class Solution:
    def minimumArrayLength(self, nums: List[int]) -> int:
        mi = nums[0]
        for x in nums:
            if x < mi:
                mi = x
        cnt = 0
        for x in nums:
            if x % mi != 0:
                return 1
            if x == mi:
                cnt += 1
        return (cnt + 1) // 2

# LeetCode 3834 - Merge Adjacent Equal Elements
# https://leetcode.com/problems/merge-adjacent-equal-elements/

from typing import List


class Solution:
    def mergeAdjacent(self, nums: List[int]) -> List[int]:
        stk = []
        for x in nums:
            stk.append(x)
            while len(stk) > 1 and stk[-1] == stk[-2]:
                a = stk.pop()
                b = stk.pop()
                stk.append(a + b)
        return stk

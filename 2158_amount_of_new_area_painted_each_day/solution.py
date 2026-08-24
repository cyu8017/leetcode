# LeetCode 2158 - Amount of New Area Painted Each Day
# https://leetcode.com/problems/amount-of-new-area-painted-each-day/

from typing import List
class Solution:
    def amountPainted(self, paint: List[List[int]]) -> List[int]:
        ans = [0] * (len(paint))
        line = [0] * (50001)
        for i in range(len(paint)):
            start = paint[i][0]
            end = paint[i][1]
            j = start
            while j < end:
                if line[j] == 0:
                    ans[i] += 1
                    line[j] = end
                    j += 1
                else:
                    next = line[j]
                    line[j] = max(end, next)
                    j = next
        return ans

# LeetCode 2610 - Convert an Array Into a 2D Array With Conditions
# https://leetcode.com/problems/convert-an-array-into-a-2d-array-with-conditions/

from typing import List


class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        freq = {}
        ans = []
        for x in nums:
            f = freq.get(x, 0)
            if f == len(ans):
                ans.append([])
            ans[f].append(x)
            freq[x] = f + 1
        return ans

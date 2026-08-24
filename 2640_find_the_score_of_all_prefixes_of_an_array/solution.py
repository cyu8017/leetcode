# LeetCode 2640 - Find the Score of All Prefixes of an Array
# https://leetcode.com/problems/find-the-score-of-all-prefixes-of-an-array/

from typing import List


class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        mx = 0
        s = 0
        for i, x in enumerate(nums):
            if x > mx:
                mx = x
            s += x + mx
            ans[i] = s
        return ans

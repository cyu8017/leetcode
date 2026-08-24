# LeetCode 2206 - Divide Array Into Equal Pairs
# https://leetcode.com/problems/divide-array-into-equal-pairs/

from typing import List
class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        freq = {}
        for x in nums:
            freq[x] = (freq.get(x) or 0) + 1
        for c in list(freq.values()):
            if c % 2 != 0:
                return False
        return True

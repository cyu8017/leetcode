# LeetCode 2150 - Find All Lonely Numbers in the Array
# https://leetcode.com/problems/find-all-lonely-numbers-in-the-array/

from typing import List
class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        freq = {}
        for x in nums:
            freq[x] = (freq.get(x) or 0) + 1
        ans = []
        for k, v in freq.items():
            if v == 1 and k - 1 not in freq and k + 1 not in freq:
                ans.append(k)
        return ans

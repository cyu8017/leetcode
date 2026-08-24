# LeetCode 2190 - Most Frequent Number Following Key In an Array
# https://leetcode.com/problems/most-frequent-number-following-key-in-an-array/

from typing import List
class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        freq = {}
        best = 0
        ans = 0
        i = 0
        while i + 1 < len(nums):
            if nums[i] == key:
                v = (freq.get(nums[i + 1]) or 0) + 1
                freq[nums[i + 1]] = v
                if v > best:
                    best = v
                    ans = nums[i + 1]
            i += 1
        return ans

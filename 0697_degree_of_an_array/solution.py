# LeetCode 0697 - Degree of an Array
# https://leetcode.com/problems/degree-of-an-array/

from typing import List


class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        first: dict[int, int] = {}
        last: dict[int, int] = {}
        count: dict[int, int] = {}
        for i, num in enumerate(nums):
            if num not in first:
                first[num] = i
            last[num] = i
            count[num] = count.get(num, 0) + 1

        degree = max(count.values())
        return min(last[num] - first[num] + 1 for num, freq in count.items() if freq == degree)

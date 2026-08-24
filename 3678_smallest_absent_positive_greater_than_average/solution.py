# LeetCode 3678 - Smallest Absent Positive Greater Than Average
# https://leetcode.com/problems/smallest-absent-positive-greater-than-average/

from typing import List


class Solution:
    def smallestAbsent(self, nums: List[int]) -> int:
        s = set()
        total = 0
        for x in nums:
            s.add(x)
            total += x
        ans = max(1, total // len(nums) + 1)
        while ans in s:
            ans += 1
        return ans

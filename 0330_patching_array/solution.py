# LeetCode 0330 - Patching Array
# https://leetcode.com/problems/patching-array/

from typing import List


class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        patches = 0
        miss = 1
        index = 0
        while miss <= n:
            if index < len(nums) and nums[index] <= miss:
                miss += nums[index]
                index += 1
            else:
                miss += miss
                patches += 1
        return patches

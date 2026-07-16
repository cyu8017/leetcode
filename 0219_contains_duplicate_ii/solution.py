# LeetCode 0219 - Contains Duplicate II
# https://leetcode.com/problems/contains-duplicate-ii/

from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        last_index: dict[int, int] = {}
        for i, num in enumerate(nums):
            if num in last_index and i - last_index[num] <= k:
                return True
            last_index[num] = i
        return False

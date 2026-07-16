# LeetCode 0740 - Delete and Earn
# https://leetcode.com/problems/delete-and-earn/

from typing import List


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if not nums:
            return 0
        max_num = max(nums)
        points = [0] * (max_num + 1)
        for num in nums:
            points[num] += num

        take = skip = 0
        for value in points:
            take, skip = skip + value, max(skip, take)
        return max(take, skip)

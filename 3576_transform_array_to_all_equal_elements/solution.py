# LeetCode 3576 - Transform Array to All Equal Elements
# https://leetcode.com/problems/transform-array-to-all-equal-elements/

from typing import List


def check3576(nums: List[int], target: int, kk: int) -> bool:
    cnt = 0
    sign = 1
    for i in range(len(nums) - 1):
        x = nums[i] * sign
        if x == target:
            sign = 1
        else:
            sign = -1
            cnt += 1
    return cnt <= kk and nums[-1] * sign == target


class Solution:
    def canMakeEqual(self, nums: List[int], k: int) -> bool:
        return check3576(nums, nums[0], k) or check3576(nums, -nums[0], k)

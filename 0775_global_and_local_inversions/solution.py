# LeetCode 0775 - Global and Local Inversions
# https://leetcode.com/problems/global-and-local-inversions/

from typing import List


class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        return all(abs(nums[i] - i) <= 1 for i in range(len(nums)))

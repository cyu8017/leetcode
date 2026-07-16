# LeetCode 0300 - Longest Increasing Subsequence
# https://leetcode.com/problems/longest-increasing-subsequence/

from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        piles: list[int] = []
        for num in nums:
            left, right = 0, len(piles)
            while left < right:
                mid = (left + right) // 2
                if piles[mid] < num:
                    left = mid + 1
                else:
                    right = mid
            if left == len(piles):
                piles.append(num)
            else:
                piles[left] = num
        return len(piles)

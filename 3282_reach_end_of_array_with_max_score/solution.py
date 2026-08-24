# LeetCode 3282 - Reach End of Array With Max Score
# https://leetcode.com/problems/reach-end-of-array-with-max-score/

from typing import List


class Solution:
    def findMaximumScore(self, nums: List[int]) -> int:
        ans, maxV = 0, 0
        for i in range(len(nums) - 1):
            if nums[i] > maxV:
                maxV = nums[i]
            ans += maxV
        return ans

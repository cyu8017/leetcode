# LeetCode 0487 - Max Consecutive Ones II
# https://leetcode.com/problems/max-consecutive-ones-ii/

class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        left = best = zeros = 0
        for right, num in enumerate(nums):
            if num == 0:
                zeros += 1
            while zeros > 1:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            best = max(best, right - left + 1)
        return best

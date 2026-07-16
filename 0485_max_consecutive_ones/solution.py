# LeetCode 0485 - Max Consecutive Ones
# https://leetcode.com/problems/max-consecutive-ones/

class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        best = current = 0
        for num in nums:
            if num == 1:
                current += 1
                best = max(best, current)
            else:
                current = 0
        return best

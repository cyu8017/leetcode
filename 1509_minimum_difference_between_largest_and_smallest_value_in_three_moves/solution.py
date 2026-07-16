# LeetCode 1509

class Solution:
    def minDifference(self, nums):
        if len(nums) <= 4:
            return 0
        nums.sort()
        return min(nums[-4+i] - nums[i] for i in range(4))

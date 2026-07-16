# LeetCode 1005 - Maximize Sum Of Array After K Negations
# https://leetcode.com/problems/maximize-sum-of-array-after-k-negations/

class Solution:
    def largestSumAfterKNegations(self, nums: list[int], k: int) -> int:
        nums.sort()
        for i in range(len(nums)):
            if k and nums[i] < 0:
                nums[i] = -nums[i]
                k -= 1
        if k % 2:
            nums.sort()
            nums[0] = -nums[0]
        return sum(nums)

# LeetCode 0918 - Maximum Sum Circular Subarray
# https://leetcode.com/problems/maximum-sum-circular-subarray/

class Solution:
    def maxSubarraySumCircular(self, nums: list[int]) -> int:
        total = sum(nums)
        max_sum = min_sum = cur_max = cur_min = nums[0]
        for x in nums[1:]:
            cur_max = max(x, cur_max + x)
            cur_min = min(x, cur_min + x)
            max_sum = max(max_sum, cur_max)
            min_sum = min(min_sum, cur_min)
        if max_sum < 0:
            return max_sum
        return max(max_sum, total - min_sum)

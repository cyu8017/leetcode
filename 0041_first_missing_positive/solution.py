# LeetCode 0041 - First Missing Positive
# https://leetcode.com/problems/first-missing-positive/


class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        n = len(nums)
        i = 0

        while i < n:
            value = nums[i]
            target = value - 1
            if 1 <= value <= n and nums[target] != value:
                nums[i], nums[target] = nums[target], nums[i]
            else:
                i += 1

        for index in range(n):
            if nums[index] != index + 1:
                return index + 1

        return n + 1

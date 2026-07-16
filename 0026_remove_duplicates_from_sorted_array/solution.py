# LeetCode 0026 - Remove Duplicates from Sorted Array
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/


class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0

        write = 1
        for read in range(1, len(nums)):
            if nums[read] != nums[write - 1]:
                nums[write] = nums[read]
                write += 1

        return write

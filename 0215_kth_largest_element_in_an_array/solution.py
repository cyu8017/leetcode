# LeetCode 0215 - Kth Largest Element in an Array
# https://leetcode.com/problems/kth-largest-element-in-an-array/

from typing import List
import random


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        target = len(nums) - k

        def partition(left: int, right: int) -> int:
            pivot = random.randint(left, right)
            nums[pivot], nums[right] = nums[right], nums[pivot]
            store = left
            for i in range(left, right):
                if nums[i] <= nums[right]:
                    nums[store], nums[i] = nums[i], nums[store]
                    store += 1
            nums[store], nums[right] = nums[right], nums[store]
            return store

        left, right = 0, len(nums) - 1
        while left <= right:
            pivot_index = partition(left, right)
            if pivot_index == target:
                return nums[pivot_index]
            if pivot_index < target:
                left = pivot_index + 1
            else:
                right = pivot_index - 1
        return nums[left]

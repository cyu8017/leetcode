# LeetCode 0360 - Sort Transformed Array
# https://leetcode.com/problems/sort-transformed-array/

from typing import List


class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        def transform(value: int) -> int:
            return a * value * value + b * value + c

        left = 0
        right = len(nums) - 1
        result = [0] * len(nums)
        index = len(nums) - 1 if a > 0 else 0
        step = -1 if a > 0 else 1

        while left <= right:
            left_value = transform(nums[left])
            right_value = transform(nums[right])

            if a > 0:
                if left_value > right_value:
                    result[index] = left_value
                    left += 1
                else:
                    result[index] = right_value
                    right -= 1
            elif left_value < right_value:
                result[index] = left_value
                left += 1
            else:
                result[index] = right_value
                right -= 1

            index += step

        return result

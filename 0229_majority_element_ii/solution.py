# LeetCode 0229 - Majority Element II
# https://leetcode.com/problems/majority-element-ii/

from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        candidate1 = candidate2 = None
        count1 = count2 = 0
        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1, count1 = num, 1
            elif count2 == 0:
                candidate2, count2 = num, 1
            else:
                count1 -= 1
                count2 -= 1

        count1 = count2 = 0
        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1

        threshold = len(nums) // 3
        result: list[int] = []
        if count1 > threshold:
            result.append(candidate1)
        if candidate2 != candidate1 and count2 > threshold:
            result.append(candidate2)
        return result

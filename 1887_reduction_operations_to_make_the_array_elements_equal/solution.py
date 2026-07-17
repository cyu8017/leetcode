# LeetCode 1887 - Reduction Operations to Make the Array Elements Equal
# https://leetcode.com/problems/reduction-operations-to-make-the-array-elements-equal/

from typing import List


class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        answer = 0
        rank = 0

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                rank += 1
            answer += rank

        return answer

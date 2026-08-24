# LeetCode 3927 - Minimize Array Sum Using Divisible Replacements
# https://leetcode.com/problems/minimize-array-sum-using-divisible-replacements/

from typing import List


class Solution:
    def minArraySum(self, nums: List[int]) -> int:
        maximum = 0
        present = [False] * 100001
        for value in nums:
            present[value] = True
            if value > maximum:
                maximum = value
        best = [0] * (maximum + 1)
        for divisor in range(1, maximum + 1):
            if not present[divisor]:
                continue
            multiple = divisor
            while multiple <= maximum:
                if best[multiple] == 0:
                    best[multiple] = divisor
                multiple += divisor
        answer = 0
        for value in nums:
            answer += best[value]
        return answer

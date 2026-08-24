# LeetCode 3952 - Maximum Total Value of Covered Indices
# https://leetcode.com/problems/maximum-total-value-of-covered-indices/

from typing import List


class Solution:
    def maxTotalValue(self, nums: List[int], s: str) -> int:
        answer = 0
        i = 0
        while i < len(s):
            if s[i] == "0":
                i += 1
                continue
            start = i
            while i < len(s) and s[i] == "1":
                i += 1
            end = i - 1
            if start == 0:
                for index in range(start, end + 1):
                    answer += nums[index]
                continue
            minimum = nums[start - 1]
            total = 0
            for index in range(start - 1, end + 1):
                total += nums[index]
                if nums[index] < minimum:
                    minimum = nums[index]
            answer += total - minimum
        return answer

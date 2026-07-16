# LeetCode 0370 - Range Addition
# https://leetcode.com/problems/range-addition/

from typing import List


class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        diff = [0] * (length + 1)

        for start, end, inc in updates:
            diff[start] += inc
            if end + 1 < len(diff):
                diff[end + 1] -= inc

        result = [0] * length
        running = 0
        for index in range(length):
            running += diff[index]
            result[index] = running

        return result

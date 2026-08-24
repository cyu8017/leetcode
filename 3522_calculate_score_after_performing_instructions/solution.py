# LeetCode 3522 - Calculate Score After Performing Instructions
# https://leetcode.com/problems/calculate-score-after-performing-instructions/

from typing import List


class Solution:
    def calculateScore(self, instructions: List[str], values: List[int]) -> int:
        n = len(values)
        vis = [False] * n
        ans = 0
        i = 0
        while 0 <= i < n and not vis[i]:
            vis[i] = True
            if instructions[i][0] == "a":
                ans += values[i]
                i += 1
            else:
                i += values[i]
        return ans

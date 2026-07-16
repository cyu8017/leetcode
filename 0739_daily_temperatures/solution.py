# LeetCode 0739 - Daily Temperatures
# https://leetcode.com/problems/daily-temperatures/

from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack: list[int] = []
        for i, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                prev = stack.pop()
                answer[prev] = i - prev
            stack.append(i)
        return answer

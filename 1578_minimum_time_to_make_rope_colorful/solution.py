from typing import List

class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        answer = maximum = 0
        for i, cost in enumerate(neededTime):
            if i and colors[i] != colors[i - 1]:
                maximum = 0
            answer += min(maximum, cost)
            maximum = max(maximum, cost)
        return answer

from typing import List

class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        left, right = toBeRemoved
        answer = []
        for start, end in intervals:
            if end <= left or start >= right:
                answer.append([start, end])
            else:
                if start < left: answer.append([start, left])
                if end > right: answer.append([right, end])
        return answer

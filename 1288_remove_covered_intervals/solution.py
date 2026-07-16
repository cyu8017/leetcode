from typing import List

class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))
        answer = 0
        farthest = -1
        for _, end in intervals:
            if end > farthest:
                answer += 1
                farthest = end
        return answer

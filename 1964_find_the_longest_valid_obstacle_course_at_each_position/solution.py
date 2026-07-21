import bisect
from typing import List

class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        tails: List[int] = []
        ans: List[int] = []
        for x in obstacles:
            i = bisect.bisect_right(tails, x)
            if i == len(tails):
                tails.append(x)
            else:
                tails[i] = x
            ans.append(i + 1)
        return ans

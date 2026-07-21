from typing import List
from collections import defaultdict

class Solution:
    def splitPainting(self, segments: List[List[int]]) -> List[List[int]]:
        diff = defaultdict(int)
        for s, e, c in segments:
            diff[s] += c
            diff[e] -= c
        points = sorted(diff)
        ans = []
        cur = 0
        for i in range(len(points) - 1):
            cur += diff[points[i]]
            if cur:
                ans.append([points[i], points[i + 1], cur])
        return ans

# LeetCode 1331 - Rank Transform Of An Array

from typing import List

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        rank = {value: i + 1 for i, value in enumerate(sorted(set(arr)))}
        return [rank[value] for value in arr]

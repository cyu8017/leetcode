from typing import List
from collections import Counter

class Solution:
    def longestCommonSubsequence(self, arrays: List[List[int]]) -> List[int]:
        cnt = Counter()
        for arr in arrays:
            for x in arr:
                cnt[x] += 1
        m = len(arrays)
        return [x for x in arrays[0] if cnt[x] == m]

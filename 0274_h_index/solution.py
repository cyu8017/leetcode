# LeetCode 0274 - H-Index
# https://leetcode.com/problems/h-index/

from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        buckets = [0] * (len(citations) + 1)
        for citation in citations:
            buckets[min(citation, len(citations))] += 1
        total = 0
        for h in range(len(buckets) - 1, -1, -1):
            total += buckets[h]
            if total >= h:
                return h
        return 0
